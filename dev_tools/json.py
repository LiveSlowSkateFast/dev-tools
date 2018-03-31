#!/usr/bin/env python3
"""Simple functions for working with JSON objects in Python"""
from __future__ import print_function

import json


def jdump(obj):
    """Convert a data object in pretty JSON format"""
    obj = json.dumps(obj, indent=4, sort_keys=True)
    return obj


def pprint(obj):
    """Print a data object in a pretty JSON format"""
    print(jdump(obj))


def save_json(obj, file_name):
    """Write a data object to a file in a pretty JSON format"""
    with open(file_name, 'w') as json_file:
        json_file.write(jdump(obj))


def load_json(file_name):
    """Load a JSON file as a data object"""
    with open(file_name) as f:
        return (json.load(f))