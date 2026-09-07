from sqlalchemy.orm import Session

from app.ai.tracker import track_objects
from app.ai.events import detect_events

from app.crud.incident import create_incident
from app.crud.detection import create_detection
from app.crud.alert import create_alert
from app.crud.ai_summary import create_ai_summary

from app.schemas.incident import IncidentCreate
from app.schemas.detection import DetectionCreate
from app.schemas.alert import AlertCreate
from app.schemas.ai_summary import AISummaryCreate

from app.services.incident_manager import (
    has_active_incident,
    register_incident,
    update_last_seen,
)


def process_frame(frame, db: Session):
    """
    VisionGuard AI Pipeline

    Camera Frame
          ↓
      Object Tracking
          ↓
      Event Detection
          ↓
      Incident Manager
          ↓
    PostgreSQL Database
    """

    # -----------------------------------------
    # Track objects
    # -----------------------------------------

    tracked_objects = track_objects(frame)

    # -----------------------------------------
    # Detect security events
    # -----------------------------------------

    events = detect_events(tracked_objects)

    # -----------------------------------------
    # Process every event
    # -----------------------------------------

    for event in events:

        track_id = event.get("track_id")

        # Crowd event has no track id
        if track_id is None:
            continue

        # Ignore duplicate incidents
        if has_active_incident(track_id):

            update_last_seen(track_id)

            continue

        print(f"\nCreating Incident for Track ID {track_id}")

        # -----------------------------------------
        # Find matching tracked object
        # -----------------------------------------

        tracked_object = next(
            (
                obj
                for obj in tracked_objects
                if obj["id"] == track_id
            ),
            None,
        )

        if tracked_object is None:
            continue

        # -----------------------------------------
        # Create Incident
        # -----------------------------------------

        incident = create_incident(
            db,
            IncidentCreate(
                event_type=event["event"],
                risk_level=event.get("risk", "LOW"),
                description=f'{event["event"]} detected by VisionGuard AI.',
                confidence=tracked_object["confidence"],
                image_path="",
                video_path="",
                camera_id=1,
            ),
        )

        # -----------------------------------------
        # Create Detection
        # -----------------------------------------

        create_detection(
            db,
            DetectionCreate(
                object_type=tracked_object["class"],
                confidence=tracked_object["confidence"],
                track_id=track_id,
                bounding_box=",".join(
                    map(str, tracked_object["bbox"])
                ),
                incident_id=incident.id,
            ),
        )

        # -----------------------------------------
        # Create Alert
        # -----------------------------------------

        create_alert(
            db,
            AlertCreate(
                title=event["event"],
                message=f'{event["event"]} detected.',
                severity=event.get("risk", "LOW"),
                incident_id=incident.id,
            ),
        )

        # -----------------------------------------
        # Create AI Summary
        # -----------------------------------------

        create_ai_summary(
            db,
            AISummaryCreate(
                summary=f'VisionGuard AI detected a {tracked_object["class"]}.',
                model_name="YOLOv8 + ByteTrack",
                confidence=str(tracked_object["confidence"]),
                incident_id=incident.id,
            ),
        )

        # -----------------------------------------
        # Register active incident
        # -----------------------------------------

        register_incident(
            track_id=track_id,
            incident_id=incident.id,
            event=event["event"],
            risk=event.get("risk", "LOW"),
        )

        print(f"Incident #{incident.id} created successfully.")

    # -----------------------------------------
    # Return results
    # -----------------------------------------

    return tracked_objects, events