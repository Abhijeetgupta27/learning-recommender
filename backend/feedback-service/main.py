from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Feedback Service",
    version="1.0.0"
)

# -----------------------------------------
# Feedback Model
# -----------------------------------------

class Feedback(BaseModel):

    username: str

    course_title: str

    rating: int

    comment: str

# -----------------------------------------
# Temporary Feedback Storage
# -----------------------------------------

feedback_list = []

# -----------------------------------------
# Health Endpoint
# -----------------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "Feedback Service Healthy"
    }

# -----------------------------------------
# Submit Feedback
# -----------------------------------------

@app.post("/feedback")
def submit_feedback(feedback: Feedback):

    feedback_list.append(feedback.dict())

    return {
        "message": "Feedback submitted successfully",
        "feedback": feedback
    }

# -----------------------------------------
# Get All Feedback
# -----------------------------------------

@app.get("/feedback")
def get_feedback():

    return feedback_list

# -----------------------------------------
# Get Feedback By Course
# -----------------------------------------

@app.get("/feedback/{course_title}")
def get_course_feedback(course_title: str):

    results = []

    for feedback in feedback_list:

        if feedback["course_title"].lower() == course_title.lower():

            results.append(feedback)

    return results