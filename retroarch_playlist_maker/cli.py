import json
from pathlib import Path

import click

from retroarch_playlist_maker.utils import scan_directory, get_item


@click.command()
@click.option('--path', default='.', help='Path to check for playlist items.')
@click.option('--ext', '-e', default='.zip', multiple=True, help="File extensions to check in path.")
@click.option('--name', default=None,
              help="The name of the playlist to generate. Default is to use the stem of the path.")
@click.option('--playlist_path', default='.', help='The directory to save the playlist.')
def cli(path, ext, name, playlist_path):
    version = "1.0"
    res = {
        'version': version,
    }
    items = []
    click.echo(ext)
    if not name:
        dir_path = Path(path)
        name = dir_path.stem.replace('_', ' ').strip()

    out_file = Path(playlist_path / name)
    out_file = out_file.with_suffix('.lpl')

    files = scan_directory(path, ext=ext)

    for f in files:
        item = get_item(f, playlist=name)
        item['db_name'] = out_file.name
        items.append(item)

    res['items'] = items

    with out_file.open('w') as f_out:
        json.dump(res, f_out, indent=4)


if __name__ == '__main__':
    cli()
