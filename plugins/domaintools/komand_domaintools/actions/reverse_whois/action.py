import komand
from .schema import ReverseWhoisInput, ReverseWhoisOutput

# Custom imports below
from komand_domaintools.util import util


class ReverseWhois(komand.Action):

    MODES = ["purchase", "quote"]

    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse_whois",
            description="Provides a list of domain names that share the same Registrant Information",
            input=ReverseWhoisInput(),
            output=ReverseWhoisOutput(),
        )

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        params["query"] = params.pop("terms")
        mode = params.get("mode")
        if mode and mode not in self.MODES:
            raise Exception(f'DomainTools: mode must be one of: {", ".join(self.MODES)}')

        return utils.make_request(self.connection.api.reverse_whois, **params)

    def test(self):
        """TODO: Test action"""
        return {}
