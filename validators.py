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

def check_files(no_match_found, folder_path):
    if no_match_found:
        print(f"[WARNING] No matching files found in '{folder_path}'.")
        return False

    return True

def check_file_exists(folder_path, filename, newname):
    destination = os.path.join(folder_path, newname)
    if os.path.exists(destination):
        print(f"[ERROR] Cannot rename {filename} → {newname}: target already exists.")
        return False

    return True

def dry_check_file_exists(folder_path, filename, newname):
    destination = os.path.join(folder_path, newname)
    if os.path.exists(destination):
        print(f"[DRY RUN][CONFLICT] Cannot rename {filename} → {newname}: target already exists.")
        return False

    return True