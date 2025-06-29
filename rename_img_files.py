import argparse
import sys
import os

parser = argparse.ArgumentParser(description="Batch rename image files in a folder with a custom prefix and optional zero-padded numbering.")
parser.add_argument("folder", help="Path to the folder containing the image files.")
parser.add_argument("extension", nargs="+", help="One or more file extensions to match (e.g. .jpg .png).")
parser.add_argument("prefix", help="Prefix for the renamed files.")
parser.add_argument("--zero-fill", type=int, default=0, help="Number of digits for zero-padding (e.g. 3 → 001, 002). Default: no padding.")
parser.add_argument("--dry-run", action="store_true", help="Preview changes without actually renaming files.")

args = parser.parse_args()

use_dry_run = args.dry_run

folder_path = args.folder

if not os.path.exists(folder_path):
    print(f"[ERROR] Folder '{folder_path}' does not exist.")
    sys.exit(1)

if not os.path.isdir(folder_path):
    print(f"[ERROR] '{folder_path}' is not a directory.")
    sys.exit(1)

image_extension = args.extension

prefix = args.prefix
if len(prefix.strip()) == 0:
    print("[ERROR] Prefix cannot be empty.")
    sys.exit(1)

use_zero_fill = args.zero_fill

files = os.listdir(folder_path)

has_files = any(
    fname.lower().endswith(tuple(ext.lower() for ext in image_extension)) 
    for fname in files
)
if not has_files:
    print(f"[WARNING] No matching files found in '{folder_path}'.")
    sys.exit(1)

target_files = [
    f for f in files
    if any(f.lower().endswith(ext.lower()) for ext in image_extension)
    and not f.startswith(prefix)
]

for index, filename in enumerate(target_files, start=1):
    matched_ext = next(
        (ext for ext in image_extension if filename.lower().endswith(ext.lower())),
        None
    )
    if matched_ext:
        clean_ext = matched_ext.lstrip(".")
        if use_zero_fill > 0:
            newname = f"{prefix}{index:0{use_zero_fill}}.{clean_ext}"
        else:
            newname = f"{prefix}{index}.{clean_ext}"
        if use_dry_run == True:
        	print(f"[DRY RUN] Would rename {filename} → {newname}")
        else:	
        	os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, newname))
        	print(f"Renaming {filename} → {newname}")