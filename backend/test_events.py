import cv2

from app.ai.tracker import track_objects
from app.ai.events import detect_events

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    tracked_objects = track_objects(frame)

    events = detect_events(tracked_objects)

    # Draw tracked objects
    for obj in tracked_objects:

        x1, y1, x2, y2 = obj["bbox"]

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f'{obj["class"]} #{obj["id"]}',
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )

    # Display detected events
    y = 30

    for event in events:

        cv2.putText(
            frame,
            event["event"],
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
        )

        y += 30

    cv2.imshow("VisionGuard AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()