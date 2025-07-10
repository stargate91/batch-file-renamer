import argparse
 
def parse_args():
	parser = argparse.ArgumentParser(description="Batch rename image files in a folder with a custom prefix and optional zero-padded numbering.")
	parser.add_argument("folder", help="Path to the folder containing the image files.")
	parser.add_argument("extension", nargs="+", help="One or more file extensions to match (e.g. .jpg .png).")
	parser.add_argument("prefix", help="Prefix for the renamed files.")
	parser.add_argument("--zero-fill", type=int, default=0, help="Number of digits for zero-padding (e.g. 3 → 001, 002). Default: no padding.")
	parser.add_argument("--dry-run", action="store_true", help="Preview changes without actually renaming files.")

	return parser.parse_args()
