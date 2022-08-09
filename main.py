import os
from difflib import SequenceMatcher
from typing import Optional
import shutil


def scan_tree(path) -> list[os.DirEntry]:
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scan_tree(entry.path)
        else:
            yield entry


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


if __name__ == '__main__':

    src_path = input('File source path: ')
    dest_path = input('File destination path: ')
    dry = input('Do replace [y/n]: ') == 'y'

    if src_path == '':
        raise Exception('missing src path')
    elif dest_path == '':
        raise Exception('missing dest path')
    elif dest_path == src_path:
        raise Exception('dest and src path can\'t match')

    src_files = dict()

    files_without_match: list[os.DirEntry] = []
    replacements: list[tuple[os.DirEntry, os.DirEntry]] = []

    for src_file in scan_tree(src_path):
        dir_entries = src_files.get(src_file.name, [])
        dir_entries.append(src_file)
        src_files[src_file.name] = dir_entries

    for dest_file in scan_tree(dest_path):
        if dest_file.name not in src_files:
            files_without_match.append(dest_file)
            print(f'MISSING -> \t"{dest_file.name}"')
            continue

        best_match: Optional[os.DirEntry] = None
        for src_file in src_files[dest_file.name]:

            if best_match is None or similar(best_match.path, dest_file.path) < similar(src_file.path, dest_file.path):
                best_match = src_file

        print(f'REPLACE -> \t"{dest_file.name}" -> "{best_match.path}"')

        if not dry:
            shutil.copy(best_match.path, dest_file.path)

        replacements.append((best_match, dest_file))

    with open('missing.txt', 'w') as file:
        file.writelines([missing.path for missing in files_without_match])

    with open('replaced.txt', 'w') as file:
        file.writelines([f'{src.path} -> {dest.path}' for src, dest in replacements])


