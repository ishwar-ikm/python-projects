There are two Python scripts that demonstrate web scraping using the BeautifulSoup library. The scripts extract information from different websites and perform specific tasks.

Script 1: Hacker News Top Voted Article
The first script (top_article.py) retrieves the top voted article on Hacker News. It fetches the HTML content of the https://news.ycombinator.com/ page, parses it using BeautifulSoup, and extracts the title, link, and vote count for each article. Finally, it displays the title, link, and vote count of the article with the highest number of votes.

Script 2: Empire Online Top Movies List
The second script (top_movies.py) retrieves a list of top movies from the Internet Archive's snapshot of Empire Online's "100 Greatest Movies of All Time". It fetches the HTML content of the page, parses it using BeautifulSoup, and extracts the movie titles. The script then saves the list of movies in reverse order to a text file called top_movies_list.txt.
