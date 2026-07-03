# **************************************************
# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     age = int(input("Enter your age: "))
#     temp = 1 / age

#     print("Welcome to DT Music Player!")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# # NEW
# import os

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     # NEW
#     message: str

#     # NEW
#     music_path: str = ""
#     # music_path: str = "     "
#     # music_path: str = "./tmp"
#     # music_path: str = "./tmp.txt"
#     # music_path: str = "./folder_empty"
#     # music_path: str = "./folder_temp"
#     # music_path: str = "./music"

#     # NEW
#     music_path = music_path.strip()
#     if not music_path:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     # NEW
#     if not os.path.exists(path=music_path):
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     # NEW
#     if not os.path.isdir(s=music_path):
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     # NEW
#     files: list[str] = os.listdir(path=music_path)

#     # NEw
#     if len(files) == 0:
#         message = f"Music path '{music_path}' is empty"
#         display_error_message(message=message)
#         return

#     # NEW: Solution (1)
#     # mp3_files: list[str] = []
#     # for file in files:
#     #     if file.endswith(".mp3"):
#     #         mp3_files.append(file)

#     # NEW: Solution (2): Best Practice
#     mp3_files: list[str] = [file for file in files if file.endswith(".mp3")]

#     if len(mp3_files) == 0:
#         message = f"There is not any 'mp3' files in music path '{music_path}'"
#         display_error_message(message=message)
#         return

#     # NEW
#     print(mp3_files)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# # NEW
# # import os
# import sys
# from pathlib import Path
# from typing import Iterator

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     message: str

#     # music_path_str: str = ""
#     # music_path_str: str = "     "
#     # music_path_str: str = "./tmp"
#     # music_path_str: str = "./tmp.txt"
#     # music_path_str: str = "./folder_empty"
#     # music_path_str: str = "./folder_temp"
#     music_path_str: str = "./music"

#     music_path_str = music_path_str.strip()
#     if not music_path_str:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     # NEW
#     music_path = Path(music_path_str).resolve()

#     # NEW
#     # print(music_path)  # For Debugging!
#     # print(music_path.name)  # For Debugging!
#     # sys.exit(1)  # For Debugging!

#     # NEW
#     # if not os.path.exists(path=music_path):
#     if not music_path.exists():
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     # NEW
#     # if not os.path.isdir(s=music_path):
#     if not music_path.is_dir():
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     # NEW
#     # files: list[str] = os.listdir(path=music_path)
#     files: Iterator[Path] = music_path.glob(pattern="*")
#     file_list: list[Path] = list(files)  # Convert the iterator to a list

#     # NEw
#     # if len(files) == 0:
#     if len(file_list) == 0:
#         message = f"Music path '{music_path}' is empty"
#         display_error_message(message=message)
#         return

#     # NEW: Solution (1)
#     # mp3_files: list[Path] = []
#     # for file in file_list:
#     #     if file.name.endswith(".mp3"):
#     #         mp3_files.append(file)

#     # NEW: Solution (2): Best Practice
#     # mp3_files: list[str] = [file for file in files if file.name.endswith(".mp3")]
#     mp3_files: list[Path] = [file for file in file_list if file.name.endswith(".mp3")]

#     if len(mp3_files) == 0:
#         message = f"There is not any 'mp3' files in music path '{music_path}'"
#         display_error_message(message=message)
#         return

#     # NEW
#     print(mp3_files)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# from pathlib import Path
# from typing import Iterator

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     message: str

#     # music_path_str: str = ""
#     # music_path_str: str = "     "
#     # music_path_str: str = "./tmp"
#     # music_path_str: str = "./tmp.txt"
#     # music_path_str: str = "./folder_empty"
#     # music_path_str: str = "./folder_temp"
#     music_path_str: str = "./music"

#     music_path_str = music_path_str.strip()
#     if not music_path_str:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     music_path = Path(music_path_str).resolve()

#     if not music_path.exists():
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     if not music_path.is_dir():
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     # NEW: '*' -> '*.mp3'
#     mp3_files: Iterator[Path] = music_path.glob(pattern="*.mp3")
#     mp3_file_list: list[Path] = list(mp3_files)

#     if len(mp3_file_list) == 0:
#         message = f"Music path '{music_path}' is empty or has no mp3 files"
#         display_error_message(message=message)
#         return

