import insightconnect_plugin_runtime
import time
from .schema import GetNewAlertsInput, GetNewAlertsOutput, Input, Output, Component
import datetime

# Custom imports below


class GetNewAlerts(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_alerts",
            description=Component.DESCRIPTION,
            input=GetNewAlertsInput(),
            output=GetNewAlertsOutput(),
        )

    def run(self, params={}):
        interval = params.get("interval", 10)
        now = datetime.datetime.now()

        query = "from siem.logtrust.alert.info select *"

        while True:
            time_ago = now - datetime.timedelta(seconds=interval)
            now = datetime.datetime.now()

            new_alerts_query_output = self.connection.api.query(query, time_ago.isoformat(), now.isoformat())
            if new_alerts := new_alerts_query_output.get("object", {}):
                self.logger.info("Alerts received, sending...")
                for alert in new_alerts:
                    cleaned_result = insightconnect_plugin_runtime.helper.clean(alert)
                    self.send({Output.ALERT: cleaned_result})
            else:
                self.logger.info("No new alerts found.")

            self.logger.info(f"Sleeping for {interval} seconds.\n")
            time.sleep(interval)
