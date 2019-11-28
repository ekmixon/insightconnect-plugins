# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Reverts the account policy to the tenant policy"


class Input:
    ACCOUNT_ID = "account_id"
    ID = "id"
    

class Output:
    SUCCESS = "success"
    

class AccountRevertPolicyInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_id": {
      "type": "string",
      "title": "Account ID",
      "description": "Account ID. Example 225494730938493804",
      "order": 1
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Reverted account ID",
      "order": 2
    }
  },
  "required": [
    "account_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AccountRevertPolicyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Indicates a successful operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
