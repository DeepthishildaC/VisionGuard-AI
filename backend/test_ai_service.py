import cv2

from app.ai.pipeline import process_frame

from app.database.database import SessionLocal

from app.services.ai_service import save_ai_results

db = SessionLocal()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    tracked_objects, events = process_frame(frame)

    if events:
        save_ai_results(
            db=db,
            camera_id=1,
            tracked_objects=tracked_objects,
            events=events,
        )

        print(events)

    cv2.imshow("VisionGuard AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
db.close()
cv2.destroyAllWindows()