#     print(mp3_file_list)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# import sys

# from rich import print
# from pathlib import Path
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )
# from typing import Iterator


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     message: str
#     music_path_str: str = "./music"

#     music_path_str = music_path_str.strip()
#     if not music_path_str:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     music_path = Path(music_path_str).resolve()

#     if not music_path.exists():
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     if not music_path.is_dir():
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     mp3_files: Iterator[Path] = music_path.glob(pattern="*.mp3")
#     mp3_file_list: list[Path] = list(mp3_files)

#     if len(mp3_file_list) == 0:
#         message = f"Music path '{music_path}' is empty or has no mp3 files"
#         display_error_message(message=message)
#         return

#     # NEW
#     while True:
#         print()
#         print("----- DT Music Player -----")
#         print()

#         for index, song in enumerate(mp3_file_list):
#             print(f"[{index + 1}]: {song}")
#         sys.exit(0)  # For Debugging!

#         # for index, song in enumerate(mp3_file_list, start=1):
#         #     print(f"[{index}]: {song}")
#         # sys.exit(0)  # For Debugging!

#         # for index, song in enumerate(mp3_file_list, 1):
#         #     index_string = f"{index}".rjust(3, " ")
#         #     print(f"[{index_string}]: {song}")

#         # for index, song in enumerate(mp3_file_list, 1):
#         #     # print(f"[{index:<3}]: {song}")
#         #     print(f"[{index:>3}]: {song}")

#         # for index, song in enumerate(mp3_file_list, 1):
#         #     print(f"[{index:>3}]: {song.name}")

#         print()
#         prompt: str = "Enter a song number to play or 'q' to quit: "
#         song_number: str = input(prompt).strip().lower()

#         if song_number in ["q", "bye", "exit", "quit"]:
#             break

#         if not song_number.isnumeric():
#             message = f"'{song_number}' is not a number"
#             display_error_message(message=message)
#             continue

#         if int(song_number) < 1 or int(song_number) > len(mp3_file_list):
#             message = f"'{song_number}' is not a valid song number!"
#             display_error_message(message=message)
#             continue

#         print("OK")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# # NEW
# import pygame

# import sys

# from rich import print
# from pathlib import Path
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )
# from typing import Iterator


# # NEW
# def play_mp3_file(mp3_file_path: Path) -> None:
#     """
#     Play mp3 file
#     """

#     message: str

#     if not mp3_file_path.exists():
#         message = f"Music file '{mp3_file_path}' not found"
#         raise Exception(message)

#     if not mp3_file_path.is_file():
#         message = f"Music file '{mp3_file_path}' is directory, not file"
#         raise Exception(message)

#     if not mp3_file_path.name.endswith(".mp3"):
#         message = f"Music file '{mp3_file_path}' is not a mp3 file"
#         raise Exception(message)

#     mp3_file_path_str: str = str(mp3_file_path.resolve())

#     print(f"Playing 'mp3' File: '{mp3_file_path_str}'")

#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(filename=mp3_file_path_str)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#     # Note: The below code does not work properly!
#     # pygame.event.wait()


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     # NEW
#     # # file_path: Path = Path("")
#     # # file_path: Path = Path("     ")
#     # # file_path: Path = Path("./music/googooli")
#     # # file_path: Path = Path("./folder_temp/tmp.txt")
#     # file_path: Path = Path("test/sample-6s.mp3")

#     # play_mp3_file(mp3_file_path=file_path)  # For Debugging!
#     # sys.exit(0)  # For Debugging!

#     message: str

#     # NEW
#     music_path_str: str = "./test"
#     # music_path_str: str = "./music"

#     music_path_str = music_path_str.strip()
#     if not music_path_str:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     music_path = Path(music_path_str).resolve()

#     if not music_path.exists():
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     if not music_path.is_dir():
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     mp3_files: Iterator[Path] = music_path.glob(pattern="*.mp3")
#     mp3_file_list: list[Path] = list(mp3_files)

#     if len(mp3_file_list) == 0:
#         message = f"Music path '{music_path}' is empty or has no mp3 files"
#         display_error_message(message=message)
#         return

#     while True:
#         print()
#         print("----- DT Music Player -----")
#         print()

