import sys
sys.path.append('..')
from test_framework.test_result import TestResult
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.eps_telemetry_converter import *
from helpers.unit_converters.convert_dict import *
from helpers.unit_converters.eps_to_dict import * 


class TestEPSA(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test EPS A HK"
        self.default_description = "Basic EPS A housekeeping check"

    def test_script(self):
        response_data = ControllerA.to_dict(self.obc.read_housekeeping_a())
        self.log.debug("OBC response: {}".format(response_data))
        self.data = ConvertDict.convert(response_data, eps_a_telemetry_conversion)
        self.result = TestCompare.assert_within_closed_interval_dict_converted(self.data, self.kwargs['ranges'])


class TestEPSB(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test EPS B HK"
        self.default_description = "Basic EPS B housekeeping check"

    def test_script(self):
        response_data = ControllerB.to_dict(self.obc.read_housekeeping_b())
        self.log.debug("OBC response: {}".format(response_data))
        self.data = ConvertDict.convert(response_data, eps_b_telemetry_conversion)
        self.result = TestCompare.assert_within_closed_interval_dict_converted(self.data, self.kwargs['ranges'])



'''
class TestPV(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Photovoltaics"
        self.default_description = "Test Photovoltaic Modules, Photodiodes and Thermometers"

    def test_script(self):
        response_data = ControllerA.to_dict(self.obc.read_housekeeping_a())
        self.log.debug("OBC response: {}".format(response_data))
        self.data = ResultData("OK", "OK", None)
        self.result = 
'''