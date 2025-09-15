from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse,Response
from backend.cdn import Assets
from backend.env import MAIN_BUCKET_NAME

asset_router = APIRouter(prefix="/assets")
buck = Assets(MAIN_BUCKET_NAME)


@asset_router.get("/image/{pid}", response_class=Response)
async def fetchImage(pid: int):
    data = buck.fetchContent(f"dataset_product_images_product_img_{pid}.png")
    if data == None:
        raise HTTPException(status_code=404, detail="Entity Not Found")
    return Response(content=data, media_type="application/image+png")

    