#         for index, song in enumerate(mp3_file_list, 1):
#             print(f"[{index:>3}]: {song.name}")

#         print()
#         prompt: str = "Enter a song number to play or 'q' to quit: "
#         song_number: str = input(prompt).strip().lower()

#         if song_number in ["q", "bye", "exit", "quit"]:
#             break

#         if not song_number.isnumeric():
#             message = f"'{song_number}' is not a number"
#             display_error_message(message=message)
#             continue

#         if int(song_number) < 1 or int(song_number) > len(mp3_file_list):
#             message = f"'{song_number}' is not a valid song number!"
#             display_error_message(message=message)
#             continue

#         # NEW
#         file_path: Path = mp3_file_list[int(song_number) - 1]
#         play_mp3_file(mp3_file_path=file_path)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# import sys
# import pygame

# from rich import print
# from pathlib import Path
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )
# from typing import Iterator


# def play_mp3_file(
#     mp3_file_path: Path,
#     notify: bool = False,
#     controllable: bool = False,
# ) -> None:
#     """
#     Play mp3 file
#     """

#     message: str

#     if not mp3_file_path.exists():
#         message = f"Music file '{mp3_file_path}' not found"
#         raise Exception(message)

#     if not mp3_file_path.is_file():
#         message = f"Music file '{mp3_file_path}' is directory, not file"
#         raise Exception(message)

#     if not mp3_file_path.name.endswith(".mp3"):
#         message = f"Music file '{mp3_file_path}' is not a mp3 file"
#         raise Exception(message)

#     mp3_file_path_str: str = str(mp3_file_path.resolve())

#     # NEW
#     if notify:
#         print(f"Playing 'mp3' File: '{mp3_file_path_str}'")

#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(filename=mp3_file_path_str)
#     pygame.mixer.music.play()

#     # NEW
#     if not controllable:
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
#         # Note: The below code does not work properly!
#         # pygame.event.wait()
#     # NEW
#     else:
#         while True:
#             prompt: str = "Press 'p' for pause, 'r' for resume, 's' for stop: "
#             choise: str = input(prompt).strip().lower()

#             match choise:
#                 case "p":
#                     pygame.mixer.music.pause()
#                 case "r":
#                     pygame.mixer.music.unpause()
#                 case "s":
#                     pygame.mixer.music.stop()
#                     break
#                 case _:
#                     pass


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     # NEW
#     # # file_path: Path = Path("")
#     # # file_path: Path = Path("     ")
#     # # file_path: Path = Path("./music/googooli")
#     # # file_path: Path = Path("./folder_temp/tmp.txt")
#     # file_path: Path = Path("test/sample-6s.mp3")

#     # play_mp3_file(mp3_file_path=file_path)  # For Debugging!
#     # sys.exit(0)  # For Debugging!

#     message: str

#     # NEW
#     music_path_str: str = "./test"
#     # music_path_str: str = "./music"

#     music_path_str = music_path_str.strip()
#     if not music_path_str:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     music_path = Path(music_path_str).resolve()

#     if not music_path.exists():
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     if not music_path.is_dir():
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     mp3_files: Iterator[Path] = music_path.glob(pattern="*.mp3")
#     mp3_file_list: list[Path] = list(mp3_files)

#     if len(mp3_file_list) == 0:
#         message = f"Music path '{music_path}' is empty or has no mp3 files"
#         display_error_message(message=message)
#         return

#     while True:
#         print()
#         print("----- DT Music Player -----")
#         print()

#         for index, song in enumerate(mp3_file_list, 1):
#             print(f"[{index:>3}]: {song.name}")

#         print()
#         prompt: str = "Enter a song number to play or 'q' to quit: "
#         song_number: str = input(prompt).strip().lower()

#         if song_number in ["q", "bye", "exit", "quit"]:
#             break

#         if not song_number.isnumeric():
#             message = f"'{song_number}' is not a number"
#             display_error_message(message=message)
#             continue

#         if int(song_number) < 1 or int(song_number) > len(mp3_file_list):
#             message = f"'{song_number}' is not a valid song number!"
#             display_error_message(message=message)
#             continue

#         file_path: Path = mp3_file_list[int(song_number) - 1]

#         # NEW
#         # play_mp3_file(mp3_file_path=file_path)
#         # play_mp3_file(mp3_file_path=file_path, notify=True)
#         play_mp3_file(mp3_file_path=file_path, notify=True, controllable=True)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# import pygame

