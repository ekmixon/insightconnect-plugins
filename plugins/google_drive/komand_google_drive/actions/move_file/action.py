import komand
from .schema import MoveFileInput, MoveFileOutput, Input, Output, Component

# Custom imports below
from googleapiclient import errors


class MoveFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="move_file", description=Component.DESCRIPTION, input=MoveFileInput(), output=MoveFileOutput()
        )

    def run(self, params={}):
        file_id = params.get(Input.FILE_ID)
        folder_id = params.get(Input.FOLDER_ID)
        try:
            file_parents = self.connection.service.files().get(fileId=file_id, fields="parents").execute()
            file_parents = ",".join(file_parents.get("parents", []))

            return {
                Output.RESULT: self.connection.service.files()
                .update(fileId=file_id, addParents=folder_id, removeParents=file_parents, fields="id, parents")
                .execute()
            }
        except errors.HttpError as error:
            raise Exception("An error occurred: %s" % error)
