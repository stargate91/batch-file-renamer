# Batch File Renamer

This is a simple Python script to batch rename image files in a folder based on various options like custom prefixes, zero-padded numbering, and random base62 identifiers.

## What it does

- Renames all files in a folder that match given extensions (like `.jpg`, `.png`).
- Adds a custom prefix to all renamed files.
- You can choose zero-padded numbering like `001`, `002` or random base62 identifiers if you want.
- Supports a dry run mode to preview changes before renaming.

## Requirements

- Python 3.x
- Standard libraries only (`argparse`, `os`, `secrets`, `string`)

## How to use

1. Open your terminal or command prompt.
2. Navigate to the folder where `main.py` is located.
3. Run the script with:

   ```bash
   python main.py /path/to/folder .jpg .png myprefix --zero-fill 3 --dry-run
   ```

   Replace `/path/to/folder` with the path to your images, `.jpg` and `.png` with your file extensions, `myprefix` with your desired prefix, and `--zero-fill` with the number of digits you want for padding. `--dry-run` lets you preview the renaming process without making any changes.

**Example:**

```bash
python main.py ./images .jpg myphoto --zero-fill 2
```

This will rename files like:
```
IMG_1234.jpg → myphoto01.jpg
```

## Arguments

| Argument       | Required | Description                                                         |
|----------------|----------|---------------------------------------------------------------------|
| `folder`       | ✅        | Path to your images folder.                                         |
| `extension`    | ✅        | One or more file extensions to match (like `.jpg`).                 |
| `prefix`       | ✅        | Prefix you want for the new file names.                             |
| `--zero-fill`  | Optional | Number of digits for zero padding. Default is `0` (no padding).     |
| `--base62`    | Optional | Use random base62 strings for file renaming instead of numbers.              |
| `--recursive`    | Optional | Include subdirectories when renaming files.              |
| `--reset-index`    | Optional |   Restart indexing from 1 for each subdirectory (only with `--recursive`).              |
| `--dry-run`    | Optional | Preview the new names without actually renaming files.              |

## Notes

- The script skips files that already start with your specified prefix.
- It will print an error if the folder does not exist, contains no matching files, or if any naming conflicts occur.
- Supports renaming files in subdirectories when `--recursive` is used.
- If `--base62` is set, it generates a random base62 string instead of using numbering or zero-padding.

## Example Output

If you run in dry run mode:
```
[DRY RUN] Would rename DSC001.jpg → holiday001.jpg
[DRY RUN] Would rename DSC002.jpg → holiday002.jpg
```

If you run it without `--dry-run`:
```
Renaming DSC001.jpg → holiday001.jpg
Renaming DSC002.jpg → holiday002.jpg
```

## Author

Written by a junior Python developer learning how to use `argparse` and work with files. 🙂

Feel free to fork it and make it better!
