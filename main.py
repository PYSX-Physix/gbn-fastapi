from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Union

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Content(BaseModel):
    type: str
    text: Union[str, None] = None
    url: Union[str, None] = None
    caption: Union[str, None] = None

class ArticleDetails(BaseModel):
    description: str
    content: List[Content]

class Article(BaseModel):
    name: str
    image: str
    date: str
    details: ArticleDetails

articles: Dict[str, Article] = {
    "Mojang Might be Getting Sued": Article(
        name="Mojang Might be Getting Sued",
        image="https://gbn-api.pages.dev/images/minecraft_the_pale_garden_update_released.jpg",
        date="2024-12-05",
        details=ArticleDetails(
            description="This article discusses the possible lawsuit Mojang might be facing from a long-time player and YouTuber known as Kian Brose.",
            content=[
                {"type": "subheader", "text": "Backstory"},
                {"type": "paragraph", "text": "This controversy began when a YouTuber known as Kian Brose wanted to remake a shutdown game known as McWar. After the months of programming the game was finally ready to launch, it did release on the 14th of September."},
                {"type": "paragraph", "text": "On May 30th, 2023, a Minecraft YouTuber known as: TheMisterEpic, posted about the investigation on another Minecraft Server known as \"Grand Theft Minecart\" (GTM) was under an investigation for violating the End User License Agreement (EULA). People responded to this tweet very negatively twords Mojang saying how they can just let Hypixel one of the most popular MC servers to date can get away with violating the EULA and not having any repercussions."},
                {"type": "subheader", "text": "The Allegations"},
                {"type": "image", "url": "https://i.ytimg.com/vi/C5RvoPQZQeM/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAZi4LwWg60nGcYAZU6hoHRZCUr-w", "caption": "The YouTube thumbnail from Kian Brose's lawsuit video"},
                {"type": "paragraph", "text": "Mr. Brose's lawsuit is accusing Mojang of enforcing unpublished guidelines. He claims the Terms of Service (ToS) is intentionally designed to be confusing which violates the European Consumer Protection Laws. This lawsuit also highlights the extreme amount of gambling in Minecraft Servers, these are known as crates. These are mimics of slot machines according to most of the community."},
                {"type": "subheader", "text": "The Community's Reaction"},
                {"type": "paragraph", "text": "The announcement of this lawsuit started a reaction within the Minecraft community. Many players and server owners have backed up Kian Brose and his lawsuit, arguing that Mojang's policies prevent creativity and targets types of gameplay unfairly."},
                {"type": "paragraph", "text": "A GoFundMe has been started in order to be able to make this lawsuit happen. The GoFundMe exists because Mr. Brose doesn't have money to hire a lawyer as stated in his Minecraft lawsuit video. The community wants Mojang to be more transparent about their policies and be more fair towards server owners."},
                {"type": "subheader", "text": "Conclusion"},
                {"type": "paragraph", "text": "To conclude, the lawsuit will need to be dependantly funded which you can participate in. Players and server owners hope justice is brought to Mojag for violating EU law."}
            ]
        )
    )
}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the GBN FAST API!"}

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
