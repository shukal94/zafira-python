import json


def encode(filename, data):
    """
    Dumps python dict object to an json file.
    Uses in requests
    :param filename: name of payload file
    :param data: dict to write
    """
    with open(filename, 'w') as fp:
        json.dump(data, fp)


def decode(json_str):
    """
    Converts json response to a python dict object
    :param filename: name of payload file
    :return: dict with response data
    """
    return json.loads(json_str)
