import cv2

from app.ai.camera import open_camera
from app.ai.detector import detect_objects

cap = open_camera()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    detections = detect_objects(frame)

    for det in detections:

        x1, y1, x2, y2 = det["bbox"]

        label = (
            f'{det["class"]} '
            f'{det["confidence"]:.2f}'
        )

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )

    cv2.imshow("VisionGuard AI", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()