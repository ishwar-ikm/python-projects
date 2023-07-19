import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


year = input("To create a Spotify playlist for top 100 songs from a specific date, enter the date in the format YYYY-MM-DD.")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

song_name = [x.getText().strip() for x in soup.select("li ul li h3")]
print(song_name)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='Your spotify client id',
        client_secret='Your spotify client id secret',
        show_dialog=True,
        cache_path="token.txt",
        username='Your spotify username',
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = year.split("-")[0]
for song in song_name:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
