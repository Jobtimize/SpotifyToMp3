import os
import requests

from bs4 import BeautifulSoup

from config import SOUPS_DIR
from setup import check_dir


def get_page(url):
    page = requests.get(url)
    if page.status_code == 200:
        print(f"Request succeeded. Status code: {page.status_code}")
    else:
        raise ValueError(f"Request not succeeded. Status code: {page.status_code}")
    return page


def get_soup(page):
    return BeautifulSoup(page.content, 'html.parser')


def get_title(soup):
    title = soup.find_all('title')[0].contents[0]
    print(f"Spotify List Title: {title}")
    return title


def save_soup(soup, title):
    if '-' in title:
        print("'-' found in title, splitting on ' - ' and taking first part. ")
        title = title.split(' - ')[0]
        print(f"New title: {title}")
    file_name = os.path.join(SOUPS_DIR, f'{title} soup.txt')
    with open(file_name, 'w') as f:
        f.write(str(soup))
    print(f'Saved soup at: {file_name}')


def extract_info(soup):
    track_objects = soup.find_all('span', class_='track-name')
    track_names = [obj.contents[0] for obj in track_objects]
    artist_object = soup.find_all('span', class_='artists-albums')
    artist_names = [obj.contents[0].contents[0].contents[0] for obj in artist_object]
    combined = [track_names[i] + ' ' + artist_names[i] for i in range(len(artist_names))]
    return combined


def spotify_url_to_search_terms(url):
    check_dir(SOUPS_DIR)
    page = get_page(url)
    soup = get_soup(page)
    title = get_title(soup)
    try:
        save_soup(soup, title)
    except FileNotFoundError:
        print("Unable to save soup. ")
    search_terms = extract_info(soup)
    print(f'Search terms: {search_terms}')
    return search_terms, title


if __name__ == '__main__':
    pass
