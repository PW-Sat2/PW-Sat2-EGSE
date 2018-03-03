import sys
import time
sys.path.append('..')
from test_framework.test_result import TestResult
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.eps_telemetry_converter import *
from helpers.unit_converters.convert_dict import *
from helpers.unit_converters.eps_to_dict import * 


class TestLCL_ANTS(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test LCL ANTS"
        self.default_description = "Turns on and off ANTS LCL and checks parameters"

    def test_script(self):
        response_data_previous = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.enable_lcl(6)
        self.log.debug("LCL enable - OBC response: {}".format(res))

        time.sleep(5)

        response_data_after = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.disable_lcl(6)
        self.log.debug("LCL disable - OBC response: {}".format(res))

        self.log.debug("Response data previous: {}".format(response_data_previous))
        self.log.debug("Response data after: {}".format(response_data_after))

        self.result, self.data = TestCompare.assert_dict_differentially(response_data_previous, response_data_after,
            [('BATC.DCHRG_CURR', "<", 0.05),
             ('BATC.VOLT_A', ">", -0.2),
             ('DISTR.CURR_5V', "<>", 0.015, 0.05),
             ('DISTR.LCL_STATE', "=", 2**(6-1))])


class TestLCL_iMTQ(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test LCL iMTQ"
        self.default_description = "Turns on and off iMTQ LCL and checks parameters"

    def test_script(self):
        response_data_previous = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.enable_lcl(7)
        self.log.debug("LCL enable - OBC response: {}".format(res))

        time.sleep(5)

        response_data_after = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.disable_lcl(7)
        self.log.debug("LCL disable - OBC response: {}".format(res))

        self.log.debug("Response data previous: {}".format(response_data_previous))
        self.log.debug("Response data after: {}".format(response_data_after))

        self.result, self.data = TestCompare.assert_dict_differentially(response_data_previous, response_data_after,
            [('BATC.DCHRG_CURR', "<", 0.15),
             ('BATC.VOLT_A', ">", -0.2),
             ('DISTR.CURR_5V', "<>", 0.03, 0.15),
             ('DISTR.CURR_3V3', "<>", 0.00, 0.05),
             ('DISTR.LCL_STATE', "=", 2**(7-1))])


class TestLCL_SENS(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test LCL SENS"
        self.default_description = "Turns on and off SENS LCL and checks parameters"

    def test_script(self):
        response_data_previous = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.enable_lcl(5)
        self.log.debug("LCL enable - OBC response: {}".format(res))
        
        time.sleep(5)

        response_data_after = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.disable_lcl(5)
        self.log.debug("LCL disable - OBC response: {}".format(res))

        self.log.debug("Response data previous: {}".format(response_data_previous))
        self.log.debug("Response data after: {}".format(response_data_after))

        self.result, self.data = TestCompare.assert_dict_differentially(response_data_previous, response_data_after,
            [('BATC.DCHRG_CURR', "<", 0.05),
             ('BATC.VOLT_A', ">", -0.2),
             ('DISTR.CURR_5V', "<>", 0.010, 0.04),
             ('DISTR.LCL_STATE', "=", 2**(5-1))])


class TestLCL_RadFET(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test LCL SENS + RadFET"
        self.default_description = "Turns on and off SENS + RadFET LCL and checks parameters"

    def test_script(self):
        response_data_previous = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.enable_lcl(5)
        self.log.debug("LCL enable - OBC response: {}".format(res))
        time.sleep(2)
        res = self.obc.payload_radfet_on()
        self.log.debug("radfet enable - OBC response: {}".format(res))
        time.sleep(2)

        response_data_after = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.disable_lcl(5)
        self.log.debug("LCL disable - OBC response: {}".format(res))

        self.log.debug("Response data previous: {}".format(response_data_previous))
        self.log.debug("Response data after: {}".format(response_data_after))

        self.result, self.data = TestCompare.assert_dict_differentially(response_data_previous, response_data_after,
            [('BATC.DCHRG_CURR', "<", 0.05),
             ('BATC.VOLT_A', ">", -0.2),
             ('DISTR.CURR_5V', "<>", 0.020, 0.05),
             ('DISTR.LCL_STATE', "=", 2**(5-1))])



class TestLCL_CAMwing(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test LCL CAMwing"
        self.default_description = "Turns on and off CAMwing LCL and checks parameters"

    def test_script(self):
        response_data_previous = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.enable_lcl(4)
        self.log.debug("LCL enable - OBC response: {}".format(res))
        
        time.sleep(5)

        response_data_after = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.disable_lcl(4)
        self.log.debug("LCL disable - OBC response: {}".format(res))

        self.log.debug("Response data previous: {}".format(response_data_previous))
        self.log.debug("Response data after: {}".format(response_data_after))

        self.result, self.data = TestCompare.assert_dict_differentially(response_data_previous, response_data_after,
            [('BATC.DCHRG_CURR', "<", 0.1),
             ('BATC.VOLT_A', ">", -0.2),
             ('DISTR.CURR_3V3', "<>", 0.05, 0.15),
             ('DISTR.LCL_STATE', "=", 2**(4-1))])


class TestLCL_CAMnadir(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test LCL CAMnadir"
        self.default_description = "Turns on and off CAMnadir LCL and checks parameters"

    def test_script(self):
        response_data_previous = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.enable_lcl(3)
        self.log.debug("LCL enable - OBC response: {}".format(res))
        
        time.sleep(5)

        response_data_after = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.disable_lcl(3)
        self.log.debug("LCL disable - OBC response: {}".format(res))

        self.log.debug("Response data previous: {}".format(response_data_previous))
        self.log.debug("Response data after: {}".format(response_data_after))

        self.result, self.data = TestCompare.assert_dict_differentially(response_data_previous, response_data_after,
            [('BATC.DCHRG_CURR', "<", 0.1),
             ('BATC.VOLT_A', ">", -0.2),
             ('DISTR.CURR_3V3', "<>", 0.05, 0.15),
             ('DISTR.LCL_STATE', "=", 2**(3-1))])


class TestLCL_SunS(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test LCL SunS"
        self.default_description = "Turns on and off SunS LCL and checks parameters"

    def test_script(self):
        response_data_previous = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.enable_lcl(2)
        self.log.debug("LCL enable - OBC response: {}".format(res))
        
        time.sleep(5)

        response_data_after = ConvertDict.convert(ControllerA.to_dict(self.obc.read_housekeeping_a()), eps_a_telemetry_conversion)
        res = self.obc.disable_lcl(2)
        self.log.debug("LCL disable - OBC response: {}".format(res))

        self.log.debug("Response data previous: {}".format(response_data_previous))
        self.log.debug("Response data after: {}".format(response_data_after))

        self.result, self.data = TestCompare.assert_dict_differentially(response_data_previous, response_data_after,
            [('BATC.DCHRG_CURR', "<", 0.04),
             ('BATC.VOLT_A', ">", -0.2),
             ('DISTR.CURR_3V3', "<>", 0.010, 0.04),
             ('DISTR.LCL_STATE', "=", 2**(2-1))])
