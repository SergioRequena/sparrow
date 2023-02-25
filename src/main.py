from directory.infrastructure.file.JsonDirectoryRepository import JsonDirectoryRepository


def main():
    directories = JsonDirectoryRepository().execute()
    print(directories)


if __name__ == '__main__':
    main()
