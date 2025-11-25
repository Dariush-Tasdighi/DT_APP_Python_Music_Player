"""
DT Music Player
"""

import os
import pygame
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

    while True:
        prompt: str = "Press 'p' for pause, 'r' for resume, 's' for stop: "
        choise: str = input(prompt).strip().lower()

        match choise:
            case "p":
                pygame.mixer.music.pause()
            case "r":
                pygame.mixer.music.unpause()
            case "s":
                pygame.mixer.music.stop()
                break
            case _:
                pass


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    music_path: str = "./music"

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
        print("\n----- DT Music Player -----\n")

        for index, song in enumerate(mp3_files):
            index_string = f"{index + 1}".rjust(3, " ")
            print(f"[{index_string}]: {song}")

        prompt: str = "\nEnter a song number to play or 'q' to quit: "
        song_number: str = input(prompt).strip().lower()

        if song_number == "q":
            break

        if not song_number.isnumeric():
            print(f"[-] '{song_number}' is not a number!\n")
            continue

        if int(song_number) < 1 or int(song_number) > len(mp3_files):
            print(f"[-] '{song_number}' is not a valid song number!\n")
            continue

        filename: str = mp3_files[int(song_number) - 1]
        play_mp3_file(path=music_path, filename=filename)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"[-] {error}!")

    print()
