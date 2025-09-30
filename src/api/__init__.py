"""
API package: exposes a small FastAPI app with endpoints that call into services.
"""
from .main import app  # re-export for uvicorn discoverability
