from fastapi import FastAPI
import httpx

app = FastAPI(
    title="API Gateway",
    version="1.0.0"
)

# -----------------------------------------
# Service URLs
# -----------------------------------------

RECOMMENDATION_SERVICE = "http://127.0.0.1:8001"

USER_SERVICE = "http://127.0.0.1:8002"

FEEDBACK_SERVICE = "http://127.0.0.1:8003"

# -----------------------------------------
# Health Endpoint
# -----------------------------------------

@app.get("/health")
def health_check():

    return {
        "status": "API Gateway Healthy"
    }

# -----------------------------------------
# Recommendation Service Routes
# -----------------------------------------

@app.get("/recommendation/health")
async def recommendation_health():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{RECOMMENDATION_SERVICE}/health"
        )

    return response.json()

# -----------------------------------------
# User Service Routes
# -----------------------------------------

@app.get("/users")
async def get_users():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{USER_SERVICE}/users"
        )

    return response.json()

# -----------------------------------------
# Feedback Service Routes
# -----------------------------------------

@app.get("/feedback")
async def get_feedback():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{FEEDBACK_SERVICE}/feedback"
        )

    return response.json()