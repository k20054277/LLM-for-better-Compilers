
from fastapi import FastAPI, BackgroundTasks
import asyncio
import aiohttp
import time

app = FastAPI()

@app.get("/sync")
def sync_endpoint():
    """Synchronous endpoint"""
    return {"message": "This is a synchronous response"}

@app.get("/async")
async def async_endpoint(background_tasks: BackgroundTasks):
    """Asynchronous endpoint"""
    background_tasks.add_task(send_email, "test@example.com", "Hello World!")
    await background_tasks.wait_for_completion()
    return {"message": "This is an asynchronous response"}

async def send_email(to: str, body: str):
    """Send email using aiohttp"""
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/api/send-email", json={"to": to, "body": body}) as response:
            data = await response.json()
            print(f"Email sent! Status code: {data['status']}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
