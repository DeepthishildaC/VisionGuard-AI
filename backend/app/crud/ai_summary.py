from sqlalchemy.orm import Session

from app.models.ai_summary import AISummary
from app.schemas.ai_summary import (
    AISummaryCreate,
    AISummaryUpdate,
)


def create_ai_summary(
    db: Session,
    summary: AISummaryCreate,
):
    db_summary = AISummary(**summary.model_dump())

    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)

    return db_summary


def get_all_ai_summaries(db: Session):
    return db.query(AISummary).all()


def get_ai_summary(
    db: Session,
    summary_id: int,
):
    return (
        db.query(AISummary)
        .filter(AISummary.id == summary_id)
        .first()
    )


def update_ai_summary(
    db: Session,
    summary_id: int,
    summary: AISummaryUpdate,
):
    db_summary = get_ai_summary(db, summary_id)

    if not db_summary:
        return None

    for key, value in summary.model_dump(exclude_unset=True).items():
        setattr(db_summary, key, value)

    db.commit()
    db.refresh(db_summary)

    return db_summary


def delete_ai_summary(
    db: Session,
    summary_id: int,
):
    db_summary = get_ai_summary(db, summary_id)

    if not db_summary:
        return None

    db.delete(db_summary)
    db.commit()

    return True