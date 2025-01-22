from fastapi import FastAPI, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "starwars3"

class Content(BaseModel):
    type: str
    text: Union[str, None] = None
    url: Union[str, None] = None
    
class Details(BaseModel):
    description: str
    content: List[Content]

class NewsItem(BaseModel):
    name: str
    image: str
    date: str
    details: Details

# In-memory storage for news items
news_db: List[NewsItem] = []

def verify_secret_key(request: Request):
    secret_key = request.headers.get("X-Secret-Key")
    if secret_key != SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid secret key",
        )

@app.get("/")
async def root():
    return {"message": "Welcome to the News API!"}

@app.post("/news/")
async def create_news(news_item: NewsItem, request: Request):
    verify_secret_key(request)
    news_db.append(news_item)
    return news_item

@app.get("/news/", response_model=List[NewsItem])
async def get_news():
    return news_db[::-1]

@app.get("/news/{news_id}", response_model=NewsItem)
async def get_news_item(news_id: int):
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    return news_db[news_id]

@app.put("/news/{news_id}", response_model=NewsItem)
async def update_news(news_id: int, updated_news: NewsItem, request: Request):
    verify_secret_key(request)
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    news_db[news_id] = updated_news
    return updated_news

@app.delete("/news/{news_id}", response_model=NewsItem)
async def delete_news(news_id: int, request: Request):
    verify_secret_key(request)
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    return news_db.pop(news_id)
