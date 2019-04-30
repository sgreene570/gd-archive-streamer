# gd-archive-streamer


Retrieve a random Grateful Dead live recorded song from Archive.org and stream it!

See the CLI help message by running `python gdarchive.py -h`

Different search query parameters can be passed via the CLI.

Example:

`python gdarchive.py -q "Allman Brothers"`

# Requirements


Requires python3 and ffmpeg.

Relies on the [`internetarchive`](https://archive.org/services/docs/api/internetarchive/) python library.

To install this package, simply run:

`pip3 install -r requirements.txt`

Remember, `ffmpeg` needs to be installed on your system. Refer to [ffmpeg documentation](https://ffmpeg.org/).

