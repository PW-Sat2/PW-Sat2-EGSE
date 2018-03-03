import sys
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare

class TestMcuTemperature(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test MCU Temperature"
        self.default_description = "Checks MCU Converted temperature and shows raw temperature value"


    def test_script(self):
        result_converted = self.obc.mcu_temp()
        result_raw = self.obc.mcu_temp_raw()
        self.log.debug("OBC response: raw {}; converted {}".format(result_raw, result_converted))
        self.result = TestCompare.assert_between_closed_interval(18, result_converted['Temp'], 30)
        self.data = ResultData(result_raw['Temperature RAW'], result_converted['Temp'], "C")