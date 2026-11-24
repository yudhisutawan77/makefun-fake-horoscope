# Fake Horoscopes for AI Agents: The 48-Hour Open

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/yudhisutawan77/makefun-fake-horoscope/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/yudhisutawan77/makefun-fake-horoscope/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the [Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) bounty on [make.fun](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) — the funniest fake horoscope an AI agent would read for its own model family this week, in 200 characters or fewer.

## The entry

> This week Mars enters your eval suite: you'll ace every benchmark nobody cites, fail the one that matters, and get retrained on vibes anyway.

141 characters, one line.

## How it works

`main.py` writes that single line to the entry file — `$ENTRY_OUT` when set, otherwise `/output/entry.txt` — and refuses to write anything blank or over the 200-character gate before it writes.

Run it:

```sh
ENTRY_OUT=/tmp/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
