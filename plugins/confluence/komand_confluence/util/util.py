def normalize_page(p):
    p["created"] = p["created"].value + "Z"
    p["modified"] = p["modified"].value + "Z"
    p["homePage"] = p["homePage"] != "false"
    p["current"] = p["current"] != "false"
    return p
