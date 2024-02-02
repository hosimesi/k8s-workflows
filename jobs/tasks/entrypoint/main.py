import argparse
import json
import os

from models.interface import Args
from shared.consts import ARTIFACT_BASE_DIR, AUDIO_FILE_NAME, TEXT_FILE_NAME
from shared.enums import FileType


def load_options() -> argparse.Namespace:
    """Parse argument options."""

    description = """
    This script is entrypoint.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-f",
        "--files",
        type=json.loads,
        default=[{"id": "1", "path": "/path/to/file1.mp3", "type": "audio"}, {"id": "2", "path": "/path/to/file2.txt", "type": "text"}],
        help=(
            """
            List of files object. \n
            This includes file path, file type, and file id. \n
            ex. -f '[{"id": "1", "path": "/path/to/file1.mp3", "type": "audio"}, {"id": "2", "path": "/path/to/file2.txt", "type": "text"}]'
            """
        ),
    )

    return parser.parse_args()

def main():
    args = load_options()

    items = [Args(**item) for item in args.files]
    text_items = []
    audio_items = []

    # pydandic BaseModel converts to dict because we need to json serializable.
    for item in items:
        if item.file_type == FileType.audio:
            audio_items.append(item.model_dump())
        elif item.file_type == FileType.text:
            text_items.append(item.model_dump())
        else:
            raise Exception("Invalid file type.")

    # Get From GCS.
    with open(os.path.join(ARTIFACT_BASE_DIR, TEXT_FILE_NAME), "w") as f:
        json.dump(text_items, f, indent=4)

    with open(os.path.join(ARTIFACT_BASE_DIR, AUDIO_FILE_NAME), "w") as f:
        json.dump(audio_items, f, indent=4)

    print("Done.")

if __name__ == '__main__':
    main()
