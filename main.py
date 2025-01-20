from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ArticleDetails(BaseModel):
    description: str
    content: str

class Article(BaseModel):
    name: str
    image: str
    date: str
    details: ArticleDetails

articles: Dict[str, Article] = {}

@app.get("/articles/", response_model=List[Article])
async def get_articles():
    return list(articles.values())[::-1]

@app.post("/articles/", response_model=Article)
async def add_article(article: Article):
    if article.name in articles:
        raise HTTPException(status_code=400, detail="Article already exists")
    articles[article.name] = article
    return article

@app.put("/articles/{article_name}", response_model=Article)
async def update_article(article_name: str, updated_article: Article):
    if article_name not in articles:
        raise HTTPException(status_code=404, detail="Article not found")
    articles[article_name] = updated_article
    return updated_article

@app.delete("/articles/{article_name}", response_model=Article)
async def delete_article(article_name: str):
    if article_name not in articles:
        raise HTTPException(status_code=404, detail="Article not found")
    return articles.pop(article_name)
