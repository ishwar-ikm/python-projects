# Billboard Top 100 Spotify Playlist Creator

This script creates a Spotify playlist containing the top 100 songs from the Billboard Hot 100 chart for a specific date. It utilizes the BeautifulSoup library to scrape the Billboard website for the song names, and the Spotipy library to interact with the Spotify API to create playlist.

The script will prompt you to enter a date in the format YYYY-MM-DD. It will then scrape the Billboard website for the top 100 songs for that date and create a new private playlist in your Spotify account named "{year} Billboard 100."

The script will attempt to find each song on Spotify and add them to the newly created playlist. If a song is not found on Spotify, it will be skipped, and a message will be displayed in the console.

# Spotify Authorization

The script uses the Spotipy library's SpotifyOAuth to handle Spotify authorization. This means the first time you run the script, it will open a web page in your default browser, asking you to log in to Spotify and grant access to your account. The script will then store the access token in a token.txt file for future use.
Note: The scope used for authorization is playlist-modify-private, which allows the script to create and modify private playlists in your Spotify account.
