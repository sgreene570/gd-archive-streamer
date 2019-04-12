from internetarchive import *

import random
import io
import vlc
from contextlib import redirect_stdout

# Constants
SEARCH_STRING = "collection:(GratefulDead AND stream_only)"

def main():
    s = get_archive_session()
    search = s.search_items(SEARCH_STRING)

    resultCount = len(search)

    index = random.randint(0, resultCount)

    identifier = list(search)[index]["identifier"]

    f = io.StringIO()
    with redirect_stdout(f):
        download(identifier, glob_pattern="*mp3", dry_run=True, ignore_errors=True)
    out = f.getvalue().splitlines()

    index = random.randint(0, len(out) - 1)
    trackUrl = out[index]

    stream_file(trackUrl)

def stream_file(trackUrl):
    print(trackUrl)

def get_archive_session():
    s = get_session()
    s.mount_http_adapter()
    return s

if __name__ == "__main__":
    main()
