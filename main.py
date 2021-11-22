from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "your-unique-client-token"
CLIENT_SECRET = "cleint-secret"
REDIRECT_URI = "http://example.com"
scope = "playlist-modify-private"

# you can ask user to enter a specific date
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(url="https://www.billboard.com/charts/hot-100/2021-11-22")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_li = []
for tag in soup.findAll(name="span", class_="chart-element__information__song"):
    song_li.append(tag.getText())

cred = spotipy.Spotify(auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope,
    show_dialog=True,
    cache_path="my_token.txt"
))

user_id = cred.current_user()["id"]
# ["id"]
track_uri = "spotify:track:4iJyoBOLtHqaGxP"
result = cred.search(q="track:Peaches", type="track")
uri = result["tracks"]["items"][0]["uri"]
song_uris = [uri]


playlist_create = cred.user_playlist_create(user=user_id, name="my_bests", public=False, description="first created playlist")
cred.playlist_add_items(playlist_id=playlist_create["id"], items=song_uris)

