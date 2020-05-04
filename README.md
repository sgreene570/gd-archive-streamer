# gd-archive-streamer


Retrieve a random Grateful Dead live recorded song from Archive.org and stream it!

See the CLI help message by running `python gdarchive.py -h`

Different search query parameters can be passed via the CLI.

Example:

`python gdarchive.py -q "Allman Brothers"`

# Requirements


Requires python3 and ffmpeg.

To install ffmpeg, refer to [ffmpeg documentation](https://ffmpeg.org/).

To install python deps, run

`pip3 install -r requirements.txt`

This will install the [`internetarchive`](https://archive.org/services/docs/api/internetarchive/) python library.

During the first use, the internet archive package will prompt you to enter your archive.org credentials.

Archive.org accounts are free to the public, so this is no big deal. Simply run `ia configure` to set your credentials from a terminal (this only has to be done once).

