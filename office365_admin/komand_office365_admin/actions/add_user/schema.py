# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add a user to Office365"


class Input:
    ACCOUNT_ENABLED = "account_enabled"
    DISPLAY_NAME = "display_name"
    FORCE_CHANGE_PASSWORD = "force_change_password"
    MAIL_NICKNAME = "mail_nickname"
    OFFICE_LOCATION = "office_location"
    PASSWORD = "password"
    USER_PRINCIPAL_NAME = "user_principal_name"
    

class Output:
    USER = "user"
    

class AddUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_enabled": {
      "type": "boolean",
      "title": "Account Enabled",
      "description": "If true, the account will be enabled",
      "order": 1
    },
    "display_name": {
      "type": "string",
      "title": "Display Name",
      "description": "The user's display name e.g. John Doe",
      "order": 2
    },
    "force_change_password": {
      "type": "boolean",
      "title": "Force Password Change",
      "description": "If true, the user will have to change their password at login",
      "order": 5
    },
    "mail_nickname": {
      "type": "string",
      "title": "Mail Nickname",
      "description": "The mail alias for the user",
      "order": 3
    },
    "office_location": {
      "type": "string",
      "title": "Office Location",
      "description": "User Office Location",
      "order": 7
    },
    "password": {
      "type": "string",
      "title": "Password",
      "displayType": "password",
      "description": "Set the user's password",
      "format": "password",
      "order": 6
    },
    "user_principal_name": {
      "type": "string",
      "title": "User Principal Name",
      "description": "The user principal name e.g. user@example.com",
      "order": 4
    }
  },
  "required": [
    "account_enabled",
    "display_name",
    "force_change_password",
    "mail_nickname",
    "password",
    "user_principal_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "type": "object",
      "title": "User",
      "description": "Return a user object in JSON format",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
