import json


def encode(dict):
    """
    Dumps python dict object to an json string.
    Uses in requests
    :param dict to convert
    :return: json str for request
    """
    return json.dumps(dict)


def decode(json_str):
    """
    Converts json response to a python dict object
    :param json_str: response body in json format
    :return: dict with response data
    """
    return json.loads(json_str)
