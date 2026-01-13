from sqlmodel import Session, select
from app.models.review import Review
from app.schemas.review import ReviewCreate
from app.ai.embeddings import get_embeddings

def create_review(session: Session, review_data: ReviewCreate):

    clean_text = review_data.text.strip().lower()
    embedding = get_embeddings(clean_text)

    review = Review(
        text = review_data.text,
        clean_text = clean_text,
        rating= review_data.rating,
        is_spam=False,
        embedding=embedding,
    )

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

