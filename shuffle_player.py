"""
DT Music Player (Shuffle)
"""

import os
import pygame
import random
import argparse
from rich import print

VERSION: str = "1.1"


def play_mp3_file(path: str, filename: str) -> None:
    """Play mp3 file"""

    file_path: str = os.path.join(path, filename)

    if not os.path.exists(path=file_path):
        print(f"[-] Music file: '{file_path}' not found!\n")
        exit()

    if not os.path.isfile(path=file_path):
        print(f"[-] Music file: '{file_path}' not found!\n")
        exit()

    if not file_path.endswith(".mp3"):
        print(f"[-] Music file: '{file_path}' is not a mp3 file!\n")
        exit()

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename=file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    description: str = "You must specify the music path!"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("music_path", help="Music Path")
    arguments = parser.parse_args()

    music_path: str = arguments.music_path

    if not os.path.exists(path=music_path):
        print(f"[-] Music path: '{music_path}' not found!\n")
        exit()

    if not os.path.isdir(s=music_path):
        print(f"[-] Music path: '{music_path}' not found!\n")
        exit()

    files: list[str] = os.listdir(path=music_path)

    if len(files) == 0:
        print(f"[-] Music path: '{music_path}' is empty!\n")
        exit()

    mp3_files: list[str] = [file for file in files if file.endswith(".mp3")]

    if len(mp3_files) == 0:
        print(f"[-] Music path: '{music_path}' has no mp3 files!\n")
        exit()

    while True:
        random.shuffle(x=mp3_files)

        print(f"# DT Music Shuffle Player {VERSION} (Song Count: {len(mp3_files)})\n")

        for index, song_filename in enumerate(mp3_files, start=1):
            index_string = f"{index}".rjust(3, " ")

            print(f"[{index_string}] Song is playing: '{song_filename}'", end=" ")
            play_mp3_file(path=music_path, filename=song_filename)
            print()

        print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as error:
        print(f"[-] {error}!")

    print()
