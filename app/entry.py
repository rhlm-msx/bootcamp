from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, HTTPException
from modules.inv import invAPI
from modules.main import mainAPI
from modules.embed import embedAPI

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


@app.exception_handler(RequestValidationError)
async def overrideValidationError(req, exc):
    raise HTTPException(status_code=400, detail="Not a valid input")


app.include_router(invAPI)
app.include_router(mainAPI)
app.include_router(embedAPI)