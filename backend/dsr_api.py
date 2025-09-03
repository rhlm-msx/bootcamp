from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel

dsr_router = APIRouter(prefix="/dsr")


class DSRSchema(BaseModel):
    mentor: str
    week: int
    date: str
    res_chal: str
    ccl: str
    ndp: str
    work_done: Optional[List[str]]
    work_in_progress: Optional[List[str]]
    res_chal: Optional[List[str]]
    unres_chal: Optional[List[str]]


@dsr_router.post("/")
async def dsr_data(data: DSRSchema):
    return data
