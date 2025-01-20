from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
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

articles: Dict[str, Article] = [
    {
  "name": "Mojang Might be Getting Sued",
  "image": "https://gbn-api.pages.dev/images/minecraft_the_pale_garden_update_released.jpg",
  "date": "2024-12-05",
  "details": {
    "description": "This article discusses the possible lawsuit Mojang might be facing from a long-time player and YouTuber known as Kian Brose.",
    "content": [
      {
        "type": "subheader",
        "text": "Backstory"
      },
      {
        "type": "paragraph",
        "text": "This controversy began when a YouTuber known as Kian Brose wanted to remake a shutdown game known as McWar. After the months of programming the game was finally ready to launch, it did release on the 14th of September."
      },
      {
        "type": "paragraph",
        "text": "On May 30th, 2023, a Minecraft YouTuber known as: TheMisterEpic, posted about the investigation on another Minecraft Server known as \"Grand Theft Minecart\" (GTM) was under an investigation for violating the End User License Agreement (EULA). People responded to this tweet very negatively twords Mojang saying how they can just let Hypixel one of the most popular MC servers to date can get away with violating the EULA and not having any repercussions."
      },
      {
        "type": "subheader",
        "text": "The Allegations"
      },
      {
        "type": "image",
        "url": "https://i.ytimg.com/vi/C5RvoPQZQeM/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAZi4LwWg60nGcYAZU6hoHRZCUr-w",
          "caption": "The YouTube thumbnail from Kian Brose's lawsuit video"
      },
      {
        "type": "paragraph",
        "text": "Mr. Brose's lawsuit is accusing Mojang of enforcing unpublished guidelines. He claims the Terms of Service (ToS) is intentionally designed to be confusing which violates the European Consumer Protection Laws. This lawsuit also highlights the extreme amount of gambling in Minecraft Servers, these are known as crates. These are mimics of slot machines according to most of the community. "
      },
      {
        "type": "subheader",
        "text": "The Community's Reaction"
      },
      {
        "type": "paragraph",
        "text": "The announcement of this lawsuit started a reaction within the Minecraft community. Many players and server owners have backed up Kian Brose and his lawsuit, arguing that Mojang's policies prevent creativity and targets types of gameplay unfairly."
      },
      {
        "type": "paragraph",
        "text": "A GoFundMe has been started in order to be able to make this lawsuit happen. The GoFundMe exists because Mr. Brose doesn't have money to hire a lawyer as stated in his Minecraft lawsuit video. The community wants Mojang to be more transparent about their policies and be more fair towards server owners."
      },
      {
        "type": "subheader",
        "text": "Conclusion"
      },
      {
        "type": "paragraph",
        "text": "To conclude, the lawsuit will need to be dependantly funded which you can participate in. Players and server owners hope justice is brought to Mojag for violating EU law."
      }
    ]
  }
},
    {
  "name": "XDefiant is Shutting Down",
  "image": "https://gbn-api.pages.dev/images/IMG_0416.jpeg",
  "date": "2024-12-05",
  "details": {
    "description": "In a surprising turn of events, Ubisoft has announced the shutdown of its free-to-play first-person shooter, XDefiant. The game, which was launched in May 2024, will see its servers go offline on June 3, 2025.",
    "content": [
      {
        "type": "subheader",
        "text": "A Good Start"
      },
      {
        "type": "paragraph",
        "text": "XDefiant initially showed great promise, breaking Ubisoft's internal records by surpassing five million players faster than any previous game. The game was praised for its fast-paced gameplay and unique factions, drawing comparisons to popular titles like Call of Duty."
      },
      {
        "type": "subheader",
        "text": "The Decline"
      },
      {
        "type": "paragraph",
        "text": "Despite its strong start, XDefiant struggled to maintain its player base. By October, rumors of a potential shutdown began to circulate, which were initially denied by Ubisoft. However, the game's player numbers continued to dwindle, leading to the difficult decision to discontinue the game."
      },
      {
        "type": "subheader",
        "text": "Ubisoft In the Background"
      },
      {
        "type": "paragraph",
        "text": "Although XDefiant was a huge success when it first launched, Ubisoft behind the scenes was struggling to make money and profit from their titles. As a result of this they had to lay off hundreds of employees."
      },
      {
        "type": "subheader",
        "text": "The Impact on Ubisoft"
      },
      {
        "type": "paragraph",
        "text": "The shutdown of XDefiant is part of a broader restructuring at Ubisoft, which includes the closure of its San Francisco and Osaka studios, affecting nearly 300 employees. Ubisoft's CEO, Yves Guillemot, acknowledged the challenges the company faces but expressed commitment to navigating these turbulent times and finding solutions to regain momentum."
      },
      {
        "type": "subheader",
        "text": "Community Reaction"
      },
      {
        "type": "paragraph",
        "text": "The announcement has left many fans disappointed. Players have taken to social media to express their sadness and frustration, with some even starting petitions to save the game. Despite the shutdown, Ubisoft has promised to release all planned content for Season 3 and provide refunds to players who made recent purchases."
      },
      {
        "type": "subheader",
        "text": "FaQ About XDefiant"
      },
      {
        "type": "paragraph",
        "text": "Although XDefiant will be shutting down, the servers will not go offline until June 3rd, 2025."
      },
      {
        "type": "subheader",
        "text": "Refunds"
      },
      {
        "type": "paragraph",
        "text": "Players who made any purchases within the last 30 days will recive a refund for their purchases. Anyone who bought the Ultimate Founders Addition will recive a full refund."
      },
      {
        "type": "subheader",
        "text": "Rewards & Cosmetics"
      },
      {
        "type": "paragraph",
        "text": "Ubisoft decided that because the game was going to shut down, players will be able to use any weapon cosmetic or any skins that were added in the game along with season 3 rewards."
      },
      {
        "type": "subheader",
        "text": "Closed Registration"
      },
      {
        "type": "paragraph",
        "text": "As of December 3, 2024 players will not be able to sign-up to play XDefiant. Players who already have the game owned on their account are able to download and install the game and play until June 3rd, 2025"
      }
    ]
  }
},
    {
  "name": "Fortnite Responds to Cheating Problem",
  "image": "https://gbn-api.pages.dev/images/fortnite-fncs-2025-champion-drake-community-cup-1920x1080.jpg",
  "date": "2024-11-29",
  "details": {
    "description": "Fortnite responds to the player base about the cheating problem.",
    "content": [
      {
        "type": "header",
        "text": "Background Context"
      },
      {
        "type": "paragraph",
        "text": "Cheating has been a persistent issue in online gaming, and Fortnite is no exception. To maintain the integrity of the game and provide a fair experience for all players, Epic Games has ramped up its efforts to combat cheating. This article explores the latest strategies and actions taken by Fortnite’s developers to tackle this problem."
      },
      {
        "type": "header",
        "text": "Fighting Back"
      },
      {
        "type": "paragraph",
        "text": "Epic Games has been seeing the amount of cheater rising in count and has decided to roll out new measures."
      },
      {
        "type": "subheader",
        "text": "Legal Actions"
      },
      {
        "type": "paragraph",
        "text": "Epic Games has announced that it is intensifying its legal actions against both players who cheat and those who sell cheating tools. This move aims to cut off cheating at its source by targeting the creators and distributors of cheat software"
      },
      {
        "type": "subheader",
        "text": "Tournament Rules"
      },
      {
        "type": "paragraph",
        "text": "To further discourage cheating, Fortnite has restructured its tournament rules. Players found teaming up with cheaters in tournaments will face a minimum 28-day competitive ban, which will increase with each subsequent violation. This rule applies to all team-based modes, ensuring that even those who indirectly benefit from cheating are held accountable."
      },
      {
        "type": "subheader",
        "text": "Technical Measures"
      },
      {
        "type": "paragraph",
        "text": "Epic Games continues to invest in new detection technologies to identify and prevent cheating in real-time2. These technical measures are constantly updated to stay ahead of new cheating methods, ensuring that the game remains fair and competitive."
      },
      {
        "type": "subheader",
        "text": "Community Involvement "
      },
      {
        "type": "paragraph",
        "text": "The Fortnite community plays a crucial role in the fight against cheating. By reporting suspicious behavior and staying vigilant, players help Epic Games identify and address cheating more effectively. The new rules also encourage players to be mindful of their teammates, as associating with cheaters can lead to penalties."
      }
    ]
  }
},
    {
      "name": "Black Ops 6 Season 01 Patch Notes Nov 19",
      "image": "https://gbn-api.pages.dev/images/BO6-SEASON-01-PATCH-NOTES.jpg",
      "date": "November 19, 2024",
      "details": {
        "description": "First real article. This article is about everything new with the patch notes for Black Ops 6 on November 19, 2024.",
        "content": [
          {
            "type": "paragraph",
            "text": "On November 19th, 2024 the developers of Black Ops 6: Treyarch released a patch for BO6 regarding the UI and movement. The patch notes go as follows below for the article."
          },
          {
            "type": "image",
            "url": "https://gbn-api.pages.dev/images/BO6_S1_HideoutAction_02.jpg",
            "caption": "Announcement image for the patch notes."
          },
          {
            "type": "paragraph",
            "text": "Below is the patch notes for November 19, 2024 updates will change."
          },
          {
            "type": "header",
            "text": "Global"
          },
          {
            "type": "subheader",
            "text": "Legacy XP Tokens"
          },
          {
            "type": "paragraph",
            "text": "Updated Black Ops 6 to support legacy XP token functionality"
          },
          {
            "type": "subheader",
            "text": "Gameplay"
          },
          {
            "type": "paragraph",
            "text": "Updated Black Ops 6 to support legacy XP token functionality"
          },
          {
            "type":"subheader",
            "text": "Cosmetics"
          },
          {
            "type": "paragraph",
            "text": "Addressed an issue where weapon sights would be misaligned with the Weaver Repairman Operator Skin equipped."
          },
          {
            "type": "subheader",
            "text": "Movement"
          },
          {
            "type": "paragraph",
            "text": "Reduced the minimum sprint time required to perform the following actions: dive-to-prone or slide."
          },
          {
            "type": "paragraph",
            "text": "Addressed an issue that could result in being unable to sprint when performing several actions within a short amount of time."
          },
          {
            "type":"image",
            "url":"https://gbn-api.pages.dev/images/BO6_S1_Heirloom_01.jpg"
          },
          {
            "type":"header",
            "text":"Multiplayer"
          },
          {
            "type":"subheader",
            "text":"Movement"
          },
          {
            "type":"paragraph",
            "text": "Players will no longer be taken out of sprint when taking forward-facing bullet damage with a Melee weapon equipped."
          },
          {
            "type":"header",
            "text": "Zombies"
          },
          {
              "type":"image",
              "url": "https://gbn-api.pages.dev/images/ZOM_S1_Directed_Mode_LibertyFalls.jpg"
          },
          {
            "type":"subheader",
            "text": "Maps"
          },
          {
            "type":"paragraph",
            "text":"Terminus: Addressed an issue where zombies could spawn indefinitely."
          },
          {
            "type":"paragraph",
            "text": "Liberty Falls: Addressed an issue where players would not be removed from a Chopper Gunner when starting the Main Quest Final Encounter."
          },
          {
            "type":"subheader",
            "text": "Directed Mode"
          },
          {
            "type":"paragraph",
            "text": "Exfil will now be triggered at the fifth hour of a Directed Mode Match due to a performance issue."
          },
          {
            "type":"subheader",
            "text":"GobbleGums"
          },
          {
            "type":"paragraph",
            "text":"Addressed an issue that allowed GobbleGums to persist indefinitely."
          }
        ]
      }
    }
]


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
