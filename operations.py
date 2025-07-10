import os
from validators import check_file_exists
from output import rename_success_message 

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


def rename_files(filtered_files, use_zero_fill, prefix):
    index = 1
    for filepath in filtered_files:
        filename = os.path.basename(filepath)
        extension = os.path.splitext(filename)[1].lstrip(".").lower()

        if use_zero_fill > 0:
            newname = f"{prefix}{index:0{use_zero_fill}}.{extension}"
        else:
            newname = f"{prefix}{index}.{extension}"

        newpath = os.path.join(os.path.dirname(filepath), newname)

        if not check_file_exists(newpath, filename, newname):
            continue

        os.rename(filepath, newpath)
        rename_success_message(filepath, newname)
        index += 1
