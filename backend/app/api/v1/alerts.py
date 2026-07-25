from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.alert import (
    AlertCreate,
    AlertUpdate,
    AlertResponse,
)

from app.crud.alert import (
    create_alert,
    get_all_alerts,
    get_alert,
    update_alert,
    delete_alert,
)

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.post("/", response_model=AlertResponse)
def add_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db),
):
    return create_alert(db, alert)


@router.get("/", response_model=list[AlertResponse])
def list_alerts(
    db: Session = Depends(get_db),
):
    return get_all_alerts(db)


@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert_by_id(
    alert_id: int,
    db: Session = Depends(get_db),
):
    alert = get_alert(db, alert_id)

    if not alert:
        raise HTTPException(
            status_code=404,
            detail="Alert not found",
        )

    return alert


@router.put("/{alert_id}", response_model=AlertResponse)
def edit_alert(
    alert_id: int,
    alert: AlertUpdate,
    db: Session = Depends(get_db),
):
    updated = update_alert(
        db,
        alert_id,
        alert,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Alert not found",
        )

    return updated


@router.delete("/{alert_id}")
def remove_alert(
    alert_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_alert(
        db,
        alert_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Alert not found",
        )

    return {
        "message": "Alert deleted successfully"
    }