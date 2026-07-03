from rich import print

from dt_utility import (
    clear_screen,
    display_error_message,
)

# NEW
import argparse  # Solution (3)


def main() -> None:
    """
    Main function
    """

    clear_screen()
    print("=" * 50)

    # ********************
    # Solution (1)
    # ********************
    music_path: str = "music"
    print(f"'music_path': {music_path}")
    # ********************

    # ********************
    # Solution (2)
    # ********************
    # music_path: str = input("Enter Music Path: ")
    # print(f"'music_path': {music_path}")
    # ********************

    # ********************
    # Solution (3)
    #
    # > python .\learn_argparse.py
    # > python .\learn_argparse.py --help
    # > python .\learn_argparse.py -h
    # > python .\learn_argparse.py music
    # ********************
    # description: str = "You must specify the music path!"
    # parser = argparse.ArgumentParser(description=description)
    # parser.add_argument("music_path", help="Music Path")
    # arguments = parser.parse_args()

    # music_path: str = arguments.music_path
    # print(f"'music_path': {music_path}")
    # ********************

    # ********************
    # Test
    #
    # > python .\learn_argparse.py
    # > python .\learn_argparse.py --help
    # > python .\learn_argparse.py -h
    # > python .\learn_argparse.py dariush
    # > python .\learn_argparse.py dariush tasdighi
    # ********************
    # description: str = "You must specify the full name (First Name and Last Name)!"
    # parser = argparse.ArgumentParser(description=description)
    # parser.add_argument("first_name", help="First Name")
    # parser.add_argument("last_name", help="Last Name")
    # arguments = parser.parse_args()

    # last_name: str = arguments.last_name
    # first_name: str = arguments.first_name

    # full_name: str = f"'full_name': {first_name} {last_name}"
    # print(full_name)
    # ********************


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
