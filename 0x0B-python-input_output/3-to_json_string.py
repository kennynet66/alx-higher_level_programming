#!/usr/bin/python3
import json
"""A function that returns the JSON representation of an object (string):"""

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    Args:
        my_obj - the json object
    """

    json.dumps(my_obj)
