from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.schemas.alert import AlertCreate, AlertUpdate


def create_alert(db: Session, alert: AlertCreate):
    db_alert = Alert(**alert.model_dump())

    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)

    return db_alert


def get_all_alerts(db: Session):
    return db.query(Alert).all()


def get_alert(db: Session, alert_id: int):
    return db.query(Alert).filter(Alert.id == alert_id).first()


def update_alert(db: Session, alert_id: int, alert: AlertUpdate):
    db_alert = get_alert(db, alert_id)

    if not db_alert:
        return None

    for key, value in alert.model_dump(exclude_unset=True).items():
        setattr(db_alert, key, value)

    db.commit()
    db.refresh(db_alert)

    return db_alert


def delete_alert(db: Session, alert_id: int):
    db_alert = get_alert(db, alert_id)

    if not db_alert:
        return None

    db.delete(db_alert)
    db.commit()

    return True