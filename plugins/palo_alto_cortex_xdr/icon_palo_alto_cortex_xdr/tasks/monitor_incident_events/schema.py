# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Monitor incident events"


class Input:
    DESCRIPTIONS = "descriptions"
    INCIDENT_ID_LIST = "incident_id_list"
    STATUS = "status"
    TIME_SORTING_FIELD = "time_sorting_field"
    

class State:
    LAST_EVENT_TIME = "last_event_time"
    

class Output:
    EVENTS = "events"
    

class MonitorIncidentEventsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "descriptions": {
      "type": "array",
      "title": "Descriptions",
      "description": "Descriptions",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "incident_id_list": {
      "type": "array",
      "title": "Incident ID List",
      "description": "Incident ID list",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "enum": [
        "any",
        "new",
        "under_investigation",
        "resolved_threat_handled",
        "resolved_known_issue",
        "resolved_false_positive",
        "resolved_other",
        "resolved_auto"
      ],
      "order": 1
    },
    "time_sorting_field": {
      "type": "string",
      "title": "Time Sorting Field",
      "description": "Field to use to sort Incident events",
      "enum": [
        "modification_time",
        "creation_time"
      ],
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorIncidentEventsState(insightconnect_plugin_runtime.State):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "last_event_time": {
      "type": "string",
      "title": "Last Event Time",
      "description": "The datetime of the last retrieved incident event",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorIncidentEventsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "events": {
      "type": "array",
      "title": "Incident Events",
      "description": "Incident events",
      "items": {
        "$ref": "#/definitions/incident"
      },
      "order": 1
    }
  },
  "definitions": {
    "incident": {
      "type": "object",
      "title": "incident",
      "properties": {
        "alert_count": {
          "type": "integer",
          "title": "Alert Count",
          "description": "Alert count",
          "order": 1
        },
        "assigned_user_mail": {
          "type": "string",
          "title": "Assigned User Mail",
          "description": "Assigned user mail",
          "order": 2
        },
        "assigned_user_pretty_name": {
          "type": "string",
          "title": "Assigned User Pretty Name",
          "description": "Assigned user pretty name",
          "order": 3
        },
        "creation_time": {
          "type": "integer",
          "title": "Creation Time",
          "description": "Creation time",
          "order": 4
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 5
        },
        "detection_time": {
          "type": "string",
          "title": "Detection Time",
          "description": "Detection time",
          "order": 6
        },
        "high_severity_alert_count": {
          "type": "integer",
          "title": "High Severity Alert Count",
          "description": "High severity alert count",
          "order": 7
        },
        "host_count": {
          "type": "integer",
          "title": "Host Count",
          "description": "Host count",
          "order": 8
        },
        "hosts": {
          "type": "array",
          "title": "Hosts",
          "description": "Hosts",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "incident_id": {
          "type": "string",
          "title": "Incident ID",
          "description": "Incident ID",
          "order": 10
        },
        "incident_name": {
          "type": "string",
          "title": "Incident Name",
          "description": "Incident name",
          "order": 11
        },
        "incident_sources": {
          "type": "array",
          "title": "Incident Sources",
          "description": "Incident sources",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "low_severity_alert_count": {
          "type": "integer",
          "title": "Low Severity Alert Count",
          "description": "Low severity alert count",
          "order": 13
        },
        "manual_description": {
          "type": "string",
          "title": "Manual Description",
          "description": "Manual description",
          "order": 14
        },
        "manual_score": {
          "type": "string",
          "title": "Manual Score",
          "description": "Manual score",
          "order": 15
        },
        "manual_severity": {
          "type": "string",
          "title": "Manual Severity",
          "description": "Manual severity",
          "order": 16
        },
        "med_severity_alert_count": {
          "type": "integer",
          "title": "Med Severity Alert Count",
          "description": "Med severity alert count",
          "order": 17
        },
        "modification_time": {
          "type": "integer",
          "title": "Modification Time",
          "description": "Modification time",
          "order": 18
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "description": "Notes",
          "order": 19
        },
        "resolve_comment": {
          "type": "string",
          "title": "Resolve Comment",
          "description": "Resolve comment",
          "order": 20
        },
        "rule_based_score": {
          "type": "string",
          "title": "Rule Based Score",
          "description": "Rule based score",
          "order": 21
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 22
        },
        "starred": {
          "type": "boolean",
          "title": "Starred",
          "description": "Starred",
          "order": 23
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 24
        },
        "user_count": {
          "type": "integer",
          "title": "User Count",
          "description": "User count",
          "order": 25
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "Users",
          "items": {
            "type": "string"
          },
          "order": 26
        },
        "xdr_url": {
          "type": "string",
          "title": "XDR URL",
          "description": "XDR URL",
          "order": 27
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
