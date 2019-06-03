from pathlib import Path
from typing import List
import binascii


def scan_directory(path: str, ext: List[Path]) -> List:
    files = []

    dir_path = Path(path)

    for p in dir_path.iterdir():
        if p.suffix in ext:
            files.append(p)

    return files


def get_name(path: Path) -> str:
    file_name = path.stem.replace('_', ' ')
    return file_name.strip()


def get_item(path: Path, playlist: str) -> dict:
    item = {
        "path": str(path.resolve()),
        "label": get_name(path),
        'core_path': 'DETECT',
        'core_name': 'DETECT',
        'crc32': 'DETECT',
    }

    return item
