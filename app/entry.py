import os
import sys
import asyncio

os.environ["HOME"] = os.environ.get("HOME", "/home")

from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from mangum import Mangum

from backend.inv_api import inv_router
from backend.asset_api import asset_router
from backend.util_api import utils_router
from backend.dsr_api import dsr_router
from backend.format_api import format_router



try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])

@app.exception_handler(RequestValidationError)
async def validationError(req, excp):
    return JSONResponse({
        "msg": "error"
        }, status_code=500)

@app.get("/")
async def redirect_to_app():
    return RedirectResponse(url="/app")

app.mount("/app", StaticFiles(directory="static", html=True), name="app")
app.include_router(inv_router)
app.include_router(asset_router)
app.include_router(utils_router)
app.include_router(dsr_router)
app.include_router(format_router)


mangumHandler = Mangum(app)


urlfix = lambda pattern,path: path if pattern not in path or pattern.endswith("/") else (path + "/")
def fixdict(dt, key):
    dt[key] = urlfix("app", dt[key])
    return dt[key]

def handler(event, context):
    print(fixdict(event, "rawPath"))
    print(fixdict(event["requestContext"]["http"], "path"))
    return mangumHandler(event, context)
