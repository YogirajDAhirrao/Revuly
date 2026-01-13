from sqlmodel import Session,select
from app.models.review import Review
from app.schemas.review import ReviewFilterResponse
from app.ai.ai_service import semantic_filter

def filter_review(session:Session,payload:ReviewFilterResponse):
    reviews = session.exec(select(Review)).all()

    results = semantic_filter(query=payload.query,reviews=reviews,exclude=payload.exclude,threshold=payload.threshold,top_k=payload.top_k)

    return [review for review,score in results]
