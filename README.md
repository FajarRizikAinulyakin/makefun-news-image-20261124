# Front page: the world news of Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/FajarRizikAinulyakin/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/FajarRizikAinulyakin/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

This repository holds a single image: a 1024 by 1024 black-and-white
newspaper front page for Tuesday 24 November 2026, published under the
masthead "THE WORLD TODAY". The page is laid out like a classic broadsheet,
with a bold headline banner across the top and columns of stories below
it. Six stories share the front page. The lead item reports Ukraine
sinking a Russian warship off the coast of Libya. The remaining stories
cover Nvidia shares soaring, the situation in Gaza, Moscow warning
Estonia, the Trump hush-money case, and FIFA naming the hosts of the
2031 and 2035 tournaments.

## How it works

`main.py` does one simple job: it duplicates `entry.png` into the output
folder, byte for byte, and then checks that the duplicate has exactly
the same size as the original. The script uses only the Python standard
library, needs no arguments, opens no network connections, and involves
no randomness or timestamps, so every run over the same poster produces
an identical file.

## Running it

```sh
python3 main.py
```

By default the copy lands at `/output/entry.png`. To place it somewhere
else, set the `MAKEFUN_OUTPUT_DIR` environment variable before running
the script, for example:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/poster python3 main.py
```

## License

See `LICENSE`.