# # NEW
# from readchar import (
#     key,
#     readkey,
# )

# from rich import print
# from pathlib import Path
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )
# from typing import Iterator


# def play_mp3_file(
#     mp3_file_path: Path,
#     notify: bool = False,
#     controllable: bool = False,
# ) -> None:
#     """
#     Play mp3 file
#     """

#     message: str

#     if not mp3_file_path.exists():
#         message = f"Music file '{mp3_file_path}' not found"
#         raise Exception(message)

#     if not mp3_file_path.is_file():
#         message = f"Music file '{mp3_file_path}' is directory, not file"
#         raise Exception(message)

#     if not mp3_file_path.name.endswith(".mp3"):
#         message = f"Music file '{mp3_file_path}' is not a mp3 file"
#         raise Exception(message)

#     mp3_file_path_str: str = str(mp3_file_path.resolve())

#     if notify:
#         print(f"Playing 'mp3' File: '{mp3_file_path_str}'")

#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(filename=mp3_file_path_str)
#     pygame.mixer.music.play()

#     if not controllable:
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
#         # Note: The below code does not work properly!
#         # pygame.event.wait()
#     else:
#         is_paused: bool = False
#         while True:
#             prompt: str = (
#                 "Press 'SPACE' for pause / resume, 'l' for add to favorites, 'ESC' for stop: "
#             )
#             choise: str = readkey().lower()

#             match choise:
#                 case key.SPACE:
#                     if is_paused:
#                         is_paused = False
#                         pygame.mixer.music.unpause()
#                     else:
#                         pygame.mixer.music.pause()
#                         is_paused = True
#                 case key.ESC:
#                     pygame.mixer.music.stop()
#                     break
#                 case "l":
#                     parent_path = mp3_file_path.parent.parent
#                     favorites_path = parent_path / "favorites"
#                     favorites_path.mkdir(exist_ok=True)
#                     target_path = favorites_path / mp3_file_path.name
#                     mp3_file_path.copy(target_path)
#                 case _:
#                     pass


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     # NEW
#     # # file_path: Path = Path("")
#     # # file_path: Path = Path("     ")
#     # # file_path: Path = Path("./music/googooli")
#     # # file_path: Path = Path("./folder_temp/tmp.txt")
#     # file_path: Path = Path("test/sample-6s.mp3")

#     # play_mp3_file(mp3_file_path=file_path)  # For Debugging!
#     # sys.exit(0)  # For Debugging!

#     message: str

#     # NEW
#     music_path_str: str = "./test"
#     # music_path_str: str = "./music"

#     music_path_str = music_path_str.strip()
#     if not music_path_str:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     music_path = Path(music_path_str).resolve()

#     if not music_path.exists():
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     if not music_path.is_dir():
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     mp3_files: Iterator[Path] = music_path.glob(pattern="*.mp3")
#     mp3_file_list: list[Path] = list(mp3_files)

#     if len(mp3_file_list) == 0:
#         message = f"Music path '{music_path}' is empty or has no mp3 files"
#         display_error_message(message=message)
#         return

#     while True:
#         print()
#         print("[bold green]----- DT Music Player -----[/bold green]")
#         print()

#         for index, song in enumerate(mp3_file_list, 1):
#             print(f"[{index:>3}]: {song.name}")

#         print()
#         prompt: str = "Enter a song number to play or 'q' to quit: "
#         song_number: str = input(prompt).strip().lower()

#         if song_number in ["q", "bye", "exit", "quit"]:
#             break

#         if not song_number.isnumeric():
#             message = f"'{song_number}' is not a number"
#             display_error_message(message=message)
#             continue

#         if int(song_number) < 1 or int(song_number) > len(mp3_file_list):
#             message = f"'{song_number}' is not a valid song number!"
#             display_error_message(message=message)
#             continue

#         file_path: Path = mp3_file_list[int(song_number) - 1]

#         # NEW
#         # play_mp3_file(mp3_file_path=file_path)
#         # play_mp3_file(mp3_file_path=file_path, notify=True)
#         play_mp3_file(mp3_file_path=file_path, notify=True, controllable=True)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# from dt_readkey import read_key

