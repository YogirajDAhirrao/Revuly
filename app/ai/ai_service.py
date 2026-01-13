from typing import List
from app.models.review import Review
from app.ai.embeddings import get_embeddings
from app.ai.similarity import cosine_similarity


def semantic_filter(
        query:str,
        reviews:List[Review],
        exclude: List[str] | None = None,
        threshold: float = 0.60,
        top_k: int = 5
):
    exclude = exclude or []
    query_embedding = get_embeddings(query)
    scored_reviews = []
    for review in reviews:
        if review.is_spam:
            continue

        if not review.embedding:
            continue

        review_text_lower = (review.clean_text or review.text).lower()
        if any(word.lower() in review_text_lower for word in exclude):
            continue

        score = cosine_similarity(query_embedding,review.embedding)

        if(score>=threshold):
            scored_reviews.append((review,score))

    scored_reviews.sort(key= lambda x:x[1],reverse=True) 

    return scored_reviews[:top_k]       