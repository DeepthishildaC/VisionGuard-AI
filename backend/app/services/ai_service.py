from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.models.detection import Detection
from app.models.alert import Alert
from app.models.ai_summary import AISummary


def save_ai_results(
    db: Session,
    camera_id: int,
    tracked_objects: list,
    events: list,
):
    """
    Save AI detections into the database.

    Pipeline:

    Tracked Objects
            ↓
        Event Engine
            ↓
       Incident
            ↓
       Detection
            ↓
         Alert
            ↓
      AI Summary
    """

    for event in events:

        # -----------------------------
        # Create Incident
        # -----------------------------
        incident = Incident(
            event_type=event["event"],
            risk_level=event.get("risk", "LOW"),
            description=f"{event['event']} detected by AI.",
            confidence=0.95,
            status="OPEN",
            camera_id=camera_id,
        )

        db.add(incident)
        db.commit()
        db.refresh(incident)

        # -----------------------------
        # Save related detections
        # -----------------------------
        for obj in tracked_objects:

            if obj["id"] != event.get("track_id"):
                continue

            detection = Detection(
                object_type=obj["class"],
                confidence=obj["confidence"],
                track_id=obj["id"],
                bounding_box=",".join(
                    map(str, obj["bbox"])
                ),
                incident_id=incident.id,
            )

            db.add(detection)

        db.commit()

        # -----------------------------
        # Create Alert
        # -----------------------------
        alert = Alert(
            title=event["event"],
            message=f"{event['event']} detected.",
            severity=event.get("risk", "LOW"),
            status="ACTIVE",
            is_read=False,
            incident_id=incident.id,
        )

        db.add(alert)
        db.commit()

        # -----------------------------
        # Create AI Summary
        # -----------------------------
        summary = AISummary(
            summary=(
                f"VisionGuard AI detected "
                f"{event['event']} "
                f"with {event.get('risk','LOW')} risk."
            ),
            model_name="YOLOv8 + ByteTrack",
            confidence="95%",
            incident_id=incident.id,
        )

        db.add(summary)
        db.commit()