# print("Press any key to continue...", end=" ", flush=True)
# key = read_key()
# print(key)
# **************************************************


# **************************************************
# from dt_readkey import read_key

# print("Press any key to continue...", end=" ", flush=True)
# key = read_key(timeout=5000)
# if key is None:
#     print("No key pressed within the timeout period.")
# else:
#     print(f"Key: {key}")
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# import pygame

# # NEW
# from dt_read_key import (
#     Keys,
#     read_key,
# )

# from typing import (
#     Final,
#     Iterator,
#     Optional,
# )

# from rich import print
# from pathlib import Path
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )

# # NEW
# MUSIC_END: Final[int] = pygame.USEREVENT + 1

# # pygame.init()
# # pygame.mixer.init()
# # pygame.mixer.music.set_endevent(MUSIC_END)


# def play_mp3_file(
#     mp3_file_path: Path,
#     notify: bool = False,
#     controllable: bool = False,
# ) -> None:
#     """
#     Play mp3 file
#     """

#     message: str

#     if not mp3_file_path.exists():
#         message = f"Music file '{mp3_file_path}' not found"
#         raise Exception(message)

#     if not mp3_file_path.is_file():
#         message = f"Music file '{mp3_file_path}' is directory, not file"
#         raise Exception(message)

#     if not mp3_file_path.name.endswith(".mp3"):
#         message = f"Music file '{mp3_file_path}' is not a mp3 file"
#         raise Exception(message)

#     mp3_file_path_str: str = str(mp3_file_path.resolve())

#     if notify:
#         print(f"Playing 'mp3' File: '{mp3_file_path_str}'")

#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.set_endevent(MUSIC_END)
#     pygame.mixer.music.load(filename=mp3_file_path_str)
#     pygame.mixer.music.play()

#     if not controllable:
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
#         # Note: The below code does not work properly!
#         # pygame.event.wait()
#     else:
#         is_paused: bool = False
#         while True:
#             prompt: str = (
#                 "Press 'SPACE': pause / resume | 'l': for add to favorites |'ESC': stop: "
#             )

#             # NEW
#             choise: Optional[str] = read_key(timeout=100)

#             # NEW
#             for event in pygame.event.get():
#                 if event.type == MUSIC_END:
#                     pygame.event.clear(MUSIC_END)
#                     return

#             match choise:
#                 case " ":
#                     if is_paused:
#                         is_paused = False
#                         pygame.mixer.music.unpause()
#                     else:
#                         pygame.mixer.music.pause()
#                         is_paused = True

#                 case Keys.ESC:
#                     pygame.mixer.music.stop()
#                     pygame.event.clear(MUSIC_END)
#                     break

#                 case "l":
#                     parent_path = mp3_file_path.parent.parent
#                     favorites_path = parent_path / "favorites"
#                     favorites_path.mkdir(exist_ok=True)
#                     target_path = favorites_path / mp3_file_path.name
#                     mp3_file_path.copy(target_path)


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     message: str

#     music_path_str: str = "./test"
#     # music_path_str: str = "./music"

#     music_path_str = music_path_str.strip()
#     if not music_path_str:
#         message: str = f"You did not specify music path! music path is empty"
#         display_error_message(message=message)
#         return

#     music_path = Path(music_path_str).resolve()

#     if not music_path.exists():
#         message: str = f"Music path '{music_path}' not found"
#         display_error_message(message=message)
#         return

#     if not music_path.is_dir():
#         message: str = f"Music path '{music_path}' is file, not directory"
#         display_error_message(message=message)
#         return

#     mp3_files: Iterator[Path] = music_path.glob(pattern="*.mp3")
#     mp3_file_list: list[Path] = list(mp3_files)

#     if len(mp3_file_list) == 0:
#         message = f"Music path '{music_path}' is empty or has no mp3 files"
#         display_error_message(message=message)
#         return

#     while True:
#         print()
#         print("[bold green]----- DT Music Player -----[/bold green]")
#         print()

#         for index, song in enumerate(mp3_file_list, 1):
#             print(f"[{index:>3}]: {song.name}")

#         print()
#         prompt: str = "Enter a song number to play or 'q' to quit: "
#         song_number: str = input(prompt).strip().lower()

#         if song_number in ["q", "bye", "exit", "quit"]:
#             break

