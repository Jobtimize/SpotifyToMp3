import sys
from datetime import datetime

from names_to_links import single_term_to_yt_link
from links_to_mp3 import download_single_yt_link

from config import update_output_path

INPUT_FILE_LIST = sys.argv[1:]


def load_input_file(input_file):
    with open(input_file) as f:
        lines = f.readlines()
        lines = [str(line.strip()) for line in lines]
    print(f"Search terms: {lines}")
    return lines


def get_todays_date():
    return datetime.today().strftime('%Y-%m-%d-%H:%M:%S')


def main():
    input_file_list = INPUT_FILE_LIST
    for input_file in input_file_list:
        print(f"Using input file: {input_file}")
        search_terms = load_input_file(input_file)
        playlist_title = get_todays_date()
        update_output_path(playlist_title)
        for term in search_terms:
            yt_link = single_term_to_yt_link(term)
            download_single_yt_link(yt_link)
    print("Finished with downloading all. ")


if __name__ == '__main__':
    main()
