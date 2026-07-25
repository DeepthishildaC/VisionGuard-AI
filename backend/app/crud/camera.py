from sqlalchemy.orm import Session

from app.models.camera import Camera
from app.schemas.camera import CameraCreate, CameraUpdate


def create_camera(db: Session, camera: CameraCreate):
    db_camera = Camera(**camera.model_dump())
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera


def get_all_cameras(db: Session):
    return db.query(Camera).all()


def get_camera(db: Session, camera_id: int):
    return (
        db.query(Camera)
        .filter(Camera.id == camera_id)
        .first()
    )


def update_camera(
    db: Session,
    camera_id: int,
    camera: CameraUpdate,
):
    db_camera = get_camera(db, camera_id)

    if not db_camera:
        return None

    update_data = camera.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_camera, key, value)

    db.commit()
    db.refresh(db_camera)

    return db_camera


def delete_camera(db: Session, camera_id: int):
    db_camera = get_camera(db, camera_id)

    if not db_camera:
        return None

    db.delete(db_camera)
    db.commit()

    return db_camera