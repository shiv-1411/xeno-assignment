from fastapi import APIRouter

from app.api.v1.endpoints import tenants, ingest, auth, dashboard

api_router = APIRouter()
api_router.include_router(tenants.router, prefix="/tenants", tags=["tenants"])
api_router.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
