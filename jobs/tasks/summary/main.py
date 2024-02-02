import argparse
import json
import os

from shared.consts import ARTIFACT_BASE_DIR, TEXT_FILE_NAME


def load_options() -> argparse.Namespace:
    """Parse argument options."""

    description = """
    This script is entrypoint.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-f",
        "--file",
        type=json.loads,
        default={"id": "1", "path": "/path/to/file1.mp3", "type": "audio"},
        help=(
            """
            Audio file object. \n
            This includes file path, file type, and file id. \n
            ex. -f '{"id": "1", "path": "/path/to/file1.mp3", "type": "audio"}'
            """
        ),
    )

    return parser.parse_args()

def main():
    args = load_options()
    print('Hello, world summary!')

    print(args.file)



if __name__ == '__main__':
    main()
    main()
