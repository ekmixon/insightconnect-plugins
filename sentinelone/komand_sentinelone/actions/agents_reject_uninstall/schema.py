# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Reject uninstall requests for all agents matching the input filter"


class Input:
    FILTER = "filter"
    

class Output:
    AFFECTED = "affected"
    

class AgentsRejectUninstallInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "object",
      "title": "Filter JSON",
      "description": "Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents",
      "order": 1
    }
  },
  "required": [
    "filter"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentsRejectUninstallOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
