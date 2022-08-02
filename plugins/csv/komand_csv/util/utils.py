import csv
import json
import re
from io import StringIO


def csv_syntax_good(csv_string):
    parsed = parse_csv_string(csv_string)
    size = len(parsed[0])
    return all(len(row) == size for row in parsed)


def fields_syntax_good(fields):
    re_single = r"\s*f[0-9]+\s*"
    re_range = f"{re_single}(-{re_single})?"
    re_multi = f"{re_range}(,{re_range})*"
    pattern = re.compile(f"^{re_multi}$")
    return bool(pattern.match(fields))


##
# Converts field to integer
# Ex. 'f2' -> 2
#
# @param field String of field
# @return integer representation of fiele
##
def field_to_number(field):
    if field.startswith("f"):
        field = field[1:]
    return int(field)


##
# Converts fields string to list of integers corresponding to position of field
#
# @param fields String of fields to keep
# @return List containing integers to reference position of each field
##
def get_field_list(fields, num_fields):
    field_split = fields.split(",")
    field_list = []
    safe_range = range(1, num_fields + 1)

    for f in field_split:
        f = f.strip()
        if "-" in f:
            start, end = f.split("-")
            start = field_to_number(start.strip())
            end = field_to_number(end.strip())
            if start < 1 or start not in safe_range or end not in safe_range:
                return None
            field_list.extend(range(start, end + 1))
        else:
            n = field_to_number(f)
            if n not in safe_range:
                return None
            field_list.append(field_to_number(f))
    field_list.sort()
    return field_list


##
# Converts CSV string to two-dimensional list
#
# @param csv The string to parse
# @return Two-dimensional list consisting of items on each line of CSV string
##
def parse_csv_string(csv_string):
    csv_list = csv_string.split("\n")
    return [line.split(",") for line in csv_list if line != ""]


##
# Converts the two-dimensional CSV array back to string form
#
# @param csv The two-dimensional array of the original CSV string
# @return The string of the CSV
##
def convert_csv_array(csv_array):
    item_delim = ","
    line_delim = "\n"
    lines = [item_delim.join(line) for line in csv_array]

    return line_delim.join(lines)


##
# Keeps specified positions in the list (1-indexed) of the line from CSV string
#
# @param line The list representing all of the items on the line of the CSV
# @param fields The list containing the indexes of the fields to keep
# @return The list of the line with only the specified remaining fields
##
def keep_fields(line, fields):
    return [line[field - 1] for field in fields]


##
# Converts a CSV string to a list of dictionariea
#
# @param csv The string of the CSV
# @return List of dictionaries
##
def csv_to_dict(s, action):
    # Create array of CSV rows
    csv_list = s.split("\n")

    # Create list from CSV header (first line)
    try:
        if len(csv_list) > 0:
            header = [csv_list[0]]
            action.logger.info("Header: %s, Length: %s", header, len(header))
    except Exception as e:
        action.logger.error("Element 0 doesn't exist in array")
        action.logger.error(f"Exception: {str(e)}")
        raise

    # Skip first line to get data
    try:
        if len(csv_list) > 0:
            first_row = [csv_list[1]]
            action.logger.info("Sample Data: %s, Length: %s", first_row, len(first_row))
    except Exception as e:
        action.logger.error("Element 1 doesn't exist in array")
        action.logger.error(f"Exception: {str(e)}")
        raise

    csv_data = csv.DictReader(csv_list)
    return [json.loads(json.dumps(row)) for row in csv_data]


def json_to_csv(input_json: dict) -> str:
    output = StringIO()
    csv_writer = csv.writer(output)
    keys = []

    # get all keys from json
    for entry in input_json:
        keys.extend(list(entry.keys()))

    if keys := list(dict.fromkeys(keys)):
        csv_writer.writerow(keys)
        for entry in input_json:
            for key in keys:
                entry[key] = entry.get(key, "")
            csv_writer.writerow(entry.values())

    return output.getvalue()
