# I choose you!

This is a toy script that I wrote for a one-day hackathon at
[boot.dev](https://boot.dev/). (I'm in the "senior" category.) The assignment
was to write something in Python, and to make use of
[PokéAPI](https://pokeapi.co/).

I had very little free time on the day in question, so I did something as simple
as possible. This script will pull data for a random Pokémon from PokéAPI;
display its image on the command line (using the
[CLImage](https://github.com/pnappa/CLImage) library); and list its stats and
abilities. That's it!

You should probably be using a modern terminal emulator in order for this to
work properly, as I've enabled the Unicode and
[true color](https://en.wikipedia.org/wiki/Color_depth#True_color_%2824-bit%29)
options in CLImage. (Without those settings, the image quality is just awful.)

## Usage

Install dependencies:

```sh
pip3 install -r requirements.txt
```

Run script:

```sh
python3 choose.py
```
