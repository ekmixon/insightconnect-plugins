import requests
import json


class Connector:
    def __init__(self, rest_url, action):
        self._token = ""
        self._url = f"{rest_url}/restapi/v1/"
        self._verify = False
        self._headers = {"Content-type": "application/json"}
        self._status_code = 0
        self.logger = action.logger

    def set_token(self, token):
        self._token = token

    def raise_error_when_not_in_status(self, status_code):
        if self._status_code != status_code:
            self.raise_error(f"Wrong returned status - {str(self._status_code)}")

    def get_code(self):
        return self._status_code

    def get_dict_from_params(self, params, names):
        values = {}
        for name in names:
            if name not in params:
                continue

            key = name
            if name == "address":
                name = "ip_address"
                key = "address"
            values[name] = params.get(key)

        return values

    def check_required_params(self, params, names):
        if not params:
            self.raise_error("Empty params")

        for name in names:
            if not params.get(name):
                self.raise_error(f"Required param: {name}")

    def raise_error(self, msg):
        self.logger.info(msg)
        raise Exception(msg)

    def request(self, action, method, params=None):
        r = {}
        action_url = self._url + action
        auth = None if self._token == "" else (self._token, "")
        try:
            if method == "post":
                r = requests.post(
                    action_url,
                    data=json.dumps(params),
                    verify=self._verify,
                    headers=self._headers,
                    auth=auth,
                )
            elif method == "get":
                r = requests.get(action_url, params=params, verify=self._verify, headers=self._headers, auth=auth)
            elif method == "put":
                r = requests.put(
                    action_url,
                    data=json.dumps(params),
                    verify=self._verify,
                    headers=self._headers,
                    auth=auth,
                )
            elif method == "delete":
                r = requests.delete(action_url, verify=self._verify, headers=self._headers, auth=auth)
        except Exception as e:
            Connector.raise_error(str(e))

        self._status_code = r.status_code

        return r.json()

    def post(self, action, params):
        return self.request(action, "post", params)

    def put(self, action, params):
        return self.request(action, "put", params)

    def get(self, action, params=None):
        return self.request(action, "get", params)

    def delete(self, action):
        return self.request(action, "delete")
