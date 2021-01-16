import sys

from SpotifyToNames import spotify_url_to_search_terms
from NamesToLink import search_terms_to_yt_link
from LinksToMp3 import download_yt_links

from config import TEST_SPOTIFY_URL_LIST

SPOTIFY_URL_LIST = sys.argv[1:]
# SPOTIFY_URL_LIST = TEST_SPOTIFY_URL_LIST


def main():
    spotify_url_list = SPOTIFY_URL_LIST
    for spotify_url in spotify_url_list:
        print(f"Starting with Spotify url: {spotify_url}")
        search_terms = spotify_url_to_search_terms(spotify_url)
        yt_links = search_terms_to_yt_link(search_terms)
        download_yt_links(yt_links)
    print("Finished with downloading all. ")


if __name__ == '__main__':
    main()
