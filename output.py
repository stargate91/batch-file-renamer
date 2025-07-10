import os

def rename_success_message(filepath, newname):
	relpath = os.path.relpath(filepath)
	print(f"Renaming {relpath} → {newname}")

def dry_run_message(filepath, newname):
	relpath = os.path.relpath(filepath)
	print(f"[DRY RUN] Would rename {relpath} → {newname}")