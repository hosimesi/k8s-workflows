import argparse
import base64
import json
import os

from shared.consts import ARTIFACT_BASE_DIR, DIVIDED_AUDIO_FILE_NAME


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
    print('Hello, world vad!')

    print(f"audio_items: {args.file}")

    # TODO: Implement vad.
    # 一旦仮おきで適当なバイナリデータを作成
    binary_data = bytes([i for i in range(256)])
    base64_data = base64.b64encode(binary_data).decode('utf-8')

    # # parametersで渡すので、重くならないように先にgcsにあげてファイルパスを保存にしても良さそう
    vad_items =[{"name": "file1-1.mp3", "obj": base64_data}, {"name": "file1-2.mp3", "obj": base64_data}, {"name": "file1-3.mp3", "obj": base64_data}, {"name": "file1-4.mp3", "obj": base64_data}]

    print(f"vad_items: {vad_items}")

    # 次のタスクで使用するためのパスリストを保存
    with open(os.path.join(ARTIFACT_BASE_DIR, DIVIDED_AUDIO_FILE_NAME), "w") as f:
        json.dump(vad_items, f, indent=4)



if __name__ == '__main__':
    main()
