import komand
from .schema import BanFileInput, BanFileOutput

# Custom imports below
import json


class BanFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ban_file",
            description="Ban file globally or by policy",
            input=BanFileInput(),
            output=BanFileOutput(),
        )

    def run(self, params={}):
        file_hash = params.get("hash")
        policy_ids = params.get("policy_ids")
        ban_method = params.get("method").lower()  # globally, policy

        self.logger.info(f"Banning with {ban_method} method")

        data = {
            "hash": file_hash,
            "fileState": 3,
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
