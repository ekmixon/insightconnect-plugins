import regex
import base64
import tldextract
import validators
from datetime import datetime
from icon_extractit.util.util import Regex


def extract(provided_regex: str, provided_string: str, provided_file: str) -> list:
    matches = []
    if provided_string:
        matches = regex.findall(provided_regex, provided_string)
    elif provided_file:
        matches = regex.findall(provided_regex, base64.b64decode(provided_file.encode("utf-8")).decode("utf-8"))
    return list(dict.fromkeys(matches))


def extract_filepath(provided_regex: str, provided_string: str, provided_file: str) -> list:
    matches = []
    if provided_string:
        new_string = regex.sub(Regex.URL, "", provided_string)
        new_string = regex.sub(Regex.Date, "", new_string)
        matches = regex.findall(provided_regex, new_string)
    elif provided_file:
        new_file = base64.b64decode(provided_file.encode("utf-8")).decode("utf-8")
        new_file = regex.sub(Regex.URL, "", new_file)
        new_file = regex.sub(Regex.Date, "", new_file)
        matches = regex.findall(provided_regex, new_file)
    return list(dict.fromkeys(matches))


def strip_subdomains(matches: list) -> list:
    for match in enumerate(matches):
        stripped_domain = tldextract.extract(match[1])
        matches[match[0]] = ".".join(stripped_domain[1:3])
    return list(dict.fromkeys(matches))


def clear_domains(matches: list) -> list:
    return [
        match[1].split("/")[0]
        for match in enumerate(matches)
        if not match[1].endswith("@")
    ]


def clear_urls(matches: list) -> list:
    return [
        match[1]
        for match in enumerate(matches)
        if not validators.ip_address.ipv4(match[1])
        and not validators.email(match[1])
    ]


def clear_emails(matches: list) -> list:
    return [match[1] for match in enumerate(matches) if validators.email(match[1])]


def parse_time(dates: list) -> list:
    for date in enumerate(dates):
        date_time_obj = datetime.strptime(date[1], "%d/%m/%Y")
        dates[date[0]] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
    return dates
