# sparrow

A program that allows you to check your tv show collection by using 
[The Movie Database Api](https://developers.themoviedb.org/3).

## Features
* Scan your library looking for folders that does not contain or files or other folders. 
* Scan your library looking for non-mkv files.
* Scan your library looking for non-standard naming files.
* Scan your library looking for tv shows that are incomplete.

## Initial conditions
Your collection must follow the next structure:
```
SOURCE_PATH/
├─ %tv_show_name% %tv_show_start_year% {tmdb-%tmdb_id%}/
│  ├─ %season%x%episode_with_2_chars_padding% - %tv_show_name%
│  ├─ (...)
├─ %tv_show_name% %tv_show_start_year% {tmdb-%tmdb_id%}/
├─ (...)
----------------------------------------------------------------
SOURCE_PATH/
├─ Game of Thrones (2011) {tmdb-1399}/
│  ├─ 1x01 - Game of Thrones.mkv
│  ├─ 1x02 - Game of Thrones.mkv
│  ├─ (...)
├─ House of the Dragon (2022) {tmdb-94997}/
│  ├─ 1x01 - House of the Dragon.mkv
│  ├─ 1x02 - House of the Dragon.mkv
│  ├─ (...)
├─ (...)
```

## Getting Started
Firstly, you need to configure the virtual environment.

```
python -m venv venv

source venv/bin/activate (Linux) | venv\Scripts\activate (Windows)
```