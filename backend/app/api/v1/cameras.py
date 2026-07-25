from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.camera import (
    CameraCreate,
    CameraUpdate,
    CameraResponse,
)
from app.crud.camera import (
    create_camera,
    get_all_cameras,
    get_camera,
    update_camera,
    delete_camera,
)

router = APIRouter(
    prefix="/camera",
    tags=["Camera"],
)


@router.post("/", response_model=CameraResponse)
def add_camera(
    camera: CameraCreate,
    db: Session = Depends(get_db),
):
    return create_camera(db, camera)


@router.get("/", response_model=list[CameraResponse])
def list_cameras(
    db: Session = Depends(get_db),
):
    return get_all_cameras(db)


@router.get("/{camera_id}", response_model=CameraResponse)
def get_camera_by_id(
    camera_id: int,
    db: Session = Depends(get_db),
):
    camera = get_camera(db, camera_id)

    if not camera:
        raise HTTPException(
            status_code=404,
            detail="Camera not found",
        )

    return camera


@router.put("/{camera_id}", response_model=CameraResponse)
def edit_camera(
    camera_id: int,
    camera: CameraUpdate,
    db: Session = Depends(get_db),
):
    updated = update_camera(
        db,
        camera_id,
        camera,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Camera not found",
        )

    return updated


@router.delete("/{camera_id}")
def remove_camera(
    camera_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_camera(
        db,
        camera_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Camera not found",
        )

    return {
        "message": "Camera deleted successfully"
    }