from fastapi import FastAPI
from modules.inv import invAPI
from modules.main import mainAPI

app = FastAPI()
app.include_router(invAPI)
app.include_router(mainAPI)