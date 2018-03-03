import sys
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData, ResultDataDict
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.flash_converter import *
from helpers.unit_converters.convert_dict import *


import re


class TestFLASH(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test FLASH Memory"
        self.default_description = "Check ID of all FLASHes"


    def test_script(self):
        convert = ['ID Not Valid', 'ID Valid']
        result = self.obc.test_flash()
        self.log.debug("OBC response: {}".format(result))
        self.result = TestCompare.assert_equal_dict(result, 1)
        self.data = ConvertDict.convert(result, flash_conversion)
