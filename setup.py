import os

from config import SOUPS_DIR, OUTPUT_DIR


def check_dir(dir):
    if os.path.isdir(dir):
        pass
    else:
        os.mkdir(dir)
        print(f"Directory didn't exist, created at: {dir}")

check_dir(SOUPS_DIR)
check_dir(OUTPUT_DIR)
