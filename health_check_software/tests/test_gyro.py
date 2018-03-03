import sys
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.gyro_to_dict import *
from helpers.unit_converters.gyro_converter import *
from helpers.unit_converters.convert_dict import *

class TestGyro(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Gyro"
        self.default_description = "Gyroscope init and read values"


    def test_script(self):
        self.result = {}
        self.data = {}

        test_result = self.obc.gyro_init()
        self.log.debug("OBC response: {}".format(test_result))
        self.result['Init'] = TestCompare.assert_equal(test_result, '')

        response = self.obc.gyro_read()
        dict_response = Gyro.to_dict(response)
        self.data = ConvertDict.convert(dict_response, gyro_conversion)
        self.result.update(TestCompare.assert_within_closed_interval_dict_converted(self.data, self.kwargs['ranges']))
        self.data.update({'Init': ResultData(test_result, test_result, None)})