import sys
import time
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.convert_dict import *
from test_framework.executor import raw_input

try:
    from emulator.beacon_parser.resistance_sensors import *
except ImportError:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../PWSat2OBC/integration_tests'))
    from emulator.beacon_parser.resistance_sensors import *


class TestExperimentalSunSBasic(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Experimental SunS"
        self.default_description = "Basic test to check if the sensor is alive"


    def test_script(self):
        self.result = {}
        self.data = {}
        ret = self.obc.enable_lcl(2)
        self.log.debug("OBC response LCL enable: {}".format(ret))
        time.sleep(5)

        test_result = self.obc.measure_suns(0, 100)
        self.log.debug("OBC response: {}".format(test_result))

        ret = self.obc.disable_lcl(2)
        self.log.debug("OBC response LCL disable: {}".format(ret))

        self.result['ALS ACK'] = TestCompare.assert_equal(test_result[0], 0)
        self.result['ALS presence'] = TestCompare.assert_equal(test_result[1], 4095)
        self.result['ALS adc_valid'] = TestCompare.assert_equal(test_result[2], 4095)

        self.data['ALS ACK'] = ResultData(test_result[0], None, None)
        self.data['ALS presence'] = ResultData(test_result[1], None, None)
        self.data['ALS adc_valid'] = ResultData(test_result[2], None, None)



class TestExperimentalSunSValues(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Experimental SunS - light test"
        self.default_description = "Check if readouts from the sensor varies with light"

    def _lm60_to_centigrades(self, raw):
        return (raw/1024.0*1225-424)/6.25

    def _rtd_to_centigrades(self, raw):
        return pt1000_res_to_temp((raw/1024.0*1000)/(1 - raw/1024.0))

    def test_script(self):
        self.result = {}
        self.data = {}
        ret = self.obc.enable_lcl(2)
        self.log.debug("OBC response LCL enable: {}".format(ret))
        time.sleep(5)

        dark = self.obc.measure_suns(0, 100)
        #dark = [0, 4095, 4095, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 475, 534, 534, 534, 532, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.log.debug("OBC response: {}".format(dark))
        self.log.debug("Waiting for user keystroke")

        while True:
            self.obc.jump_to_time(0)
            time.sleep(2)
            if raw_input("Direct a beam of light towards the sensor and press l...") == 'l':
                break

        light = self.obc.measure_suns(0, 100)
        #light = [0, 4095, 4095, 6396, 6218, 6742, 6580, 6371, 6290, 6458, 6538, 6446, 6317, 6397, 6583, 474, 534, 534, 534, 533, 0, 10, 9433, 8729, 9823, 9285, 9049, 8769, 9641, 9222, 9033, 8907, 9291, 9227]
        self.log.debug("OBC response: {}".format(light))
        ret = self.obc.disable_lcl(2)
        self.log.debug("OBC response LCL disable: {}".format(ret))

        self.result['STRUCT TEMP'] = TestCompare.assert_between_closed_interval(18, self._lm60_to_centigrades(light[15]), 25)
        self.result['TEMP A'] = TestCompare.assert_between_closed_interval(18, self._rtd_to_centigrades(light[16]), 25)
        self.result['TEMP B'] = TestCompare.assert_between_closed_interval(18, self._rtd_to_centigrades(light[17]), 25)
        self.result['TEMP C'] = TestCompare.assert_between_closed_interval(18, self._rtd_to_centigrades(light[18]), 25)
        self.result['TEMP D'] = TestCompare.assert_between_closed_interval(18, self._rtd_to_centigrades(light[19]), 25)


        self.data['STRUCT TEMP'] = ResultData(light[15], self._lm60_to_centigrades(light[15]), 'C')
        self.data['TEMP A'] = ResultData(light[16], self._rtd_to_centigrades(light[16]), 'C')
        self.data['TEMP B'] = ResultData(light[17], self._rtd_to_centigrades(light[17]), 'C')
        self.data['TEMP C'] = ResultData(light[18], self._rtd_to_centigrades(light[18]), 'C')
        self.data['TEMP D'] = ResultData(light[19], self._rtd_to_centigrades(light[19]), 'C')

        difference = [light - dark for light, dark in zip(light, dark)]
        self.log.debug("SunS difference: {}".format(difference))

        for i in range(0, 12):
            self.result['delta ALS VL {}'.format(i)] = TestCompare.assert_greater(difference[3:15][i], 100)
            self.result['delta ALS IR {}'.format(i)] = TestCompare.assert_greater(difference[22:34][i], 100)

            self.data['delta ALS VL {}'.format(i)] = ResultData(difference[3:15][i], None, None)
            self.data['delta ALS IR {}'.format(i)] = ResultData(difference[22:34][i], None, None)