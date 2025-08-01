#!/usr/bin/env python3
import argparse
import sys
import os
import shutil
from pathlib import Path
from collections import defaultdict

def flatten_and_rename(root: Path, dry_run: bool = False):
    if not root.is_dir():
        print(f"Error: {root} is not a directory.", file=sys.stderr)
        sys.exit(1)

    # Walk bottom‑up so we delete children before parents
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        current_dir = Path(dirpath)

        # Skip the root itself
        if current_dir == root:
            continue

        # Skip any dir if its name—or any ancestor’s name—starts with '.'
        rel = current_dir.relative_to(root)
        if any(part.startswith('.') for part in rel.parts):
            continue

        if not filenames:
            # no files → try deleting if empty
            print(f"Removing empty folder: {current_dir}")
            if not dry_run:
                try:
                    current_dir.rmdir()
                except OSError as e:
                    print(f"  [!] Could not remove {current_dir}: {e}", file=sys.stderr)
            continue

        parent_name = current_dir.name

        # group files by extension
        ext_groups = defaultdict(list)
        for fname in filenames:
            ext = Path(fname).suffix
            ext_groups[ext].append(fname)

        # move & rename per-extension
        for ext, fnames in ext_groups.items():
            if len(fnames) == 1:
                # unique extension → no suffix
                old = current_dir / fnames[0]
                new = root / f"{parent_name}{ext}"
                print(f"Moving: {old} → {new}")
                if not dry_run:
                    shutil.move(str(old), str(new))
            else:
                # multiple files with same ext → add _1, _2, …
                for idx, fname in enumerate(fnames, start=1):
                    old = current_dir / fname
                    new = root / f"{parent_name}_{idx}{ext}"
                    print(f"Moving: {old} → {new}")
                    if not dry_run:
                        shutil.move(str(old), str(new))

        # now delete the (hopefully empty) folder
        print(f"Removing folder: {current_dir}")
        if not dry_run:
            try:
                current_dir.rmdir()
            except OSError as e:
                print(f"  [!] Could not remove {current_dir}: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Flatten subfolders: move & rename each file into the root, then delete "
            "the subfolders. Skip any folder (and its contents) if its own name—or "
            "any ancestor’s—starts with '.'."
        )
    )
    parser.add_argument(
        "root",
        type=Path,
        help="Path to the root directory"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show actions without making any changes"
    )
    args = parser.parse_args()
    flatten_and_rename(args.root, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
