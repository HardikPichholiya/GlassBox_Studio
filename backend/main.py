"""FastAPI entry point for Glassbox AI Studio

This file creates the FastAPI app instance, includes routers, and defines
basic health endpoints. Configure CORS to allow the Next.js frontend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import users as users_router
from app.api import projects as projects_router
from app.api import fairness as fairness_router
from app.api import explainability as explainability_router
from app.api import logs as logs_router
from app.schemas.response import APIResponse

# so here we are only creating the instance of app and it is not nesscary to add the 
# version and title but it will eventually help in documentation
app = FastAPI(title="Glassbox AI Studio API", version="0.1.0")  


# CORS: Cross-Origin Resource Sharing, so this is because we are deploying our frontend 
# somewhere else and backend somewhere else so to connect both we use this

# middleware is a code that runs for each request and response
app.add_middleware(
    CORSMiddleware,
    # here this tells that what domain can talk to the backend 
    allow_origins=["*"],  # Replace with ["https://your-vercel-domain"]  
    allow_credentials=True,
    allow_methods=["*"],    # allows all methods like get, post, put, delete, etc.
    allow_headers=["*"],
)


@app.get("/health", response_model=APIResponse[dict])
def health():
    """Basic health check endpoint used by uptime checks."""
    return APIResponse(
        success=True,
        data={"status": "ok", "service": "glassbox-ai-studio"},
        message="Service is healthy"
    )


# Include all feature routers under /api

app.include_router(users_router.router, prefix="/api", tags=["users"])
app.include_router(projects_router.router, prefix="/api", tags=["projects"])
app.include_router(fairness_router.router, prefix="/api", tags=["fairness"])
app.include_router(explainability_router.router, prefix="/api", tags=["explainability"])
app.include_router(logs_router.router, prefix="/api", tags=["logs"])


