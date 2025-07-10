import os
from validators import dry_check_file_exists
from output import dry_run_message

def dry_run(filtered_files, use_zero_fill, prefix):
    index = 1

    for filepath in filtered_files:
        filename = os.path.basename(filepath)
        extension = os.path.splitext(filename)[1].lstrip(".").lower()

        if use_zero_fill > 0:
            newname = f"{prefix}{index:0{use_zero_fill}}.{extension}"
        else:
            newname = f"{prefix}{index}.{extension}"

        newpath = os.path.join(os.path.dirname(filepath), newname)

        if not dry_check_file_exists(newpath, filename, newname):
            continue

        dry_run_message(filepath, newname)

        index += 1
