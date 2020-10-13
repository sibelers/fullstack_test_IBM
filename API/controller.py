from bs4 import BeautifulSoup
import requests


def link_map(url):
    # Getting the html content of the url
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    # Mapping the "a" tags
    tags_parse = soup.find_all('a')

    # Using href property
    tag_list = {'links': []}
    for tag in tags_parse:
        tag_list['links'].append(tag['href'])

    return tag_list
