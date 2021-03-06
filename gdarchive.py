import random
import io
import os
import argparse
from contextlib import redirect_stdout
from internetarchive import *

def main():
    # Argparse code
    parser = argparse.ArgumentParser(description="Archive.org streamer commands")
    parser.add_argument("-q", "--query", required=False, type=str, help="Archive search query string")
    parser.add_argument("-s", "--silent", action="store_true", help="Disable audio stream playback")
    parser.add_argument("-v", "--verbose", action="store_true", help="Display track URL info")
    parser.add_argument("-r", "--repeat", action="store_true", help="Play a new track after prior track finishes")
    args = parser.parse_args()

    # Set default search string
    search_string = "collection:(GratefulDead AND stream_only)"

    if args.query is not None:
        # Modify search_string if passed via args
        search_string = args.query

    if args.verbose:
        print(search_string)

    # Runtime code
    s = get_archive_session()
    url = find_file(s, search_string)

    if args.verbose:
        print(url)

    # If silent mode is not enabled, stream the track
    if not args.silent:
        play_file(url, args.repeat)

def find_file(session, search_string):
    # Search archive.org
    search = session.search_items(search_string)

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

    return trackUrl

def play_file(trackUrl, repeat):
    # For now, use ffplay in terminal
    try:
        os.system("ffplay -autoexit" + " " + trackUrl + " > /dev/null 2>&1")
    except OSError:
        print("Error using ffplay, is ffmpeg installed?")
        return
    # Run program again if repeat flag enabled
    if repeat:
        main()

def get_archive_session():
    s = get_session()
    s.mount_http_adapter()
    return s

if __name__ == "__main__":
    main()
