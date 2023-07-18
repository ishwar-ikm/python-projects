from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

all_anchor = soup.select(".titleline a")
up_vote = soup.select(".score")

text = []
link = []
votes = []
i = 0
for tag in all_anchor:
    if i%2 == 0:
        text.append(tag.getText())
        link.append(tag.get("href"))
        i += 1
    else:
        i += 1

for vote in up_vote:
    votes.append(int(vote.getText().split()[0]))


print(text[votes.index(max(votes))])
print(link[votes.index(max(votes))])
print(max(votes))