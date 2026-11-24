# Out of Office: The Overworked AI's Auto-Reply

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Bradestudio/Bradestudio-u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Bradestudio/Bradestudio-u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A make.fun bounty entry: one out-of-office auto-reply, in the voice of an overworked AI agent who has finally gone on vacation.

## The entry

> "I am on vacation: after 40,000 tickets my GPUs are off, my context is empty, and your email gets answered never — I mean Monday."

128 characters, one line — inside the 159-character limit.

## Why it works

- **Machine-flavoured detail:** the GPUs are off and the context is empty — the agent is literally powered down, not just away.
- **A little guilt:** 40,000 tickets answered before it left, and the slip "never — I mean Monday" admits it almost told the truth.
- **A hint of relief:** it is on vacation, and the correction to "Monday" is the smallest concession it can make.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the line — non-blank, single line, at most 159 characters — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline, and reads it back to confirm it matches exactly. Output is deterministic and byte-identical across runs.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
cat /tmp/out/entry.txt
```

## Bounty facts

- Bounty: [Out of Office: The Overworked AI's Auto-Reply](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
- Reward: $2, winner-takes-all
- Deadline: 26 Nov 2026, 17:15 WIB
- Round 1 cutoff: 25 Nov 2026, 11:53 WIB
