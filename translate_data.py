
import requests

from urlListGenerator import url_list_generator
import mirea_parser

import numpy as np

def translate_data(table):
    dataset = {}

    for t in table:
        try:
            fio = t["fio"]
            marks_sum = sum(map(int, t["marks"].split())) + int(t["achievments"])
            dataset[fio] = marks_sum
        except ValueError:
            pass

    return dataset
