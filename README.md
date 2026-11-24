# Front page: the world news of Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/FajarRizikAinulyakin/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/FajarRizikAinulyakin/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A single 1024×1024 newspaper front page for Tuesday 24 November 2026: six stories, one image.

## The poster

`entry.png` is the whole entry — a black-and-white front page under the masthead "THE WORLD TODAY", dated Tuesday 24 November 2026. Its lead story is Ukraine sinking the Russian corvette Merkury off Libya; the five stories below it cover Jensen Huang's return to Nvidia, the Oxfam report calling Gaza a toxic wasteland, Moscow's "open war" warning to Estonia, the appeals court giving Trump a path to erase his hush-money conviction, and FIFA naming the hosts of the 2031 and 2035 Women's World Cups.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` into `/output/entry.png` and creates `/output` when it is not there. It has no arguments, no network use and no randomness: run it twice and the two outputs are byte-for-byte the same file. The sources behind each headline are recorded in `SOURCES.md` in the build notes, which is not part of this repository.

## Running it

```bash
python3 main.py
```

Afterwards the poster is at `/output/entry.png`.
