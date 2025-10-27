from fastapi import FastAPI, APIRouter, HTTPException
from campaign_data import campaigns_list

app = FastAPI()

api = APIRouter(prefix = "/api/v1")

@api.get("/")
async def root():
    return {"Hello": "World"}

@api.get("/campaigns")
async def get_all_campaigns():
    return {"campaigns": campaigns_list}

@api.get("/campaigns/{id}")
async def get_campaign_by_id(id: int):
    for campaign in campaigns_list:
        if campaign["campaign_id"] == id:
            return {"campaigns": campaign}
    raise HTTPException(status_code=404, detail="Campaign not found")

app.include_router(api)