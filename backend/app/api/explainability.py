"""Explainability API routes"""

from fastapi import APIRouter, Depends
from datetime import datetime

from app.dependencies import get_current_user, FirebaseUser
from app.schemas.explain import ExplainRequest, ExplanationTask, ExplanationResult
from app.schemas.response import APIResponse

router = APIRouter()


@router.post("/explain/model", response_model=APIResponse[ExplanationTask])
async def request_model_explanation(
    request: ExplainRequest,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Request model explanation and return task ID"""
    task = ExplanationTask(
        id=f"explain-{datetime.now().timestamp()}",
        project_id=request.project_id,
        model_id=request.model_id,
        explanation_type=request.explanation_type,
        status="pending",
        created_at=datetime.now().isoformat()
    )
    
    # Mock processing - in production, queue background task
    return APIResponse(
        success=True,
        data=task,
        message="Explanation task initiated successfully"
    )


@router.get("/explain/results/{task_id}", response_model=APIResponse[ExplanationResult])
async def get_explanation_results(
    task_id: str,
    current_user: FirebaseUser = Depends(get_current_user)
):
    """Fetch explanation results by task ID"""
    # Mock completed explanation
    result = ExplanationResult(
        task_id=task_id,
        explanation_type="shap",
        feature_importance=[
            {"feature": "age", "importance": 0.4, "value": 0.2},
            {"feature": "income", "importance": 0.3, "value": 0.1},
            {"feature": "education", "importance": 0.2, "value": 0.05},
            {"feature": "location", "importance": 0.1, "value": 0.02}
        ],
        summary="Age and income are the most important features for this prediction",
        visualizations=[
            "https://example.com/shap-waterfall.png",
            "https://example.com/feature-importance.png"
        ],
        created_at=datetime.now().isoformat()
    )
    
    return APIResponse(
        success=True,
        data=result,
        message="Explanation results retrieved successfully"
    )


