"""
DT Music Single Player
"""

# NEW
import argparse

from dt_utility import (
    clear_screen,
    display_error_message,
)

from rich import print
from pathlib import Path
from typing import Iterator

from dt_pathlib import check_path
from dt_audio_player import play_audio_file


def main() -> None:
    """
    Main function
    """

    clear_screen()
    print("=" * 50)

    message: str

    # NEW
    description: str = "You must specify the music path!"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("music_path", help="Music Path")
    arguments = parser.parse_args()
    audio_path_str: str = arguments.music_path
    audio_path_object = check_path(path=audio_path_str)

    audio_files: Iterator[Path] = audio_path_object.glob(pattern="*.mp3")
    audio_file_list: list[Path] = list(audio_files)

    if len(audio_file_list) == 0:
        message = f"The '{audio_path_object}' path is empty or has no 'mp3' files"
        display_error_message(message=message)
        return

    while True:
        print()
        print("[bold blue]----- DT Music Player -----[/bold blue]")
        print()

        for index, song in enumerate(audio_file_list, 1):
            print(f"[{index:>3}]: {song.name}")

        print()
        prompt: str = "Enter a song number to play or 'q' to quit: "
        song_number: str = input(prompt).strip().lower()

        if song_number in ["q", "bye", "exit", "quit"]:
            break

        if not song_number.isnumeric():
            message = f"'{song_number}' is not a number"
            display_error_message(message=message)
            continue

        song_number_int = int(song_number)
        audio_file_count = len(audio_file_list)
        if song_number_int < 1 or song_number_int > audio_file_count:
            message = f"'{song_number}' is not a valid song number"
            display_error_message(message=message)
            continue

        file_path_object: Path = audio_file_list[song_number_int - 1]
        file_path: str = str(file_path_object)

        play_audio_file(
            notify=True,
            controllable=True,
            filename=file_path,
        )


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as exception:
        display_error_message(message=str(exception))

    finally:
        print("=" * 50)
        print()
