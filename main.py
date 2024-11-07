from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define the article data model

class Details(BaseModel):
    description: str
    content: str

class Article(BaseModel):
    title: str
    image: str
    date: Optional[str] = None
    details: Details


# In-memory database of articles
articles_db = [
    {
        "name": "Black Ops 6 Season 01 Official Announcement",
        "image": "https://gbn-api.pages.dev/images/BO6-SEASON-01-ANNOUNCEMENT-001.jpg",
        "date": "November 7, 2024",
        "details":{
            "description": "This article talks about the official announcement of Black Ops 6 Season 01.",
            "content": "Sony has decided to shut down Firewalk Studios after a horrible game release by the name of Concord that costed $40 on the PS5 Store. The release was very bad and only stayed around for two weeks, the official IGN account gave the game a 7 out of 10."
        }
    },
    {
        "name": "Sony Shuts Down Firewalk Studios After Terrible Release",
        "image": "https://gbn-api.pages.dev/images/concord-central-art.jpg",
        "date": "November 6, 2024",
        "details":{
            "description": "This article talks about how Sony shutdown a game studio after a very bad game launch.",
            "content": "Sony has decided to shut down Firewalk Studios after a horrible game release by the name of Concord that costed $40 on the PS5 Store. The release was very bad and only stayed around for two weeks, the official IGN account gave the game a 7 out of 10."
        }
    },
    {
        "name": "CoD BO6 Season 1 Everything we Know",
        "image": "https://gbn-api.pages.dev/images/COD-BO6-COD-101-TOUT.jpg",
        "date": "November 5, 2024",
        "details":{
            "description": "This article talks about Call of Duty: Black Ops 6 Season 01 coming soon and showing everything known coming up on November 14th.",
            "content": "Call of Duty: Black Ops 6 is coming here is everything we know."
        }
    },
    
    {
        "name": "Call of Duty: Black Ops 6 Releases Nuketown",
        "image": "https://gbn-api.pages.dev/images/COD-BO6-S0-ANNOUNCEMENT-002.jpg",
        "date": "November 1, 2024",
        "details":{
            "description": "This article talks about Call of Duty: Black Ops 6 devs Treyarch released Nuketown and how players love the remastered design.",
            "content": "Treyarch releases Nuketown in Call of Duty: Black Ops 6."
        }
    },

    {
        "name": "Fortnite Reveals Ice Spice & Players Aren't Happy",
        "image": "https://gbn-api.pages.dev/images/fortnite-chapter-2-remix-ice-spice-1920x1080.jpg",
        "date": "November 1, 2024",
        "details":{
            "description": "This article talks about when Fortnite revealed celebrities such as Ice Spice, Snoop Dogg, and Eminem and how're they taking over point-of-interest's instead of the og chapter 2 versions.",
            "content": "Players are not happy with Ice Spice and other rappers taking over the island."
        }
    }
]


@app.get("/")
async def read_root():
    return {"message": "GBN API go to https://gbn.pages.dev/articles/ if you wish to use the API. This is open source and usable by everyone."}

@app.get("/articles/", response_model=List[Article])
async def get_articles(search: Optional[str] = None):
    if search:
        # Filter articles by search query
        filtered_articles = [article for article in articles_db if search.lower() in article["title"].lower() or search.lower() in article["description"].lower()]
        if not filtered_articles:
            raise HTTPException(status_code=404, detail="No articles found matching the search criteria.")
        return filtered_articles
    return articles_db
