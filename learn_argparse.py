import os
from rich import print
import argparse  # Solution (3)


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    # Solution (0)
    music_path = r".\music"
    print(f"music_path: '{music_path}'")
    # /Solution (0)

    # Solution (1)
    # music_path = "./music"
    # print(f"music_path: '{music_path}'")
    # /Solution (1)

    # Solution (2)
    # music_path: str = input("Music Path: ")
    # print(f"music_path: '{music_path}'")
    # /Solution (2)

    # Solution (3)
    # description: str = "You must specify the music path!"
    # parser = argparse.ArgumentParser(description=description)
    # parser.add_argument("music_path", help="Music Path")
    # arguments = parser.parse_args()

    # music_path: str = arguments.music_path
    # print(f"music_path: '{music_path}'")
    # /Solution (3)

    # Test
    # description: str = "You must specify the full name (First Name and Last Name)!"
    # parser = argparse.ArgumentParser(description=description)
    # parser.add_argument("first_name", help="First Name")
    # parser.add_argument("last_name", help="Last Name")
    # arguments = parser.parse_args()

    # last_name: str = arguments.last_name
    # first_name: str = arguments.first_name

    # full_name: str = f"Full Name: '{first_name} {last_name}'"
    # print(full_name)
    # /Test


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"[-] {error}!")

    print()
