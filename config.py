SOUPS_DIR = 'soups'
BASE_URL = 'https://www.youtube.com/results?search_query='
OUTPUT_DIR = '../Music/'

YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': OUTPUT_DIR + '/%(title)s.%(ext)s'
}

TEST_SPOTIFY_URL = 'https://open.spotify.com/playlist/07zoQjzRszj3ki9A09omiM'
TEST_SPOTIFY_URL_LIST = ['https://open.spotify.com/playlist/07zoQjzRszj3ki9A09omiM']
TEST_SEARCH_TERMS = ['Roller Coaster Danny Vera', 'Hotel California - 2013 Remaster Eagles']
INPUT_FILE = '../input_file.txt'
