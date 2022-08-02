import komand
from .schema import QueryInput, QueryOutput


class Query(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query",
            description="Query block history information for address",
            input=QueryInput(),
            output=QueryOutput(),
        )

    def run(self, params={}):
        cidr = params.get("cidr")
        client = self.connection.client
        results = client.query(cidr)
        is_blocked = len(results) != False
        return {"result": results, "is_blocked": is_blocked}

    def test(self):
        """TODO: Test action"""
        return {}
