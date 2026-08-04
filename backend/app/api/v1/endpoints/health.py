"""
Health check endpoints.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health",
    tags=["Health"],
    summary="Health Check",
)
async def health():
    """
    Returns backend health.
    """

    return {
        "status": "healthy",
        "service": "AI Study Assistant",
    }