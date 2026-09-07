import cv2

from app.ai.pipeline import process_frame
from app.database.database import SessionLocal

db = SessionLocal()

print("Opening webcam...")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open webcam")
    exit()

print("✅ Webcam opened successfully")

while True:

    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to read frame")
        break

    tracked_objects, events = process_frame(frame, db)

    print(f"Objects: {len(tracked_objects)} | Events: {len(events)}")

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
            0.7,
            (0, 255, 0),
            2,
        )

    cv2.imshow("VisionGuard AI", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        print("Exiting...")
        break

cap.release()
db.close()
cv2.destroyAllWindows()