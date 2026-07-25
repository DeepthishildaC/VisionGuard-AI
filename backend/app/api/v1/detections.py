from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.detection import (
    DetectionCreate,
    DetectionUpdate,
    DetectionResponse,
)

from app.crud.detection import (
    create_detection,
    get_all_detections,
    get_detection,
    update_detection,
    delete_detection,
)

router = APIRouter(
    prefix="/detections",
    tags=["Detections"],
)


@router.post("/", response_model=DetectionResponse)
def add_detection(
    detection: DetectionCreate,
    db: Session = Depends(get_db),
):
    return create_detection(db, detection)


@router.get("/", response_model=list[DetectionResponse])
def list_detections(
    db: Session = Depends(get_db),
):
    return get_all_detections(db)


@router.get("/{detection_id}", response_model=DetectionResponse)
def get_detection_by_id(
    detection_id: int,
    db: Session = Depends(get_db),
):
    detection = get_detection(db, detection_id)

    if not detection:
        raise HTTPException(
            status_code=404,
            detail="Detection not found",
        )

    return detection


@router.put("/{detection_id}", response_model=DetectionResponse)
def edit_detection(
    detection_id: int,
    detection: DetectionUpdate,
    db: Session = Depends(get_db),
):
    updated = update_detection(
        db,
        detection_id,
        detection,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Detection not found",
        )

    return updated


@router.delete("/{detection_id}")
def remove_detection(
    detection_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_detection(
        db,
        detection_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Detection not found",
        )

    return {
        "message": "Detection deleted successfully"
    }