#         if not song_number.isnumeric():
#             message = f"'{song_number}' is not a number"
#             display_error_message(message=message)
#             continue

#         if int(song_number) < 1 or int(song_number) > len(mp3_file_list):
#             message = f"'{song_number}' is not a valid song number!"
#             display_error_message(message=message)
#             continue

#         file_path: Path = mp3_file_list[int(song_number) - 1]

#         # play_mp3_file(mp3_file_path=file_path)
#         # play_mp3_file(mp3_file_path=file_path, notify=True)
#         play_mp3_file(mp3_file_path=file_path, notify=True, controllable=True)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )

# from rich import print
# from pathlib import Path
# from typing import Iterator

# from dt_pathlib import check_path
# from dt_audio_player import play_audio_file


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     message: str

#     # audio_path_str: str = ""
#     # audio_path_str: str = "   "
#     # audio_path_str: str = "./tmp"
#     # audio_path_str: str = "./tmp.txt"
#     # audio_path_str: str = "./folder_empty"
#     # audio_path_str: str = "./folder_temp"

#     audio_path_str: str = "./test"
#     # audio_path_str: str = "./music"

#     audio_path_object = check_path(path=audio_path_str)

#     audio_files: Iterator[Path] = audio_path_object.glob(pattern="*.mp3")
#     audio_file_list: list[Path] = list(audio_files)

#     if len(audio_file_list) == 0:
#         message = f"The '{audio_path_object}' path is empty or has no 'mp3' files"
#         display_error_message(message=message)
#         return

#     while True:
#         print()
#         print("[bold green]----- DT Music Player -----[/bold green]")
#         print()

#         for index, song in enumerate(audio_file_list, 1):
#             print(f"[{index:>3}]: {song.name}")

#         print()
#         prompt: str = "Enter a song number to play or 'q' to quit: "
#         song_number: str = input(prompt).strip().lower()

#         if song_number in ["q", "bye", "exit", "quit"]:
#             break

#         if not song_number.isnumeric():
#             message = f"'{song_number}' is not a number"
#             display_error_message(message=message)
#             continue

#         if int(song_number) < 1 or int(song_number) > len(audio_file_list):
#             message = f"'{song_number}' is not a valid song number!"
#             display_error_message(message=message)
#             continue

#         file_path_object: Path = audio_file_list[int(song_number) - 1]
#         file_path = str(file_path_object)

#         play_audio_file(filename=file_path, notify=True, controllable=True)


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# """
# DT Music Single Player
# """

# from dt_utility import (
#     clear_screen,
#     display_error_message,
# )

# from rich import print
# from pathlib import Path
# from typing import Iterator

# from dt_pathlib import check_path
# from dt_audio_player import play_audio_file


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     print("=" * 50)

#     message: str

#     audio_path_str: str = "./test"
#     # audio_path_str: str = "./music"

#     audio_path_object = check_path(path=audio_path_str)

#     audio_files: Iterator[Path] = audio_path_object.glob(pattern="*.mp3")
#     audio_file_list: list[Path] = list(audio_files)

#     if len(audio_file_list) == 0:
#         message = f"The '{audio_path_object}' path is empty or has no 'mp3' files"
#         display_error_message(message=message)
#         return

#     while True:
#         print()
#         print("[bold green]----- DT Music Player -----[/bold green]")
#         print()

#         for index, song in enumerate(audio_file_list, 1):
#             print(f"[{index:>3}]: {song.name}")

#         print()
#         prompt: str = "Enter a song number to play or 'q' to quit: "
#         song_number: str = input(prompt).strip().lower()

#         if song_number in ["q", "bye", "exit", "quit"]:
#             break

#         if not song_number.isnumeric():
#             message = f"'{song_number}' is not a number"
#             display_error_message(message=message)
#             continue

#         song_number_int = int(song_number)
#         audio_file_count = len(audio_file_list)
#         if song_number_int < 1 or song_number_int > audio_file_count:
#             message = f"'{song_number}' is not a valid song number"
#             display_error_message(message=message)
#             continue

#         file_path_object: Path = audio_file_list[song_number_int - 1]
#         file_path: str = str(file_path_object)

#         play_audio_file(
#             notify=True,
#             controllable=True,
#             filename=file_path,
#         )


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         print("=" * 50)
#         print()
# **************************************************
