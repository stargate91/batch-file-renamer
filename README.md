
# Batch Image Renamer

This is a simple Python script to batch rename image files in a folder.

## What it does

- Renames all files in a folder that match given extensions (like `.jpg`, `.png`).
- Adds a custom prefix to all renamed files.
- You can choose zero-padded numbering like `001`, `002` if you want.
- Supports a dry run mode to preview changes before renaming.

## Requirements

- Python 3.x
- Standard libraries only (`argparse`, `os`, `sys`)

## How to use

1. Open your terminal or command prompt.
2. Navigate to the folder where `rename_images.py` is located.
3. Run the script with:

   ```bash
   python rename_images.py /path/to/folder .jpg .png myprefix --zero-fill 3 --dry-run
   ```

   Replace `/path/to/folder` with the path to your images, `.jpg` and `.png` with your file extensions, `myprefix` with your desired prefix, and `--zero-fill` with the number of digits you want for padding.

**Example:**

```bash
python rename_images.py ./images .jpg myphoto --zero-fill 2
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
| `--dry-run`    | Optional | Preview the new names without actually renaming files.              |

## Notes

- The script will skip files that already start with your prefix.
- It prints an error if the folder does not exist or has no matching files.
- It works only for files in the given folder (no subfolders).

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