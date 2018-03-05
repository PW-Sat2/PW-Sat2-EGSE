import sys
import time
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.convert_dict import *
from test_framework.executor import raw_input

from helpers.unit_converters.eps_telemetry_converter import *
from helpers.unit_converters.convert_dict import *
from helpers.unit_converters.eps_to_dict import * 


class TestSolarCells(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Solar Cells"
        self.default_description = "Check voltage and current on solar cells. Additionally get currents of photodiodes."

    def test_script(self):
        self.data = []
        axis = raw_input("Type name of the axis: ")
        print("Press Ctrl-C to finish")

        res = self.obc.enable_lcl(5)
        time.sleep(3)
        self.log.debug("OBC response: PLD LCL on {}".format(res))
        try:
            format_string = "{0:<5} [V] | {1:<5} [A] | {2:<5} [A] || {3:<5} [V] | {4:<5} [A] | {5:<5} [A] || {6:<5} [V] | {7:<5} [A] | {8:<5} [A] || {9:<5} [V] | {10:<5} [A] | {11:<5} [A]".format("PV Xp", "PV Xp", "Ph Xp", "PV Xn", "PV Xn", "Ph Xn", "PV Yp", "PV Yp", "Ph Yp", "PV Yn", "PV Yn", "Ph Yn")
            self.log.debug(format_string)
            self.data.append(("", ResultData(format_string, "", None)))
            while True:
                self.obc.jump_to_time(0)
                payload_response_data = self.obc.payload_photodiodes()
                eps_response_data = ControllerA.to_dict(self.obc.read_housekeeping_a())
                converted_eps_data = ConvertDict.convert(eps_response_data, eps_a_telemetry_conversion)
                format_string = "{0:<9} | {1:<9} | {2:<9} || {3:<9} | {4:<9} | {5:<9} || {6:<9} | {7:<9} | {8:<9} || {9:<9} | {10:<9} | {11:<9}".format(
                    converted_eps_data['MPPT_X.SOL_VOLT'].converted,converted_eps_data['MPPT_X.SOL_CURR'].converted, payload_response_data['Xn'],
                    converted_eps_data['MPPT_X.SOL_VOLT'].converted, converted_eps_data['MPPT_X.SOL_CURR'].converted, payload_response_data['Xp'],
                    converted_eps_data['MPPT_Y_PLUS.SOL_VOLT'].converted, converted_eps_data['MPPT_Y_PLUS.SOL_CURR'].converted, payload_response_data['Yn'],
                    converted_eps_data['MPPT_Y_MINUS.SOL_VOLT'].converted, converted_eps_data['MPPT_Y_MINUS.SOL_CURR'].converted, payload_response_data['Yp'])
                self.log.debug(format_string)
                self.data.append((time.time(), ResultData(format_string, "", None)))
                time.sleep(0.5)
        except:
            res = self.obc.disable_lcl(5)
            self.log.debug("OBC response: PLD LCL off {}".format(res))
            self.log.debug("Finished")
            while True:
                result = raw_input("Result of the test - type pass or fail: ")
                if result == 'pass' or result == 'fail':
                    self.result = [(axis, TestCompare.assert_equal(result, 'pass'))]
                    break