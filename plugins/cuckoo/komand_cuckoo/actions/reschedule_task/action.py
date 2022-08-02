import komand
from .schema import RescheduleTaskInput, RescheduleTaskOutput

# Custom imports below
import json
import requests


class RescheduleTask(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reschedule_task",
            description="Reschedule a task with the specified ID and priority (default priority is 1)",
            input=RescheduleTaskInput(),
            output=RescheduleTaskOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get("task_id", "")
        if priority := params.get("priority", ""):
            endpoint = server + "/tasks/reschedule/%d/%d" % (task_id, priority)
        else:
            endpoint = server + "/tasks/reschedule/%d" % (task_id)

        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            return r.json()

        except Exception as e:
            self.logger.error(f"Error: {str(e)}")

    def test(self):
        out = self.connection.test()
        out["task_id"] = 0
        return out
