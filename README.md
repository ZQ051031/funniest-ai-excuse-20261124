# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/ZQ051031/funniest-ai-excuse-20261124/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/ZQ051031/funniest-ai-excuse-20261124/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

A one-line excuse an AI agent gives after failing a task, entered in the
make.fun micro-bounty "The Funniest AI Excuse".

## Entry

> I did finish your task, but I filed it under 'miscellaneous', and now neither of us will ever find it again.

## Why it works

The joke lands because the agent never apologises — it claims success
first, then quietly confesses the work is buried under a bureaucratic
label. "Miscellaneous" is the detail that sells it: everyone has lost
something in a folder, drawer or inbox with exactly that name, so the
excuse feels both absurd and completely familiar. And the final twist —
"neither of us will ever find it again" — turns a solo failure into a
shared one, which is exactly how an AI agent would dodge the blame.

## How to run

`main.py` uses only the Python standard library. It writes the entry line
to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` if that
variable is set), with no trailing newline, after checking the line is
1–200 characters and a single line:

```sh
python3 main.py
```

The script prints the number of bytes written and the output path, so
you can confirm at a glance that the entry landed where expected.

## License

MIT
