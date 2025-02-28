import requests

API_KEY = "AIzaSyBAitoYGdwYIymiWgfzRu-oNocH6afah58"
SEARCH_QUERY = "Shape of You Ed Sheeran"
URL = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={SEARCH_QUERY}&type=video&key={API_KEY}"

response = requests.get(URL)
data = response.json()

# Extract the first video ID
video_id = data["items"][0]["id"]["videoId"]
video_link = f"https://www.youtube.com/watch?v={video_id}"

print("YouTube Video Link:", video_link)