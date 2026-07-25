from sqlalchemy.orm import Session

from app.models.detection import Detection
from app.schemas.detection import (
    DetectionCreate,
    DetectionUpdate,
)


def create_detection(db: Session, detection: DetectionCreate):
    db_detection = Detection(**detection.model_dump())

    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)

    return db_detection


def get_all_detections(db: Session):
    return db.query(Detection).all()


def get_detection(db: Session, detection_id: int):
    return (
        db.query(Detection)
        .filter(Detection.id == detection_id)
        .first()
    )


def update_detection(
    db: Session,
    detection_id: int,
    detection: DetectionUpdate,
):
    db_detection = get_detection(db, detection_id)

    if not db_detection:
        return None

    for key, value in detection.model_dump(exclude_unset=True).items():
        setattr(db_detection, key, value)

    db.commit()
    db.refresh(db_detection)

    return db_detection


def delete_detection(
    db: Session,
    detection_id: int,
):
    db_detection = get_detection(db, detection_id)

    if not db_detection:
        return None

    db.delete(db_detection)
    db.commit()

    return True