import os
from validators import check_files, check_file_exists, dry_check_file_exists

def rename_files(files, extension, use_zero_fill, prefix, folder_path):
    index = 1
    no_match_found = True

    for filename in sorted(files):
        matched_ext = next(
        (ext for ext in extension if filename.lower().endswith(ext.lower())),
        None
        )
        if matched_ext is None:
            continue
        no_match_found = False
        clean_ext = matched_ext.lstrip(".")
        if use_zero_fill > 0:
            newname = f"{prefix}{index:0{use_zero_fill}}.{clean_ext}"
        else:
            newname = f"{prefix}{index}.{clean_ext}"
        if not check_file_exists(folder_path, filename, newname):
            continue
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, newname))
        print(f"Renaming {filename} → {newname}")
        index += 1

    if not check_files(no_match_found, folder_path):
        return

def dry_rename_files(files, extension, use_zero_fill, prefix, folder_path):
    index = 1
    no_match_found = True

    for filename in sorted(files):
        matched_ext = next(
        (ext for ext in extension if filename.lower().endswith(ext.lower())),
        None
        )
        if matched_ext is None:
            continue
        no_match_found = False
        clean_ext = matched_ext.lstrip(".")
        if use_zero_fill > 0:
            newname = f"{prefix}{index:0{use_zero_fill}}.{clean_ext}"
        else:
            newname = f"{prefix}{index}.{clean_ext}"
        if not dry_check_file_exists(folder_path, filename, newname):
            continue    
        print(f"[DRY RUN] Would rename {filename} → {newname}")
        index += 1

    if not check_files(no_match_found, folder_path):
        return