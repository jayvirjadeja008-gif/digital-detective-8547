# Task 3.1 — Operating-system observations

| Information explored | What it tells you | Privacy-safe observation |
|---|---|---|
| Operating system / system details | Identifies the operating system family and its version/build. | macOS, privacy-safe system details: version 27.2.1, build 26B131 |
| Current account identity | Identifies the account under which Terminal commands run. | `[redacted]` |
| Available and used storage | Shows how much disk capacity is used and remains for files. | Root storage snapshot showed 460 GiB total, 13 GiB used, and 307 GiB available |
| System activity snapshot | Shows uptime and current load, plus processes that may be running. | System had been running for 36 minutes; sample load values were 1.16, 1.28 and 2.21 |

The storage numbers and load values are observations from one moment and may change continuously. Private usernames and device identifiers were excluded.

# Task 3.2 — Processes

A process is a running instance of a program or system service. The `PID` column identifies each process with a process identifier. The PID is useful for distinguishing and managing running processes.

Examples observed in the process snapshot:

1. `launchd`, PID 1, is macOS's system service manager.
2. `logd`, a background system logging service.

# Task 3.3 — Paths and permissions

The assignment folder and `terminal-practice/` subfolder produced the following privacy-safe locations:

- Assignment folder: `~/digital-detective-8547`
- Practice subfolder: `~/digital-detective-8547/terminal-practice`

An **absolute path** starts from the filesystem root, such as `/Users/[redacted]/digital-detective-8547/terminal-practice`. A **relative path** starts from the current directory, such as `terminal-practice` when already in the assignment folder.

For `terminal-practice/notes.txt`, the detailed listing began with `-rw-r--r--`. The owner permission letters were `rw-`, meaning the owner can read and write the file but cannot execute it.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows the file's contents to be read | Opening a text file |
| `w` — Write | Allows the file to be changed | Editing a text file |
| `x` — Execute | Allows a file to be run or a directory to be traversed | Running a script or entering a directory |
