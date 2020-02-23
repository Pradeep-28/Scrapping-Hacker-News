import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(custom_hn):
    return sorted(custom_hn, key=lambda k: k['points'], reverse=True)


def create_custom_hn(links, votes):
    custom_hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        points = int(votes[index].getText().split(' ')[0])
        if points > 2:
            custom_hn.append({'title': title, 'link': href, 'points': points})
    return sort_stories_by_votes(custom_hn)


res = requests.get('https://news.ycombinator.com/newest?next=22394136&n=271')
soup = BeautifulSoup(res.text, 'html.parser')  # For parsing html data
links = soup.select('.storylink')
votes = soup.select('.subtext')
pprint.pprint(create_custom_hn(links, votes))
