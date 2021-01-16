import os

SOUPS_DIR = 'soups'
BASE_URL = 'https://www.youtube.com/results?search_query='
OUTPUT_DIR = '../Music/'
SINGLE_MP3_FILE_NAME = '/%(title)s.%(ext)s'

YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': OUTPUT_DIR + SINGLE_MP3_FILE_NAME
}

TEST_SPOTIFY_URL = 'https://open.spotify.com/playlist/07zoQjzRszj3ki9A09omiM'
TEST_SPOTIFY_URL_LIST = ['https://open.spotify.com/playlist/07zoQjzRszj3ki9A09omiM']
TEST_SEARCH_TERMS = ['Roller Coaster Danny Vera', 'Hotel California - 2013 Remaster Eagles']
INPUT_FILE = '../input_file.txt'


def update_output_path(playlist_title: str):
    new_path = os.path.join(OUTPUT_DIR, playlist_title) + SINGLE_MP3_FILE_NAME
    YDL_OPTS['outtmpl'] = new_path
