from internetarchive import *

import random

# Constants
SEARCH_STRING = "Grateful Dead"

def main():
    s = get_archive_session()
    search = s.search_items(SEARCH_STRING)

    resultCount = len(search)

    index = random.randint(0, resultCount)

    identifier = list(search)[index]["identifier"]
    print(identifier)
    download(identifier)


def get_archive_session():
    s = get_session()
    s.mount_http_adapter()
    return s

if __name__ == "__main__":
    main()
