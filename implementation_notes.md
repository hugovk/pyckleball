# Implementation Notes

`uv init` creates all of the following immediately:

1. git folder
2. .gitignore
3. .python-version
4. main.py
5. pyproject.toml
6. README.md

I then did:

`uv add pytest`
`uv add playwright`

I had trouble getting playwright to work, so I started the virtual environment with
`source .venv/bin/activate`
and then ran
`playwright install` and that seemed to work

## Pycon

- Huge and at times, disorienting, but fun. Data scientists, software devs, hackers/hobbyists, finance.
- Topics
  - Lots of people were talking about the updates about removing the GIL, but I wasn't tracking that.
  - Marimo is a fast-growing alternative to jupyter notebooks.
  - UV has become a standard very quickly.
- Vim and making editing fun/fast???
- Open source and the sprint days.

understand the difference between I/O problems and CPU processing (where parallel processing).

thomas builds things in python and then if it's not fast enough, at least it helps you figure out the edge cases. if you want fast, then you can rebuild in rust.

async should be faster than multi-threaded processing. but it doesn't have the same overhead as parallel processing.


## Update on TSPi work

- SAFe is starting to make sense.
  - Roles are super clear, no one can hide.
  - Works well for enormous projects if institutional knowledge is lost.
  - Development process does feel pretty organic, information flows in both directions.
  - Tickets are actually actionable by the time the devs start working on them - they really can be done!
  - TBD about whether or not testers will really have the information that they need to do proper testing.
  - I see no way that I can be doing any coding.

## Project Questions

1. Multiple windows?
2. PYTHONPATH - referring to subdirector from sister directory.
3. how can I make my sessions more modular? Can you explain the logic behind submitter_session function and yielding?
