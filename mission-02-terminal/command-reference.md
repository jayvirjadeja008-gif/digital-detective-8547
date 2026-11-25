# Mission 2 — Terminal command reference

| Operation / command name | What it does | What I observed |
|---|---|---|
| Current-directory display: `pwd` | Displays the full path of the current working directory. | The working location was shown; a privacy-safe shortened form was used in notes. |
| Directory listing: `ls` | Lists visible files and folders in the current location. | The practice folder showed `notes.txt` and `notes-copy.txt`. |
| Detailed listing: `ls -l` | Shows a detailed listing with permissions, owner information, size and modification details. | Both practice files appeared with their sizes and permission patterns. |
| Change directory: `cd` | Moves from one directory to another. | Moving to `..` changed the location to the parent folder; moving back returned to the assignment repository. |
| Create directory: `mkdir` | Creates a new directory. | `terminal-practice/` was created inside the assignment repository. |
| Create empty file: `touch` | Creates an empty file or updates its timestamp. | The practice file was available for subsequent text operations. |
| Copy file: `cp` | Creates a copy of a file, normally without moving the original. | `notes.txt` was copied before the backup was renamed. |
| Move or rename file: `mv` | Moves a file or changes its name. | The copied backup was renamed from `notes-backup.txt` to `notes-copy.txt`. |
| Display file contents: `cat` | Prints a file's contents to the Terminal. | Both lines of the original practice file were visible. |

## File-change answers

- **Replacing versus adding text:** Replacing overwrites existing contents. Adding text with `>>` appends a new line after the existing text, preserving the first line.
- **Copying versus moving:** Copying creates a second file and leaves the original in place. Moving changes the file's location or name and does not leave a duplicate at the old location.
- **Current-directory display:** `pwd` provides the current working location, helping commands target the correct directory.
- **Directory listing:** `ls` helps check which files and folders exist and confirms whether file operations worked.
