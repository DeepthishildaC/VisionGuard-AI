from app.ai.model import model

def track_objects(frame):
    """
    Detect and track objects using YOLOv8 + ByteTrack.

    Returns:
    [
        {
            "id": 5,
            "class": "person",
            "confidence": 0.94,
            "bbox": [100,50,220,400]
        }
    ]
    """

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.4,
        verbose=False,
    )

    tracked_objects = []

    for result in results:

        if result.boxes is None:
            continue

        for box in result.boxes:

            # Skip detections that don't yet have a tracking ID
            if box.id is None:
                continue

            track_id = int(box.id.item())

            class_id = int(box.cls.item())
            class_name = model.names[class_id]

            confidence = float(box.conf.item())

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            tracked_objects.append(
                {
                    "id": track_id,
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

    return tracked_objects