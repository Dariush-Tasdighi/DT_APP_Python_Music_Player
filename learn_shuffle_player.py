"""
DT Music Player (Shuffle)
"""

import os
import pygame

# NEW
import random
from rich import print


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

    # NEW
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    # NEW
    music_path: str = "./test"
    # music_path: str = "./music"

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
        # NEW
        random.shuffle(x=mp3_files)

        print(f"----- DT Music Player (Song Count: {len(mp3_files)}) -----\n")

        # NEW - start=1
        for index, song_filename in enumerate(mp3_files, start=1):
            index_string = f"{index}".rjust(3, " ")

            # NEW - end=" "
            print(f"[{index_string}] Song is playing: '{song_filename}'", end=" ")
            play_mp3_file(path=music_path, filename=song_filename)
            print()

        print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        # NEW
        # pass
        print()

    except Exception as error:
        print(f"[-] {error}!")

    print()
