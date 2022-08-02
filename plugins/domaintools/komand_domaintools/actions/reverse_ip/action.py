import komand
from .schema import ReverseIpInput, ReverseIpOutput

# Custom imports below
from komand_domaintools.util import util


class ReverseIp(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_ip",
            description="Provides a list of domain names that share the same Internet host (i.e. the same IP address)",
            input=ReverseIpInput(),
            output=ReverseIpOutput(),
        )

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        return utils.make_request(self.connection.api.reverse_ip, **params)

    def test(self):
        """TODO: Test action"""
        return {}
