import komand
from .schema import ConnectionSchema

# Custom imports below
import json
import requests


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        server = params.get("url")
        self.server = server

    def test(self):
        server = self.server
        endpoint = f"{server}/cuckoo/status"
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")
