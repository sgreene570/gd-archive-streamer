from internetarchive import *

import random

# Constants
SEARCH_STRING = "collection:(GratefulDead AND stream_only)"

def main():
    s = get_archive_session()
    search = s.search_items(SEARCH_STRING)

    resultCount = len(search)

    index = random.randint(0, resultCount)

    identifier = list(search)[index]["identifier"]
    download(identifier, glob_pattern="*mp3", dry_run=True, ignore_errors=True)

def get_archive_session():
    s = get_session()
    s.mount_http_adapter()
    return s

if __name__ == "__main__":
    main()
