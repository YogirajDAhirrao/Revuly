from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas.review import ReviewView, ReviewCreate
from app.db.session import get_session
from app.services.review_service import *
router = APIRouter()

@router.post("/",response_model= ReviewView)
def add_review(review: ReviewCreate,session: Session = Depends(get_session)):
    return create_review(session,review)

@router.get("/get-all", response_model=List[ReviewView])
def list_all_reviews(session: Session = Depends(get_session)):
    return get_all_reviews(session)

@router.get("/{review_id}",response_model=ReviewView)
def get_by_id(review_id:int,session:Session = Depends(get_session)):
    review = get_review_by_id(session,review_id)
    if not review:
        raise HTTPException(status_code=404,detail="Review Not found")
    return review