import json
import subprocess


class RcloneDirectoryRepository():

    def execute(self, path: str) -> list:
        params = ["rclone", "lsjson", path, "-R"]
        results = json.loads(subprocess.check_output(params))
        with open('tv_shows.json', 'w+') as json_file:
            json.dump(results, json_file)
        return results
