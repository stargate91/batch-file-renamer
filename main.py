import os
from variables import def_variables, get_files
from validators import check_folder, check_prefix, check_files
from operations import rename_files, filter_files
from dry import dry_run

def main():
    use_dry_run, folder_path, extension, prefix, use_zero_fill, use_recursive = def_variables()

    if not check_folder(folder_path):
        return

    if not check_prefix(prefix):
        return
    
    all_files = get_files(folder_path, use_recursive)
    filtered_files = filter_files(all_files, extension)

    if not check_files(filtered_files, folder_path):
        return

    if use_dry_run:
        dry_run(filtered_files, use_zero_fill, prefix)
    else:
        rename_files(filtered_files, use_zero_fill, prefix)

if __name__ == "__main__":
    main()