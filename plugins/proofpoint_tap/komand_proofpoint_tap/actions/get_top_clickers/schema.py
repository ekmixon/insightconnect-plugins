# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch the identities and attack index of the top clickers within your organization for a given period"


class Input:
    WINDOW = "window"
    

class Output:
    RESULTS = "results"
    

class GetTopClickersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "window": {
      "type": "integer",
      "title": "Window",
      "description": "An integer indicating how many days the data should be retrieved for",
      "enum": [
        14,
        30,
        90
      ],
      "order": 1
    }
  },
  "required": [
    "window"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTopClickersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/top_clickers",
      "title": "Results",
      "description": "The results containing top clickers",
      "order": 1
    }
  },
  "required": [
    "results"
  ],
  "definitions": {
    "click_statistics": {
      "type": "object",
      "title": "click_statistics",
      "properties": {
        "clickCount": {
          "type": "integer",
          "title": "Click Count",
          "description": "Click count",
          "order": 1
        },
        "families": {
          "type": "array",
          "title": "Families",
          "description": "Families",
          "items": {
            "$ref": "#/definitions/families"
          },
          "order": 2
        }
      },
      "definitions": {
        "families": {
          "type": "object",
          "title": "families",
          "properties": {
            "clicks": {
              "type": "integer",
              "title": "Clicks",
              "description": "Clicks",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            }
          }
        }
      }
    },
    "families": {
      "type": "object",
      "title": "families",
      "properties": {
        "clicks": {
          "type": "integer",
          "title": "Clicks",
          "description": "Clicks",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        }
      }
    },
    "identity": {
      "type": "object",
      "title": "identity",
      "properties": {
        "customerUserId": {
          "type": "string",
          "title": "Customer User ID",
          "description": "Customer user ID",
          "order": 2
        },
        "department": {
          "type": "string",
          "title": "Department",
          "description": "Department",
          "order": 5
        },
        "emails": {
          "type": "array",
          "title": "Emails",
          "description": "Emails",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "guid": {
          "type": "string",
          "title": "GUID",
          "description": "GUID",
          "order": 1
        },
        "location": {
          "type": "string",
          "title": "Location",
          "description": "Location",
          "order": 6
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 4
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title",
          "order": 7
        },
        "vip": {
          "type": "boolean",
          "title": "VIP",
          "description": "VIP",
          "order": 8
        }
      }
    },
    "top_clickers": {
      "type": "object",
      "title": "top_clickers",
      "properties": {
        "interval": {
          "type": "string",
          "title": "Interval",
          "description": "An ISO8601-formatted interval showing what time the response was calculated for",
          "order": 3
        },
        "totalTopClickers": {
          "type": "integer",
          "title": "Total Top Clickers",
          "description": "An integer describing the total number of top clickers in the time interval",
          "order": 2
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "An array of user objects that contain information about the user's identity and statistics of the clicking behavior",
          "items": {
            "$ref": "#/definitions/user"
          },
          "order": 1
        }
      },
      "definitions": {
        "click_statistics": {
          "type": "object",
          "title": "click_statistics",
          "properties": {
            "clickCount": {
              "type": "integer",
              "title": "Click Count",
              "description": "Click count",
              "order": 1
            },
            "families": {
              "type": "array",
              "title": "Families",
              "description": "Families",
              "items": {
                "$ref": "#/definitions/families"
              },
              "order": 2
            }
          },
          "definitions": {
            "families": {
              "type": "object",
              "title": "families",
              "properties": {
                "clicks": {
                  "type": "integer",
                  "title": "Clicks",
                  "description": "Clicks",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 1
                }
              }
            }
          }
        },
        "families": {
          "type": "object",
          "title": "families",
          "properties": {
            "clicks": {
              "type": "integer",
              "title": "Clicks",
              "description": "Clicks",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            }
          }
        },
        "identity": {
          "type": "object",
          "title": "identity",
          "properties": {
            "customerUserId": {
              "type": "string",
              "title": "Customer User ID",
              "description": "Customer user ID",
              "order": 2
            },
            "department": {
              "type": "string",
              "title": "Department",
              "description": "Department",
              "order": 5
            },
            "emails": {
              "type": "array",
              "title": "Emails",
              "description": "Emails",
              "items": {
                "type": "string"
              },
              "order": 3
            },
            "guid": {
              "type": "string",
              "title": "GUID",
              "description": "GUID",
              "order": 1
            },
            "location": {
              "type": "string",
              "title": "Location",
              "description": "Location",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 4
            },
            "title": {
              "type": "string",
              "title": "Title",
              "description": "Title",
              "order": 7
            },
            "vip": {
              "type": "boolean",
              "title": "VIP",
              "description": "VIP",
              "order": 8
            }
          }
        },
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "clickStatistics": {
              "$ref": "#/definitions/click_statistics",
              "title": "Click Statistics",
              "description": "Click statistics",
              "order": 2
            },
            "identity": {
              "$ref": "#/definitions/identity",
              "title": "Identity",
              "description": "Identity",
              "order": 1
            }
          },
          "definitions": {
            "click_statistics": {
              "type": "object",
              "title": "click_statistics",
              "properties": {
                "clickCount": {
                  "type": "integer",
                  "title": "Click Count",
                  "description": "Click count",
                  "order": 1
                },
                "families": {
                  "type": "array",
                  "title": "Families",
                  "description": "Families",
                  "items": {
                    "$ref": "#/definitions/families"
                  },
                  "order": 2
                }
              },
              "definitions": {
                "families": {
                  "type": "object",
                  "title": "families",
                  "properties": {
                    "clicks": {
                      "type": "integer",
                      "title": "Clicks",
                      "description": "Clicks",
                      "order": 2
                    },
                    "name": {
                      "type": "string",
                      "title": "Name",
                      "description": "Name",
                      "order": 1
                    }
                  }
                }
              }
            },
            "families": {
              "type": "object",
              "title": "families",
              "properties": {
                "clicks": {
                  "type": "integer",
                  "title": "Clicks",
                  "description": "Clicks",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 1
                }
              }
            },
            "identity": {
              "type": "object",
              "title": "identity",
              "properties": {
                "customerUserId": {
                  "type": "string",
                  "title": "Customer User ID",
                  "description": "Customer user ID",
                  "order": 2
                },
                "department": {
                  "type": "string",
                  "title": "Department",
                  "description": "Department",
                  "order": 5
                },
                "emails": {
                  "type": "array",
                  "title": "Emails",
                  "description": "Emails",
                  "items": {
                    "type": "string"
                  },
                  "order": 3
                },
                "guid": {
                  "type": "string",
                  "title": "GUID",
                  "description": "GUID",
                  "order": 1
                },
                "location": {
                  "type": "string",
                  "title": "Location",
                  "description": "Location",
                  "order": 6
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 4
                },
                "title": {
                  "type": "string",
                  "title": "Title",
                  "description": "Title",
                  "order": 7
                },
                "vip": {
                  "type": "boolean",
                  "title": "VIP",
                  "description": "VIP",
                  "order": 8
                }
              }
            }
          }
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "clickStatistics": {
          "$ref": "#/definitions/click_statistics",
          "title": "Click Statistics",
          "description": "Click statistics",
          "order": 2
        },
        "identity": {
          "$ref": "#/definitions/identity",
          "title": "Identity",
          "description": "Identity",
          "order": 1
        }
      },
      "definitions": {
        "click_statistics": {
          "type": "object",
          "title": "click_statistics",
          "properties": {
            "clickCount": {
              "type": "integer",
              "title": "Click Count",
              "description": "Click count",
              "order": 1
            },
            "families": {
              "type": "array",
              "title": "Families",
              "description": "Families",
              "items": {
                "$ref": "#/definitions/families"
              },
              "order": 2
            }
          },
          "definitions": {
            "families": {
              "type": "object",
              "title": "families",
              "properties": {
                "clicks": {
                  "type": "integer",
                  "title": "Clicks",
                  "description": "Clicks",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 1
                }
              }
            }
          }
        },
        "families": {
          "type": "object",
          "title": "families",
          "properties": {
            "clicks": {
              "type": "integer",
              "title": "Clicks",
              "description": "Clicks",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 1
            }
          }
        },
        "identity": {
          "type": "object",
          "title": "identity",
          "properties": {
            "customerUserId": {
              "type": "string",
              "title": "Customer User ID",
              "description": "Customer user ID",
              "order": 2
            },
            "department": {
              "type": "string",
              "title": "Department",
              "description": "Department",
              "order": 5
            },
            "emails": {
              "type": "array",
              "title": "Emails",
              "description": "Emails",
              "items": {
                "type": "string"
              },
              "order": 3
            },
            "guid": {
              "type": "string",
              "title": "GUID",
              "description": "GUID",
              "order": 1
            },
            "location": {
              "type": "string",
              "title": "Location",
              "description": "Location",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 4
            },
            "title": {
              "type": "string",
              "title": "Title",
              "description": "Title",
              "order": 7
            },
            "vip": {
              "type": "boolean",
              "title": "VIP",
              "description": "VIP",
              "order": 8
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
