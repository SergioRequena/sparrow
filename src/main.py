from logging import getLogger

import click

from directory.infrastructure.file.JsonDirectoryRepository import JsonDirectoryRepository
from src.directory.exceptions import DirectoryException


logger = getLogger(__name__)


@click.command()
def main():
    directories = JsonDirectoryRepository().execute()
    for directory in directories:
        try:
            print(repr(directory))
        except DirectoryException as exc:
            logger.error(exc)


if __name__ == '__main__':
    main()
