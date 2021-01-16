This is a simple package that is able to download Spotify playlists via YouTube as MP3 files.

First, it scrapes the track and artist names from Spotify.
Thereafter, it gathers the YouTube links from youtube.
Finally, it uses these links to download the corresponding MP3 files.

----

Install requirements.txt:
pip install -r requirements.txt

Run setup.py:
python setup.py
or
python3 setup.py

Make sure to have Google Chrome installed.
Download chromedriver.exe (selenium) and place in the main directory. Please pay attention to your Chrome version.
https://chromedriver.chromium.org/downloads

Now you are ready to download music.

Run main.py from command line, with spotify URL playlists as arguments (can be multiple).
Each spotify playlist will be downloaded and placed in a separate folder.

Windows example:
open cmd
cd 'this_directory'
python main.py SPOTIFY_URL

config.py holds some settings you can adjust, if you wish.
