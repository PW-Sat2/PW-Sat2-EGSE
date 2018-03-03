import sys
sys.path.append('..')
from test_framework.test_result import TestResult
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.comm_telemetry_converter import *
from helpers.unit_converters.convert_dict import *


class TestCOMMReceiver(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test COMM Receiver"
        self.default_description = "Basic COMM Receiver telemetry check"

        
    def test_script(self):
        response_data = self.obc.comm_get_receiver_telemetry()
        self.log.debug("OBC response: {}".format(response_data))
        self.result = TestCompare.assert_within_closed_interval_dict(response_data, self.kwargs['ranges'])
        self.data = ConvertDict.convert(response_data, receiver_telemetry_conversion)


class TestCOMMTransmitter(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test COMM Transmitter"
        self.default_description = "Basic COMM Transmitter telemetry check"


    def test_script(self):
        response_data = self.obc.comm_get_transmitter_telemetry()
        self.log.debug("OBC response: {}".format(response_data))
        self.result = TestCompare.assert_within_closed_interval_dict(response_data, self.kwargs['ranges'])
        self.data = ConvertDict.convert(response_data, transmitter_telemetry_conversion)