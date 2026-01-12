from sqlmodel import Session, select
from app.models.review import Review
from app.schemas.review import ReviewCreate

def create_review(session: Session, review_data: ReviewCreate):
    review = Review.model_validate(review_data)
    session.add(review)
    session.commit()
    session.refresh(review)
    return review

def get_all_reviews(session: Session):
    statement = select(Review)
    results = session.exec(statement)
    return results.all()

def get_review_by_id(session:Session,review_id:int)->Review| None:
    return session.get(Review,review_id)

