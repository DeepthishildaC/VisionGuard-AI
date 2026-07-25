from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.ai_summary import (
    AISummaryCreate,
    AISummaryUpdate,
    AISummaryResponse,
)

from app.crud.ai_summary import (
    create_ai_summary,
    get_all_ai_summaries,
    get_ai_summary,
    update_ai_summary,
    delete_ai_summary,
)

router = APIRouter(
    prefix="/ai-summaries",
    tags=["AI Summaries"],
)


@router.post("/", response_model=AISummaryResponse)
def add_summary(
    summary: AISummaryCreate,
    db: Session = Depends(get_db),
):
    return create_ai_summary(db, summary)


@router.get("/", response_model=list[AISummaryResponse])
def list_summaries(
    db: Session = Depends(get_db),
):
    return get_all_ai_summaries(db)


@router.get("/{summary_id}", response_model=AISummaryResponse)
def get_summary(
    summary_id: int,
    db: Session = Depends(get_db),
):
    summary = get_ai_summary(db, summary_id)

    if not summary:
        raise HTTPException(
            status_code=404,
            detail="AI Summary not found",
        )

    return summary


@router.put("/{summary_id}", response_model=AISummaryResponse)
def edit_summary(
    summary_id: int,
    summary: AISummaryUpdate,
    db: Session = Depends(get_db),
):
    updated = update_ai_summary(
        db,
        summary_id,
        summary,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="AI Summary not found",
        )

    return updated


@router.delete("/{summary_id}")
def remove_summary(
    summary_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_ai_summary(
        db,
        summary_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="AI Summary not found",
        )

    return {
        "message": "AI Summary deleted successfully"
    }