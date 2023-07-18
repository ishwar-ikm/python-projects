import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies = [m.getText() for m in soup.select(".article-title-description__text .title")]
movies = list(reversed(movies))
with open("top_movies_list.txt.", mode='w', encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie} \n")