# Image File Renamer

A simple command-line tool to batch rename image files in a folder using a custom prefix and optional zero-padded numbering.

Useful for organizing photos, cleaning up filenames, or preparing images for publishing.

## Features

- Rename `.jpg`, `.png`, `.jpeg`, or any other extension
- Accepts multiple extensions at once
- Optional zero-padding (e.g. `001`, `002`, ...)
- Safe preview mode with `--dry-run`

## Usage

python rename_img_files.py <folder> <extension(s)> <prefix> [--zero-fill N] [--dry-run]

### Arguments

| Argument        | Description                                                            |
|-----------------|-------------------------------------------------------------------------|
| `folder`        | Path to the folder containing the image files                          |
| `extension`     | One or more file extensions to match (e.g. `.jpg .png`)                |
| `prefix`        | The prefix to use for the renamed files                                |
| `--zero-fill`   | (Optional) Number of digits for zero-padding (e.g. 3 → `001`, `002`)   |
| `--dry-run`     | (Optional) Preview changes without actually renaming files             |

## Examples

Rename only `.jpg` files:

python rename_img_files.py ./images .jpg photo_

Rename both `.jpg` and `.png` with 3-digit zero-padding:

python rename_img_files.py ./images .jpg .png img_ --zero-fill 3

Preview what would happen without making changes:

python rename_img_files.py ./images .jpeg result_ --dry-run

## Notes

- Extensions are case-insensitive
- Files that already start with the prefix will be skipped
- Both relative and absolute paths are supported

---

Made for learning and small batch file cleanup tasks.