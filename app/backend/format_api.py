from fastapi import APIRouter
from fastapi.responses import Response
from backend.asset_api import buck


format_router = APIRouter(prefix="/format")

@format_router.get("/output")
async def getOutput():
    return Response(content=buck.fetchContent("wal.pdf"), media_type="application/pdf")
