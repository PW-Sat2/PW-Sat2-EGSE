from enum import Enum

class TestResult(Enum):
    PASS = 1
    FAIL = 2
    ABORTED = 3


class ResultData(object):
    def __init__(self, raw, converted, unit):
        self.raw = raw
        self.converted = converted
        self.unit = unit


def ResultDataDict(raw_dict, converted_dict):
    out = {}
    for key, value in sorted(raw_dict.iteritems()):
        out[key] = ResultData(value, converted_dict[key], None)
    return out