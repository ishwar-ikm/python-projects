# Importing the required libraries
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Getting the year input from the user to create the playlist for top 100 songs from that specific date
year = input("To create a Spotify playlist for top 100 songs from a specific date, enter the date in the format YYYY-MM-DD.")

# Fetching the Billboard webpage for the specified year
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/")
webpage = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Extracting the names of the songs from the Billboard webpage
song_name = [x.getText().strip() for x in soup.select("li ul li h3")]
print(song_name)

# Authenticating with Spotify using the SpotifyOAuth method
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='Your spotify client id',        # Replace with your Spotify client ID
        client_secret='Your spotify client id secret',    # Replace with your Spotify client secret
        show_dialog=True,
        cache_path="token.txt",
        username='Your spotify username',    # Replace with your Spotify username
    )
)

# Getting the user ID of the current authenticated user
user_id = sp.current_user()["id"]
print(user_id)

# Initializing an empty list to store the Spotify URIs of the songs
song_uris = []

# Extracting only the year from the entered date (to use in Spotify search query)
year = year.split("-")[0]

# Searching for each song on Spotify and appending its URI to the song_uris list
for song in song_name:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
print(playlist)

# Adding the found songs to the newly created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
