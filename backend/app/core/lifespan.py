"""
Application startup and shutdown events.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting AI Study Assistant Backend...")
    yield
    print("Shutting down AI Study Assistant Backend...")