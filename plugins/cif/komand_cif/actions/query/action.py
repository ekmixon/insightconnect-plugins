import komand
from .schema import QueryInput, QueryOutput

# Custom imports below
import requests


class Query(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="query",
            description="Query for observables",
            input=QueryInput(),
            output=QueryOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        url = f"{self.connection.url}/observables"
        headers = {
            "Authorization": f"Token token={self.connection.api_token}",
            "Accept": "application/vnd.cif.v2+json",
            "Content-Type": "application/json",
        }

        # Normalize input parameters
        nolog = str(1) if params.get("nolog") == True else str(0)
        params["nolog"] = nolog
        if params.get("protocol") == "all":
            del params["protocol"]
        if params.get("otype") == "all":
            del params["otype"]
        for k in list(params.keys()):
            if not params[k]:
                del params[k]

        l = list(params.keys())
        self.logger.info("Inputs: %s", l)

        if l:
            url = f"{url}?"
            for opt in l:
                # Debugging
                # self.logger.info(url)
                url = f"{url}{opt}={params.get(opt)}&"
            url = url.rstrip("&")
        self.logger.info(url)

        try:
            r = requests.get(url, headers=headers, verify=self.connection.verify)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP error occurred. Error: {str(e)}")
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error(f"A network problem occurred. Error: {str(e)}")
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error(f"Timeout occurred. Error: {str(e)}")
            raise
        except requests.exceptions.TooManyRedirects as e:
            self.logger.error(f"Too many redirects! Error: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")
            raise

        # Debugging
        # self.logger.info(r.request.headers)
        data = r.json()
        mod_data = []
        for item in data:
            if "confidence" in item:
                item["confidence"] = float(item["confidence"])
            if isinstance(item["application"], str):
                format_app = [item["application"]]
                item["application"] = format_app
            mod_data.append(item)
        result = mod_data

        ## Remove None types to avoid schema failure
        # Iterate over list
        for obj in result:
            # Iterate over dict keys
            for k in obj:
                if obj[k] is None:
                    obj[k] = "None"

        return {"query": result}

    def test(self):
        url = f"{self.connection.url}/ping"
        headers = {
            "Authorization": f"Token token={self.connection.api_token}",
            "Accept": "application/vnd.cif.v2+json",
            "Content-Type": "application/json",
        }


        try:
            r = requests.get(url, headers=headers, verify=self.connection.verify)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP error occurred. Error: {str(e)}")
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error(f"A network problem occurred. Error: {str(e)}")
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error(f"Timeout occurred. Error: {str(e)}")
            raise
        except requests.exceptions.TooManyRedirects as e:
            self.logger.error(f"Too many redirects! Error: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")
            raise
        return {"query": [r.json()]}
