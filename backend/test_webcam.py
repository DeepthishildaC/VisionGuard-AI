import cv2

from app.ai.detector import detect_objects


# Open default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    detections = detect_objects(frame)

    for det in detections:

        x1, y1, x2, y2 = det["bbox"]

        label = f'{det["class"]} {det["confidence"]:.2f}'

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

    cv2.imshow("VisionGuard AI - Live Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()