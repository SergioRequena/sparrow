# sparrow

A program that allows you to check your tv show collection by using 
[The Movie Database Api](https://developers.themoviedb.org/3).

# Project presentation

## Input
You will be provided with an extended json file that contains two types of objects:
* Directory
```
{
   "Path":"Game of Thrones (2011) {tmdb-1399}",
   "Name":"Game of Thrones (2011) {tmdb-1399}",
   "Size":-1,
   "MimeType":"inode/directory",
   "ModTime":"2022-04-28T18:52:07.333Z",
   "IsDir":true,
   "ID":"1NBuQnUrZVi4ECIGieQACtLr7oGyigUSM"
}
```
* File
```
{
   "Path":"Game of Thrones (2011) {tmdb-1399}/1x01 - Game of Thrones.mkv",
   "Name":"1x01 - Game of Thrones.mkv",
   "Size":1551410953,
   "MimeType":"video/x-matroska",
   "ModTime":"2019-11-14T08:25:37.612Z",
   "IsDir":false,
   "ID":"1o2ERA5GewkQ9FatiMHxjQjZ_JAFZXBEa"
}
```

## Features
We want to implement the following features:
* Scan your library looking for folders that does not contain or files or other folders.
* Scan your library looking for non-mkv files.
* Scan your library looking for non-standard naming files.
* Scan your library looking for tv shows that are incomplete.

## Output
Different log files that contains the detailed information of each feature.

## Teams

### Team 1
* Define and construct **Directory** domain entity from input objects.
* Define and construct **File** domain entity from input objects.
* Implement feature: Look for folders that does not contain or files or other folders.
* Implement feature: Look for non-mkv files.
* Implement feature: Look for non-standard naming files.

### Team 2
* Define and construct **CollectedShow** domain entity from **Directory** objects.
* Define and construct **CollectedEpisode** domain entity from **File** objects.
* Define and construct **Show** domain entity from api call.
* Define and construct **Episode** domain entity from api call.
* Implement feature: Look for tv shows that are incomplete.

## Concepts you will learn
* Virtual environments
* Environment variables
* Git branches
* External libraries
* APIs
* Hexagonal architecture
* Domain Driven Design (DDD)

# Project definition

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
│  ├─ 1x01 - Game of Thrones
│  ├─ 1x02 - Game of Thrones
│  ├─ (...)
├─ House of the Dragon (2022) {tmdb-94997}/
│  ├─ 1x01 - House of the Dragon
│  ├─ 1x02 - House of the Dragon
│  ├─ (...)
├─ (...)
```

## Getting Started
Firstly, you need to configure the virtual environment.

```
python -m venv venv

source venv/bin/activate (Linux) | venv\Scripts\activate (Windows)
```

Secondly, you need to install dependencies running the next command:

```
pip install -r requirements.txt
```

Now, create the file ```.env``` in the root folder. You will need these variables:

```
TMDB_API_KEY={YOUR_PRIVATE_API_KEY}
```