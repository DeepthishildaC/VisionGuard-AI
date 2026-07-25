import cv2

from app.ai.detector import detect_objects

image = cv2.imread("sample_images/person.jpg")

detections = detect_objects(image)

for det in detections:

    x1, y1, x2, y2 = det["bbox"]

    label = f'{det["class"]} {det["confidence"]:.2f}'

    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2,
    )

    cv2.putText(
        image,
        label,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )

cv2.imshow("VisionGuard AI", image)
cv2.waitKey(0)
cv2.destroyAllWindows()