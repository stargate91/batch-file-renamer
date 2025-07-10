import os
from cli import parse_args

def def_variables():
    args = parse_args()

    use_dry_run = args.dry_run
    folder_path = args.folder
    extension = args.extension
    prefix = args.prefix
    use_zero_fill = args.zero_fill
    files = os.listdir(folder_path)
    
    return use_dry_run, folder_path, extension, prefix, use_zero_fill, files
