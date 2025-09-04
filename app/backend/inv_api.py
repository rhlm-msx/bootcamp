from typing import Optional
import json
from fastapi.responses import HTMLResponse, Response
from fastapi import APIRouter, HTTPException
from backend.cdn import Assets


'''

inventory/listing
inventory/id/{id}

'''

inv_router = APIRouter(prefix="/inventory")
buck = Assets("locals3")
data = buck.fetchContent("dataset_products.json")
data = json.loads(data)
import pandas as pd
data = pd.DataFrame(data)
data = data.fillna(-1)
cols = data.columns


data = [ { col: row[col] for col in cols } for index, row in data.iterrows()]


@inv_router.get("/summary", description="Produces summary of the inventory", tags=["Inventory Summary"])
async def summary():
    return {
        "entity_count" : len(data)
            }

@inv_router.get("/listing", description="Complete list of inventory", tags=["Inventory Listing"])
async def inventory_listing():
    return data


@inv_router.get("/listing/{item_id}", tags=["Inventory Listing"])
async def inventory_listing(item_id: Optional[int]):
    if len(data) < (item_id - 1):
        raise HTTPException(status_code=404, detail="Entity Not Exist")
    return data[item_id]
