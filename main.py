import os
from variables import def_variables
from validators import check_folder, check_prefix
from operations import rename_files, dry_rename_files

def main():
    use_dry_run, folder_path, extension, prefix, use_zero_fill, files = def_variables()

    if not check_folder(folder_path):
        return

    if not check_prefix(prefix):
        return

    if use_dry_run:
        dry_rename_files(files, extension, use_zero_fill, prefix, folder_path)
    else:
        rename_files(files, extension, use_zero_fill, prefix, folder_path)

if __name__ == "__main__":
    main()