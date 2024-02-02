import argparse
import json
import os

from shared.consts import ARTIFACT_BASE_DIR, DIVIDED_STT_FILE_NAME


def valid_json(json_string: str):
    try:
        # 入力が二重エスケープされたJSON文字列であることを期待して、まず一度エスケープを解除します
        unescaped_string = json_string.encode().decode('unicode_escape')
        return json.loads(unescaped_string)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid JSON: {str(e)}") from e


def load_options() -> argparse.Namespace:
    """Parse argument options."""
    description = """
    This script is entrypoint.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-f",
        "--file",
        type=valid_json,
        nargs='+',
        default=[],
        help=(
            """
            Audio file object. \n
            This includes file path, file type, and file id. \n
            ex. -f '[{"name": "file1.mp3", "obj": "AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+P0BBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmqq6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX2Nna29zd3t/g4eLj5OXm5+jp6uvs7e7v8PHy8/T19vf4+fr7/P3+/w=="}]'
            """
        ),
    )
    return parser.parse_args()



def main():
    args = load_options()
    print('Hello, world stt!')

    print(f"divided_audio_items: {args.file}")

    stt_item = {"name": "file1-1.mp3", "text": "こんにちは、世界1"}

    # 次のタスクで使用するためのパスリストを保存
    with open(os.path.join(ARTIFACT_BASE_DIR, DIVIDED_STT_FILE_NAME), "w") as f:
        json.dump(stt_item, f, indent=4)

if __name__ == '__main__':
    main()
