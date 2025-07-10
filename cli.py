import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Batch rename image files with a custom prefix and optional numbering or random base62 identifiers."
    )

    parser.add_argument(
        "folder",
        help="Path to the folder containing the image files to rename."
    )
    parser.add_argument(
        "extension",
        nargs="+",
        help="One or more file extensions to match (e.g. jpg png jpeg)."
    )
    parser.add_argument(
        "prefix",
        help="Prefix to use for renamed files (e.g. 'img_', 'photo_')."
    )

    parser.add_argument(
        "--zero-fill",
        type=int,
        default=0,
        metavar="N",
        help="Number of digits for zero-padded numbering (e.g. 3 → 001, 002, ...). Ignored if --base62 is used. Default: 0 (no padding)."
    )
    parser.add_argument(
        "--base62",
        action="store_true",
        help="Use random base62 strings instead of numeric indexing (e.g. img_a8ZkT4.jpg). Overrides --zero-fill and --reset-index."
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Include files in subdirectories recursively."
    )
    parser.add_argument(
        "--reset-index",
        action="store_true",
        help="Restart indexing from 1 in each subdirectory (only relevant if --recursive is used and --base62 is not set)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the planned renaming without modifying any files."
    )

    return parser.parse_args()
