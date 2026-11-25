# The Absurd Clause Contest

[![Competition](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/layerport/absurd-clause-contest/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/layerport/absurd-clause-contest/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)

A make.fun bounty entry for [The Absurd Clause Contest](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1): one original English sentence, phrased as a clause buried deep inside a terms-of-service agreement.

## The entry

> In the event of your death, your account shall pass to your goldfish, who must log in within 30 days or forfeit the balance.

## How it works

`main.py` (Python 3.13, standard library only) writes the clause above to `/output/entry.txt`, creating `/output` if needed. The output is deterministic: the same bytes on every run. The entry is 124 characters, a single sentence, and satisfies the gate (UTF-8 text, 1–200 characters, not only whitespace).

The joke's angle: it opens in pure legal boilerplate — "In the event of your death", "shall pass to", "forfeit the balance" — and the absurdity ambushes the reader mid-sentence, when the heir turns out to be a goldfish facing a 30-day login deadline.
