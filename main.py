import sys

from spotify_url_to_names import spotify_url_to_search_terms
from names_to_links import search_terms_to_yt_link
from links_to_mp3 import download_yt_links

from config import update_output_path, TEST_SPOTIFY_URL_LIST

SPOTIFY_URL_LIST = sys.argv[1:]


def main():
    spotify_url_list = SPOTIFY_URL_LIST
    for spotify_url in spotify_url_list:
        print(f"Starting with Spotify url: {spotify_url}")
        search_terms, playlist_title = spotify_url_to_search_terms(spotify_url)
        update_output_path(playlist_title)
        yt_links = search_terms_to_yt_link(search_terms)
        download_yt_links(yt_links)
    print("Finished with downloading all. ")


if __name__ == '__main__':
    main()
