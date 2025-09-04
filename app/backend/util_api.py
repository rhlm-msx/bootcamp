from fastapi import FastAPI, APIRouter
from backend.asset_api import buck
import pywal



utils_router = APIRouter(prefix="/utils")


@utils_router.get("/colors/{asset_id}")
async def getColor(asset_id: int):
    key = f"dataset_product_images_product_img_{asset_id}.png"
    file = buck.fetchContentasFile(key)
    colors = pywal.colors.get(f"/tmp/{key}")
    return colors

@utils_router.post("/colors/")
async def getColor():
    colors = None
    return colors


