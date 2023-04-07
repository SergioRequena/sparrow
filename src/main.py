from directory.infrastructure.file.JsonDirectoryRepository import JsonDirectoryRepository
from src.show.application.get_shows import GetShows
from src.show.domain.show import Show


def main():
    directories = JsonDirectoryRepository().execute()
    shows = []
    for directory in directories:
        if directory['IsDir'] and '{tmdb-' in directory['Name']:
            shows.append(
                Show(
                    id=directory['Name'].split('{tmdb-')[1][:-1],
                    name=directory['Name'],
                    seasons=[],
                )
            )

    shows_from_api = GetShows().execute(shows)
    print(shows_from_api)


if __name__ == '__main__':
    main()
