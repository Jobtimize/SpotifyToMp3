from __future__ import unicode_literals
import youtube_dl
from tqdm import tqdm

from config import INPUT_FILE, YDL_OPTS


def load_links():
    with open(INPUT_FILE, 'r') as file:
        links_list = file.readlines()
    return links_list


def download_yt_links(links_list):
    for link in tqdm(links_list):
        with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
            ydl.download([link])


def main():
    links = load_links()
    download_yt_links(links)


if __name__ == '__main__':
    main()
