from fastapi import FastAPI
import aiohttp

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/fetch_post_async/{post_id}")
async def fetch_post_async(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {"error": "Post not found"}