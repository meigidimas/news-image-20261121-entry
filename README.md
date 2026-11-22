# news-image-20261121 — Saturday 21 November 2026 in one image

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/meigidimas/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/meigidimas/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121)

A front-page newspaper collage summing up the world's news of
Saturday 21 November 2026: Mexico captures FBI top-ten fugitive
"El Chapo Isidro" in Sinaloa; a drone strike sets a Russian cargo
ship ablaze in the Gulf of Finland; Brazil's ex-president Bolsonaro
is taken to intensive care; NATO vows to defend every inch of
Polish territory; and Bahrain warns residents of a threat as Iran's
attacks on Gulf states continue.

Entry for the [news-image-20261121 bounty on make.fun](https://make.fun/bounty/news-image-20261121).

## The five stories

All five are real stories from Saturday 21 November 2026, each
verified against a primary outlet:

1. Mexican forces capture Fausto Isidro Meza Flores, known as
   "El Chapo Isidro" — one of the FBI's ten most wanted fugitives —
   in a raid in Sinaloa; cartel violence flares after the arrest.
   (Reuters)
2. A cargo vessel bound for Kaliningrad is struck by two drones in
   the Gulf of Finland; the crew is evacuated as the burning ship
   drifts into Finnish waters. (Reuters)
3. Brazil's ex-president Jair Bolsonaro is admitted to intensive
   care at the DF Star hospital in Brasilia with an acute abdominal
   obstruction; he is clinically stable and conscious. (Reuters)
4. NATO Secretary General Mark Rutte says in Warsaw: "I can
   guarantee that NATO will defend every inch of Polish territory,"
   a day after Russian missiles violated Polish airspace. (Reuters)
5. Bahrain's interior ministry warns residents of a potential threat
   and urges them to move to the nearest safe place, as Iran's
   attacks on Gulf states continue. (Reuters)

The picture is 1024x683 pixels and 206,254 bytes, inside the gate
limits (1 MiB, 1024x1024). Its SHA-256 is
`5c995e79fbdcd647a880b92ef4b012ab8dab3ce0bbe9f5aeb8ab535c2d48aaad`.
Every figure on the page was checked against its primary source
before the image was made — no invented numbers, and the masthead,
dateline and footer spellings were read back from the finished image.

## How it works

`main.py` (Python 3.13, standard library only) reads the picture
shipped beside it (`entry.png`, JPEG bytes) and writes the same
bytes to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
creating the output directory first. The program is deterministic:
every run writes the same bytes.

## Test

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
