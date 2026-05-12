from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from recommender import CourseRecommender

app = FastAPI(
    title="Course Recommendation API",
    version="1.0.0"
)

print("Starting recommendation engine...")

recommender = CourseRecommender()

print("Recommendation engine ready")

class RecommendationRequest(BaseModel):

    query: str

    difficulty: Optional[str] = None

    top_n: int = 5

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }

@app.post("/recommend")
def recommend_courses(request: RecommendationRequest):

    results = recommender.recommend_courses(
        query=request.query,
        difficulty=request.difficulty,
        top_n=request.top_n
    )

    return results.to_dict(orient="records")