import os
from validators import check_file_exists
from output import rename_success_message
from variables import generate_secure_filename
from collections import defaultdict

def filter_files(all_files, extension):
    filtered_files = []
    for filepath in all_files:
        filename = os.path.basename(filepath)

        if any(filename.lower().endswith(ext.lower()) for ext in extension):
            filtered_files.append(filepath)
    
    return filtered_files

# Pythonic approach:
# def filter_files(all_files, extension):
#     return [
#     f for f in all_files
#     if any(os.path.basename(f).lower().endswith(ext.lower()) for ext in extension)
#     ]

def rename_files(filtered_files, use_zero_fill, prefix, use_base62, use_reset_index):
    if use_base62:
        files_with_indices = [(None, filepath) for filepath in filtered_files]
    elif use_reset_index:
        files_by_folder = defaultdict(list)
        for filepath in filtered_files:
            folder = os.path.dirname(filepath)
            files_by_folder[folder].append(filepath)

        files_with_indices = []
        for folder, files in files_by_folder.items():
            for i, filepath in enumerate(files, start=1):
                files_with_indices.append((i, filepath))
    else:
        files_with_indices = [(i, filepath) for i, filepath in enumerate(filtered_files, start=1)]

    for index, filepath in files_with_indices:
        folder = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        extension = os.path.splitext(filename)[1].lstrip(".").lower()

        if use_base62:
            secure = generate_secure_filename()
            newname = f"{prefix}{secure}.{extension}"
        elif use_zero_fill > 0:
            newname = f"{prefix}{index:0{use_zero_fill}}.{extension}"
        else:
            newname = f"{prefix}{index}.{extension}"

        newpath = os.path.join(folder, newname)

        if not check_file_exists(newpath, filepath, newname):
            continue

        os.rename(filepath, newpath)
        rename_success_message(filepath, newname)
