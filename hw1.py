import argparse
import shutil
from pathlib import Path

def parse_argv():
    parser = argparse.ArgumentParser(description="Copying files to folder")
    parser.add_argument("-i", "--input", type=Path, required=True, help="Folder with files to be copied")
    parser.add_argument("-o", "--output", type=Path, default=Path("dist"), help="Folder where to copy files")
    return parser.parse_args()

def copy_files(input: Path, output: Path):
  for el in input.iterdir():
    if el.is_dir():
      copy_files(el, output)
    else:
      try:
        folder = output / el.suffix[1::]
        folder.mkdir(exist_ok=True, parents=True)
        shutil.copy(el, folder)
      except PermissionError:
        print(f"Cannot access file '{el.resolve()}'. Check access rights.")
      except Exception as e:
        print(f"Unknown error: {e}")

def main():
    args = parse_argv()
    copy_files(args.input, args.output)

main()
