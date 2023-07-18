# Importing the required libraries
from bs4 import BeautifulSoup
import requests

# Sending a GET request to the Hacker News website
response = requests.get("https://news.ycombinator.com/")
webpage = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Selecting all the anchor tags within the "titleline" class
all_anchor = soup.select(".titleline a")

# Selecting all the elements with the "score" class
up_vote = soup.select(".score")

# Initializing empty lists to store the extracted data
text = []
link = []
votes = []

# Iterating over the anchor tags to extract the text and link
# We also keep track of the iteration count using the variable "i"
# If i is even, we append the tag's text and link to the respective lists
# If i is odd, we simply increment the count
i = 0
for tag in all_anchor:
    if i % 2 == 0:
        text.append(tag.getText())
        link.append(tag.get("href"))
        i += 1
    else:
        i += 1

# Extracting the vote count from each element in the "up_vote" list
# We split the text to remove any additional information and convert it to an integer
for vote in up_vote:
    votes.append(int(vote.getText().split()[0]))

# Printing the title, link, and maximum vote count
# We use the index of the maximum vote count to retrieve the corresponding title and link
print(text[votes.index(max(votes))])
print(link[votes.index(max(votes))])
print(max(votes))
