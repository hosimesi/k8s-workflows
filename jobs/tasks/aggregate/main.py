import json
import os

from shared.consts import (AGGREGATE_TEXT_FILE_NAME, ARTIFACT_BASE_DIR,
                           DIVIDED_STT_FILE_NAME)


def main():
    print('Hello, world aggregate!')

    # Get From GCS.
    with open(os.path.join(ARTIFACT_BASE_DIR, DIVIDED_STT_FILE_NAME), "w") as f:
        divided_files = json.load(f, indent=4)

    aggregate_text_items = []

    for file_object in divided_files:
        print(f"file_object: {file_object}")
        aggregate_text_items.append(file_object)

    # 次のタスクで使用するためのパスリストを保存
    with open(os.path.join(ARTIFACT_BASE_DIR, AGGREGATE_TEXT_FILE_NAME), "w") as f:
        json.dump(aggregate_text_items, f, indent=4)




if __name__ == '__main__':
    main()
