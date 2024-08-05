from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

print("check")
try:
    conn = psycopg2.connect(host = "localhost", database="fastapi-database", 
                            user="postgres", password="postgres", cursor_factory=RealDictCursor)

    cursor = conn.cursor()

    print("database connected successfully")
except Exception as err:
    print("exception occured")

    print("Error", err)


my_posts = [
    {
        "title":"this is tile1",
        "content": "this is content1" 
    },
        {
        "title":"this is tile2",
        "content": "this is content2" 
    }
]

@app.get("/")
async def root():           
    return {"message": "Hello World !!"}

@app.post("/posts")
async def createPost(payload: Post):
    # print(payload)

    # print(payload.model_dump())
    

    print("json dump", payload.model_dump_json())

    print("dump", payload.model_dump())

    my_posts.append(payload.model_dump())
    
    return {"new post": "done"}

    # return {"new post": f"title {payload["title"]} content: {payload["content"].upper()}"}

