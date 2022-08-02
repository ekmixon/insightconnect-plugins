import komand
from .schema import SubmitFilesInput, SubmitFilesOutput

# Custom imports below
import json
import requests
import base64


class SubmitFiles(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_files",
            description="Adds one or more files and/or files embedded in archives to the list of pending tasks",
            input=SubmitFilesInput(),
            output=SubmitFilesOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        files = params.get("files")
        endpoint = f"{server}/tasks/create/file"
        file_list = [
            ("file", (f["filename"], base64.b64decode(f["contents"])))
            for f in files
        ]


        try:
            r = requests.post(endpoint, files=file_list)
            r.raise_for_status()
            return r.json()

        except Exception as e:
            self.logger.error(f"Error: {str(e)}")

    def test(self):
        out = self.connection.test()
        out["task_id"] = 0
        out["submit_id"] = 0
        return out
