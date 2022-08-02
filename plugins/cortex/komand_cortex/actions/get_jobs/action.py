import komand
from .schema import GetJobsInput, GetJobsOutput

# Custom imports below
import requests


class GetJobs(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_jobs",
            description="List of analysis jobs",
            input=GetJobsInput(),
            output=GetJobsOutput(),
        )

    def run(self, params={}):
        """TODO: Run action"""
        url = f"{self.connection.url}/api/job"

        l = []

        for i in params.keys():
            if isinstance(params[i], int) and params[i] > 0:
                l.append(i)
                continue
            if isinstance(params[i], str) and params[i].isalpha():
                l.append(i)

        self.logger.info("Inputs: %s", l)

        if l:
            url = f"{url}?"
            for opt in l:
                # self.logger.info(url)
                url = f"{url}{opt}={params.get(opt)}&"
            url = url.rstrip("&")
        self.logger.info(url)

        try:
            resp = requests.get(url)
            try:
                out = resp.json()
            except ValueError:
                self.logger.error(resp.content.decode())
                raise
        except ValueError:
            self.logger.error("No JSON returned")
            raise ValueError
        except:
            raise

        return {"list": out} if out else {"list": [{}]}

    def test(self):
        """TODO: Test action"""
        client = self.connection.client

        try:
            url = f"{self.connection.url}/api/job"
            out = requests.get(url).json()
        except:
            raise

        return {"list": out}
