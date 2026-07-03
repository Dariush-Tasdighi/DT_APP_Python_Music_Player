"""
DT Music Player (Shuffle)
"""

import argparse

# NEW
import random
from typing import Final

from dt_utility import (
    clear_screen,
    display_error_message,
)

from rich import print
from pathlib import Path
from typing import Iterator

from dt_pathlib import check_path
from dt_audio_player import play_audio_file

# NEW
VERSION: Final[str] = "2.0.0"


def main() -> None:
    """
    Main function
    """

    clear_screen()
    # print("=" * 50)

    message: str

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
        # NEW
        print(f"[bold blue]<<<<< DT Music Player ({VERSION}) >>>>>[/bold blue]")
        print()

        # NEW
        random.shuffle(x=audio_file_list)

        # NEW
        for index, audio_file_path in enumerate(audio_file_list, start=1):
            print(f"{index:>3}: Playing: [green]{audio_file_path.name}[/green]", end=" ")
            audio_file_path_string: str = str(audio_file_path)

            play_audio_file(
                notify=False,
                controllable=True,
                filename=audio_file_path_string,
            )

            print()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as exception:
        display_error_message(message=str(exception))

    finally:
        # print("=" * 50)
        print()
