import json
import subprocess


class RcloneDirectoryRepository():

    def execute(self, path: str) -> list | None:
        f = open('tv_shows.json')
        data = json.load(f)
        f.close()
        return data

    '''
    def execute(self, path: str) -> list | None:
        params = ["rclone", "lsjson", path, "-R"]
        results = json.loads(subprocess.check_output(params))
        with open('tv_shows_2.json', 'w+') as json_file:
            json.dump(results, json_file)
        return results
    '''