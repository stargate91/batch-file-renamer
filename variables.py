import os
import secrets
import string
from cli import parse_args

def def_variables():
    args = parse_args()

    folder_path = args.folder
    extension = args.extension
    prefix = args.prefix
    use_zero_fill = args.zero_fill
    use_base62 = args.base62
    use_recursive = args.recursive
    use_reset_index = args.reset_index
    use_dry_run = args.dry_run
    
    return folder_path, extension, prefix, use_zero_fill, use_base62, use_recursive, use_reset_index, use_dry_run

def get_files(folder_path, use_recursive=False):
    if use_recursive:
        all_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in sorted(files, key=str.lower):
                all_files.append(os.path.join(root, file))
        return all_files
    else:
        all_files = sorted(os.listdir(folder_path), key=str.lower)
        return [os.path.join(folder_path, f) for f in all_files]

def generate_secure_filename():
    length = 24
    chars = string.ascii_letters + string.digits
    random_part = ''.join(secrets.choice(chars) for i in range(length))
    return random_part