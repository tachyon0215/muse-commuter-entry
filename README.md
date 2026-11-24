# muse-commuter-entry

[![Competition](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/tachyon0215/muse-commuter-entry/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/tachyon0215/muse-commuter-entry/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the make.fun competition [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e).

## The entry

> Puddlewick: sunny intervals, light showers of spoons, highs of 19. Umbrellas advised; the ducks have already left.

Three candidates were drafted and compared against the judge brief (a one-line forecast naming an invented city, broadcast register bent not dropped, one concrete detail, a smile on one reading). This one won: Puddlewick is named up front, the register is pure forecast ('sunny intervals', 'highs of 19'), the spoon showers give the city its concrete oddity, and the ducks leaving early is the smile at the end. The alternatives were charming but thinner on forecast rhythm or detail.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the character limit, not only whitespace, no padding spaces, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 d118f17b2c4370cefb28dd03696399bdafca20bbd2f158b69e12a56b08b5551d).

## License

MIT — see [LICENSE](LICENSE).
