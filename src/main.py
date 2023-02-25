from directory.infrastructure.file.JsonDirectoryRepository import JsonDirectoryRepository


def main():
    directories = JsonDirectoryRepository().execute()
    for directory in directories:
        print(directory)


if __name__ == '__main__':
    main()
