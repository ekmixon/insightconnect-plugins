import komand
from .schema import ConnectionSchema

# Custom imports below
import requests


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        service_address = params.get("service_address")
        api_key = params.get("api_key").get("secretKey")
        auth_headers = {"Authorization": api_key, "te_cookie": "remember"}
        if using_cloud_server := params.get("using_cloud_server"):
            self.url = f"https://{service_address}/tecloud/api/v1/file/"
        else:
            self.url = f"https://{service_address}:18194/tecloud/api/v1/file/"
        self.session = requests.session()
        self.session.headers.update(auth_headers)
        self.logger.info("Connect: Connecting...")
