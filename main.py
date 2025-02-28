from fastapi import FastAPI
import requests

app = FastAPI()  # This must exist

API_KEY = "AIzaSyBAitoYGdwYIymiWgfzRu-oNocH6afah58"  # Replace with your actual YouTube API key

@app.get("/")  # Add this route to check if API is running
def home():
    return {"message": "YouTube API is running!"}

@app.get("/search")  # Correct route
def search_video(query: str):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "items" not in data or not data["items"]:
        return {"error": "No results found"}

    video_id = data["items"][0]["id"]["videoId"]
    video_link = f"https://www.youtube.com/watch?v={video_id}"
    
    return {"video_link": video_link}
