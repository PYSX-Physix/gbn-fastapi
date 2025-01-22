from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List, Union
import jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "starwars3"
ALGORITHM = "HS256"

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

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


@app.get("/")
async def root():
    return {"message": "Welcome to the News API!"}

@app.post("/news/")
async def create_news(news_item: NewsItem, token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
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
async def update_news(news_id: int, updated_news: NewsItem):
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    news_db[news_id] = updated_news
    return updated_news

@app.delete("/news/{news_id}", response_model=NewsItem)
async def delete_news(news_id: int, token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if news_id >= len(news_db):
        raise HTTPException(status_code=404, detail="News item not found")
    return news_db.pop(news_id)
