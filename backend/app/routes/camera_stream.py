import cv2

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.ai.pipeline import process_frame
from app.database.database import SessionLocal

router = APIRouter()


def generate_frames():
    """
    Capture webcam frames, process them through the AI pipeline,
    draw detections, and stream them to the browser.
    """

    db = SessionLocal()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Unable to open webcam.")
        return

    print("Webcam streaming started...")

    while True:

        success, frame = cap.read()

        if not success:
            break

        # -----------------------------------------
        # Run AI Pipeline
        # -----------------------------------------

        tracked_objects, events = process_frame(frame, db)

        # -----------------------------------------
        # Draw Bounding Boxes + Event Labels
        # -----------------------------------------

        for obj in tracked_objects:

            x1, y1, x2, y2 = obj["bbox"]

            # Default values
            event_name = obj["class"]
            risk = "LOW"

            # Find matching event
            for e in events:

                if e.get("track_id") == obj["id"]:

                    event_name = e["event"]
                    risk = e.get("risk", "LOW")
                    break

            # Choose color based on risk
            if risk.upper() == "HIGH":
                color = (0, 0, 255)      # Red
            elif risk.upper() == "MEDIUM":
                color = (0, 165, 255)    # Orange
            else:
                color = (0, 255, 0)      # Green

            # Draw rectangle
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                2,
            )

            # Draw event label
            cv2.putText(
                frame,
                f"{event_name} | {risk} | ID {obj['id']}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2,
            )

        # -----------------------------------------
        # Draw Dashboard Information
        # -----------------------------------------

        cv2.putText(
            frame,
            f"Incidents: {len(events)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Tracked Objects: {len(tracked_objects)}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            "VisionGuard AI",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )

        # -----------------------------------------
        # Encode frame
        # -----------------------------------------

        _, buffer = cv2.imencode(".jpg", frame)

        frame_bytes = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame_bytes
            + b"\r\n"
        )

    cap.release()
    db.close()


@router.get("/video_feed")
def video_feed():
    """
    Live MJPEG video stream.
    """

    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )