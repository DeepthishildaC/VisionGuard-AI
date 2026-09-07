from app.ai.model import model


def detect_objects(frame):
    """
    Detect every object visible in the frame.

    Returns:
    [
        {
            "class": "person",
            "confidence": 0.97,
            "bbox": [x1, y1, x2, y2]
        }
    ]
    """

    # Lower confidence -> detects more objects
    results = model(
        frame,
        conf=0.25,
        verbose=False,
    )

    detections = []

    for result in results:

        for box in result.boxes:

            # Bounding Box Coordinates
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # Confidence
            confidence = float(box.conf[0])

            # Object Class
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            detections.append(
                {
                    "class": class_name,
                    "confidence": round(confidence, 2),
                    "bbox": [
                        int(x1),
                        int(y1),
                        int(x2),
                        int(y2),
                    ],
                }
            )

    return detections