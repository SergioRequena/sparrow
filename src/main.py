from directory.infrastructure.rclone.RcloneDirectoryRepository import RcloneDirectoryRepository


def main():
    directories = RcloneDirectoryRepository().execute("source_path")
    print(directories)


if __name__ == '__main__':
    main()