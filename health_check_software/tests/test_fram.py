import sys
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.fram_converter import *
from helpers.unit_converters.convert_dict import *

import re


class TestFRAM(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test FRAM Memory"
        self.default_description = "Check ID of all FRAMs"


    def test_script(self):
        self.result = {}
        collected_results = {}
        for i in range(0, 3):
            result = self.obc.fram_status(i)
            self.log.debug("OBC response - FRAM {}: {}".format(i, result))
            parsed_result = int(re.search("Status register=([0-9]+)", result).groups()[0])
            collected_results['FRAM {}'.format(i)] = parsed_result
            self.result['FRAM {}'.format(i)] = TestCompare.assert_equal(parsed_result, 0)
        self.data = ConvertDict.convert(collected_results, fram_conversion)
