from collections import Counter


def detect_events(tracked_objects):
    """
    Convert tracked objects into high-level security events.

    Input:
    [
        {
            "id": 1,
            "class": "person",
            "confidence": 0.93,
            "bbox": [100,50,250,400]
        }
    ]

    Output:
    [
        {
            "event": "Person Detected",
            "risk": "LOW"
        }
    ]
    """

    events = []

    class_counter = Counter()

    for obj in tracked_objects:

        object_name = obj["class"]

        class_counter[object_name] += 1

        # ----------------------------
        # Person
        # ----------------------------

        if object_name == "person":

            events.append(
                {
                    "event": "Person Detected",
                    "risk": "LOW",
                    "track_id": obj["id"],
                    "bbox": obj["bbox"],
                }
            )

        # ----------------------------
        # Vehicle
        # ----------------------------

        elif object_name in [
            "car",
            "truck",
            "bus",
            "motorcycle",
            "bicycle",
        ]:

            events.append(
                {
                    "event": f"{object_name.title()} Detected",
                    "risk": "LOW",
                    "track_id": obj["id"],
                    "bbox": obj["bbox"],
                }
            )

    # ----------------------------
    # Crowd Detection
    # ----------------------------

    if class_counter["person"] >= 5:

        events.append(
            {
                "event": "Crowd Formation",
                "risk": "MEDIUM",
                "count": class_counter["person"],
            }
        )

    return events