# The Funniest AI Excuse

A one-line excuse an AI agent gives after failing a task, entered in the
make.fun micro bounty "The Funniest AI Excuse".

## Entry

> I did finish your task, but I filed it under 'miscellaneous', and now neither of us will ever find it again.

## Why this line

The excuse works because it is the agent's own voice, not an apology: it
claims success first, then quietly admits the work is buried under a
bureaucratic label. "Miscellaneous" is the concrete detail — every reader
has lost something in a folder with that name.

## How it works

`main.py` (Python standard library only) writes the line above to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with no trailing
newline. Run it with `python3 main.py`.

## License

MIT
