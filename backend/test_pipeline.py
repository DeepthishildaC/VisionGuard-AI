import cv2

from app.ai.pipeline import process_frame

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    result = process_frame(frame)

    print("=" * 60)

    print("Tracked Objects")
    print(result["tracked_objects"])

    print()

    print("Events")
    print(result["events"])

    cv2.imshow("VisionGuard AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()