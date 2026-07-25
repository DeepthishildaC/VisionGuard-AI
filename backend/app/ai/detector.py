from ultralytics import YOLO

# --------------------------------------------------
# Load Pretrained YOLOv8 Nano Model
# --------------------------------------------------
model = YOLO("yolov8n.pt")


def detect_objects(frame):
    """
    Detect objects in a frame using YOLOv8.

    Returns:
        List of detections:
        [
            {
                "class": "person",
                "confidence": 0.95,
                "bbox": [x1, y1, x2, y2]
            }
        ]
    """

    # Higher confidence removes weak detections
    results = model(
        frame,
        conf=0.5,
        verbose=False,
    )

    detections = []

    # Objects useful for CCTV surveillance
    allowed_classes = {
        "person",
        "car",
        "truck",
        "bus",
        "motorcycle",
        "bicycle",
        "backpack",
        "handbag",
        "suitcase",
    }

    for result in results:

        for box in result.boxes:

            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # Confidence Score
            confidence = float(box.conf[0])

            # Class
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            # Ignore unwanted objects
            if class_name not in allowed_classes:
                continue

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