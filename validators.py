import os

def check_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder '{folder_path}' does not exist.")
        return False

    if not os.path.isdir(folder_path):
        print(f"[ERROR] '{folder_path}' is not a directory.")
        return False

    return True

def check_prefix(prefix):
    if len(prefix.strip()) == 0:
        print("[ERROR] Prefix cannot be empty.")
        return False

    return True

def check_files(filtered_files, folder_path):
    if not filtered_files:
        print(f"[WARNING] No matching files found in '{folder_path}'.")
        return False

    return True


def check_file_exists(destination, filepath, newname):
    if os.path.exists(destination):
        relpath = os.path.relpath(filepath)
        print(f"[ERROR] Cannot rename {relpath} → {newname}: target already exists.")
        return False

    return True


def dry_check_file_exists(destination, filepath, newname):
    if os.path.exists(destination):
        relpath = os.path.relpath(filepath)
        print(f"[DRY RUN][CONFLICT] Cannot rename {relpath} → {newname}: target already exists.")
        return False

    return True