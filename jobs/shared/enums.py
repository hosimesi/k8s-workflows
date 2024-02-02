from enum import Enum


class FileType(str, Enum):
    audio: str = "audio"
    text: str = "text"
