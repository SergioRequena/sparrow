from typing import TypedDict


class Path(TypedDict):
    Path: str
    Name: str
    Size: int
    MimeType: str
    ModTime: str
    Isdir: bool
