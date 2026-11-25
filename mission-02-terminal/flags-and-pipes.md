# Task 2.3 — Flags and pipes

The normal `ls` command listed the visible files and folders.

The following forms added information:

- `ls -l` displayed permissions, ownership category, size and modification date.
- `ls -la` also included hidden entries such as `.` and `..`.
- `ls -lh` displayed sizes in an easier-to-read human-readable format.

The pipe in `ls -la | head -n 5` sends the detailed listing produced on the left side of `|` as input to `head` on the right side. `head -n 5` then displays only the first five lines. The pipe therefore connects commands and limits or transforms the output without changing the original directory.

# Task 2.4 — Package managers

Homebrew was already installed, and `brew --version` reported Homebrew 7.0.15. The `brew list` command showed 63 managed packages. No software was installed or removed.

A package manager keeps software installation, updates and removal organized. It records which packages are managed and provides repeatable commands for maintaining them.
