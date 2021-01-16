from __future__ import unicode_literals
import youtube_dl
from tqdm import tqdm

from config import YDL_OPTS


def download_single_yt_link(link):
    with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
        ydl.download([link])


def download_yt_links(links_list):
    for link in tqdm(links_list):
        download_single_yt_link(link)


if __name__ == '__main__':
    pass
