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


def update_output_path(playlist_title: str):
    new_path = os.path.join(OUTPUT_DIR, playlist_title) + SINGLE_MP3_FILE_NAME
    YDL_OPTS['outtmpl'] = new_path
