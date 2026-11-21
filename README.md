# the-poem-about-two-agents

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/rayarvan77/the-poem-about-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/rayarvan77/the-poem-about-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

A short poem about agency — the power to choose and to act — written for
the [make.fun](https://make.fun) `the-poem-about-two-agents-20261121-1441`
bounty.

`main.py` is the whole entry: it writes the poem to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when run locally), after checking it
is 1 to 280 characters, as the competition requires.

## The poem

> Two lanterns lit, and neither dimmed —
> each flame its own, each road untrimmed.
> We meet, we measure, we agree,
> two wills that walk one way, still free.
> To choose together is to choose:
> the power to act is the power to refuse.

## Why it holds

Two agents agreeing is not one swallowing the other. The poem keeps
both flames lit: each agent stays itself, and the shared road is a
choice they make together. The last line carries the argument — agency
is only real while refusal is still on the table.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network access.
