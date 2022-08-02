import komand
from .schema import UnbanFileInput, UnbanFileOutput

# Custom imports below
import json


class UnbanFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unban_file",
            description="Unban file globally or by policy",
            input=UnbanFileInput(),
            output=UnbanFileOutput(),
        )

    def run(self, params={}):
        file_hash = params.get("hash")
        ban_method = params.get("method").lower()  # globally, policy
        policy_ids = params.get("policy_ids")
        new_state = params.get("new_state").lower()

        self.logger.info(
            f"Unbanning via {ban_method} method with new state of {new_state}"
        )


        data = {
            "hash": file_hash,
            "fileState": 1 if new_state is "unapproved" else 2,
            "policyIds": "0" if ban_method is "globally" else ",".join(str(i) for i in policy_ids),
        }

        url = f"{self.connection.host}/api/bit9platform/v1/fileRule"
        r = self.connection.session.post(url, json.dumps(data), verify=self.connection.verify)

        try:
            r.raise_for_status()
        except:
            raise Exception(f"Run: HTTPError: {r.text}")

        result = komand.helper.clean(r.json())

        return {"file_rule": result}

    def test(self):
        url = f"{self.connection.host}/api/bit9platform/v1/approvalRequest?limit=-1"

        request = self.connection.session.get(url=url, verify=self.connection.verify)

        try:
            request.raise_for_status()
        except:
            raise Exception(f"Run: HTTPError: {request.text}")

        return {}
