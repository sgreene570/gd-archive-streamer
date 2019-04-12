import random
import io
import os
from contextlib import redirect_stdout
from internetarchive import *

# Constants
SEARCH_STRING = "collection:(GratefulDead AND stream_only)"

def main():
    s = get_archive_session()
    # Search archive.org
    search = s.search_items(SEARCH_STRING)

    resultCount = len(search)

    # Create random show index
    index = random.randint(0, resultCount)

    # Find random show
    # TODO optimize iterator index
    identifier = list(search)[index]["identifier"]

    # Redirect the output of the "dry_run" download function
    f = io.StringIO()
    with redirect_stdout(f):
        download(identifier, glob_pattern="*mp3", dry_run=True, ignore_errors=True)
    out = f.getvalue().splitlines()

    # Pick random track from show
    index = random.randint(0, len(out) - 1)
    trackUrl = out[index]

    # Play track
    play_file(trackUrl)

def play_file(trackUrl):
    # For now, use ffplay in terminal
    os.system("ffplay" + " " + trackUrl)

def get_archive_session():
    s = get_session()
    s.mount_http_adapter()
    return s

if __name__ == "__main__":
    main()
