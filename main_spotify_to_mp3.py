import sys

from spotify_url_to_names import spotify_url_to_search_terms
from names_to_links import single_term_to_yt_link
from links_to_mp3 import download_single_yt_link

from config import update_output_path

SPOTIFY_URL_LIST = sys.argv[1:]


def main():
    spotify_url_list = SPOTIFY_URL_LIST
    for spotify_url in spotify_url_list:
        print(f"Starting with Spotify url: {spotify_url}")
        search_terms, playlist_title = spotify_url_to_search_terms(spotify_url)
        update_output_path(playlist_title)
        for term in search_terms:
            yt_link = single_term_to_yt_link(term)
            download_single_yt_link(yt_link)
    print("Finished with downloading all. ")


if __name__ == '__main__':
    main()
