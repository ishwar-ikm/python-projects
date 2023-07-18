# Importing the required libraries
import requests
from bs4 import BeautifulSoup

# Sending a GET request to the Empire Online webpage
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Selecting all the elements with the class "article-title-description__text" and "title"
movies = [m.getText() for m in soup.select(".article-title-description__text .title")]

# Reversing the order of the movies list
movies = list(reversed(movies))

# Opening a file called "top_movies_list.txt" in write mode
# Using UTF-8 encoding to support special characters
with open("top_movies_list.txt.", mode='w', encoding="utf-8") as file:
    # Writing each movie to the file, followed by a new line character
    for movie in movies:
        file.write(f"{movie} \n")
