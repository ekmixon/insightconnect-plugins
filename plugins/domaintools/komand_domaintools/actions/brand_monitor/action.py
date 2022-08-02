import komand
from .schema import BrandMonitorInput, BrandMonitorOutput

# Custom imports below
from komand_domaintools.util import util


class BrandMonitor(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="brand_monitor",
            description="Searches across all new domain registrations worldwide",
            input=BrandMonitorInput(),
            output=BrandMonitorOutput(),
        )

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        return utils.make_request(self.connection.api.brand_monitor, **params)

    def test(self):
        """TODO: Test action"""
        return {}
