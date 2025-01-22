from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Content(BaseModel):
    type: str  # e.g., "text", "image", "header", "bullet"
    value: str  # The actual content

class NewsItem(BaseModel):
    title: str
    date: str
    desc: str
    content: List[Content]  # List of content items

# In-memory storage for news items
news_db: List[NewsItem] = []


@app.get("/")
async def root():
    return {"message": "Welcome to the News API!"}

@app.post("/news/")
async def create_news(news_item: NewsItem):
    news_db.append(news_item)
    return news_item

@app.get("/news/", response_model=List[NewsItem])
async def get_news():
    return news_db

@app.get("/news/{news_id}", response_model=NewsItem)
async def get_news_item(news_id: int):
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    return news_db[news_id]

@app.put("/news/{news_id}", response_model=NewsItem)
async def update_news(news_id: int, updated_news: NewsItem):
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    news_db[news_id] = updated_news
    return updated_news

@app.delete("/news/{news_id}", response_model=NewsItem)
async def delete_news(news_id: int):
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    return news_db.pop(news_id)
