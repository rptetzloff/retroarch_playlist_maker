# retroarch_playlist_maker

## Information

Generate an XML-style RetroArch playlist via cli.

- Should work on Linux, MacOS, or Windows

## TODO

- crc support?
- handling of core files and names
- thumbnails
- GUI?
- Documentation

## CLI Script

```bash
make_playlist --help                                                                                                                                                                                          199ms  Mon Jun  3 14:26:52 2019
Usage: make_playlist [OPTIONS]

Options:
  --path TEXT           Path to check for playlist items.
  -e, --ext TEXT        File extensions to check in path.
  --name TEXT           The name of the playlist to generate. Default is to
                        use the stem of the path.
  --playlist_path TEXT  The directory to save the playlist.
  --help                Show this message and exit.

```

### Examples

```bash
make_playlist --path "Z:\roms\Nintendo - Nintendo Entertainment System" -e .zip --playlist_path C:\Users\ray\AppData\Roaming\RetroArch\playlists
```