import sys
import time
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.convert_dict import *

try:
    from emulator.beacon_parser.resistance_sensors import *
except ImportError:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../PWSat2OBC/integration_tests'))
    from emulator.beacon_parser.resistance_sensors import *


class TestPayload(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test of Payload board"
        self.default_description = "Performs test of all components located on payload PCB"

    def _lmt87_to_centigrades(self, raw):
        return (raw/4096.0*4100-2637)/-13.6

    def _rtd_to_centigrades(self, raw):
        return pt1000_res_to_temp((raw/4096.0*1000)/(1 - raw/4096.0))

    def _hk_voltage(self, raw):
        return raw/4096.0*2*4.10

    def _radfet_mos_voltage(self, raw):
        return raw*2.5/2**24

    def _radfet_diode_voltage(self, raw):
        return raw*2.5/2**24/2


    def test_script(self):
        self.result = {}
        self.data = {}
        ret = self.obc.enable_lcl(5)
        self.log.debug("OBC response LCL enable: {}".format(ret))
        time.sleep(2)

        res = self.obc.payload_whoami()
        self.log.debug("OBC response - payload_whoami: {}".format(res))
        self.result['Who Am I'] = TestCompare.assert_equal(res['Who Am I'], 83)
        self.data['Who Am I'] = ResultData(res['Who Am I'], None, None)


        res = self.obc.payload_housekeeping()
        self.log.debug("OBC response - payload_housekeeping: {}".format(res))

        self.result['HK INT 3V3D'] = TestCompare.assert_between_closed_interval(3.2, self._hk_voltage(res['INT 3V3D']), 3.4)
        self.data['HK INT 3V3D'] = ResultData(res['INT 3V3D'], self._hk_voltage(res['INT 3V3D']), 'V')

        self.result['HK OBC 3V3D'] = TestCompare.assert_between_closed_interval(3.2, self._hk_voltage(res['OBC 3V3D']), 3.4)
        self.data['HK OBC 3V3D'] = ResultData(res['OBC 3V3D'], self._hk_voltage(res['OBC 3V3D']), 'V')


        res = self.obc.payload_temps()

        self.log.debug("OBC response - payload_temps: {}".format(res))

        self.result['TEMP CAM Nadir'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['CAM Nadir']), 30)
        self.data['TEMP CAM Nadir'] = ResultData(res['CAM Nadir'], self._rtd_to_centigrades(res['CAM Nadir']), 'C')

        self.result['TEMP CAM Wing'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['CAM Wing']), 30)
        self.data['TEMP CAM Wing'] = ResultData(res['CAM Wing'], self._rtd_to_centigrades(res['CAM Wing']), 'C')

        self.result['TEMP SADS'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['SADS']), 25)
        self.data['TEMP SADS'] = ResultData(res['SADS'], self._rtd_to_centigrades(res['SADS']), 'C')

        self.result['TEMP Sail'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['Sail']), 25)
        self.data['TEMP Sail'] = ResultData(res['Sail'], self._rtd_to_centigrades(res['Sail']), 'C')

        self.result['TEMP Xn'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['Xn']), 25)
        self.data['TEMP Xn'] = ResultData(res['Xn'], self._rtd_to_centigrades(res['Xn']), 'C')

        self.result['TEMP Xp'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['Xp']), 25)
        self.data['TEMP Xp'] = ResultData(res['Xp'], self._rtd_to_centigrades(res['Xp']), 'C')

        self.result['TEMP Yn'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['Yn']), 25)
        self.data['TEMP Yn'] = ResultData(res['Yn'], self._rtd_to_centigrades(res['Yn']), 'C')

        self.result['TEMP Yp'] = TestCompare.assert_between_closed_interval(15, self._rtd_to_centigrades(res['Yp']), 25)
        self.data['TEMP Yp'] = ResultData(res['Yp'], self._rtd_to_centigrades(res['Yp']), 'C')

        self.result['TEMP Supply'] = TestCompare.assert_between_closed_interval(15, self._lmt87_to_centigrades(res['Supply']), 25)
        self.data['TEMP Supply'] = ResultData(res['Supply'], self._lmt87_to_centigrades(res['Supply']), 'C')



        res = self.obc.payload_photodiodes()

        self.log.debug("OBC response - payload_photodiodes: {}".format(res))

        self.result['Phd Xn'] = TestCompare.assert_between_closed_interval(80, res['Xn'], 500)
        self.data['Phd Xn'] = ResultData(res['Xn'], None, None)

        self.result['Phd Xp'] = TestCompare.assert_between_closed_interval(80, res['Xp'], 500)
        self.data['Phd Xp'] = ResultData(res['Xp'], None, None)

        self.result['Phd Yn'] = TestCompare.assert_between_closed_interval(80, res['Yn'], 500)
        self.data['Phd Yn'] = ResultData(res['Yn'], None, None)

        self.result['Phd Yp'] = TestCompare.assert_between_closed_interval(80, res['Yp'], 500)
        self.data['Phd Yp'] = ResultData(res['Yp'], None, None)


        res = self.obc.payload_suns()

        self.log.debug("OBC response - payload_suns: {}".format(res))

        self.result['SunS V1'] = TestCompare.assert_between_closed_interval(2400, res['V1'], 2900)
        self.data['SunS V1'] = ResultData(res['V1'], None, None)

        self.result['SunS V2'] = TestCompare.assert_between_closed_interval(2400, res['V2'], 2900)
        self.data['SunS V2'] = ResultData(res['V2'], None, None)

        self.result['SunS V3'] = TestCompare.assert_between_closed_interval(2400, res['V3'], 2900)
        self.data['SunS V3'] = ResultData(res['V3'], None, None)

        self.result['SunS V4'] = TestCompare.assert_between_closed_interval(2400, res['V4'], 2900)
        self.data['SunS V4'] = ResultData(res['V4'], None, None)

        self.result['SunS V5'] = TestCompare.assert_between_closed_interval(2600, res['V5'], 2900)
        self.data['SunS V5'] = ResultData(res['V5'], None, None)



        res = self.obc.payload_radfet_on()
        self.log.debug("OBC response - payload_radfet_on: {}".format(res))
        self.result['Radfet On Status'] = TestCompare.assert_equal(res['Status'], 255)
        self.data['Radfet On Status'] = ResultData(res['Status'], None, None)

        res = self.obc.payload_radfet_read()
        self.log.debug("OBC response - payload_radfet_read: {}".format(res))

        self.result['Radfet Temperature'] = TestCompare.assert_between_closed_interval(0.55, self._radfet_diode_voltage(res['Temperature']), 0.65)
        self.data['Radfet Temperature'] = ResultData(res['Temperature'], self._radfet_diode_voltage(res['Temperature']), 'V')

        self.result['Radfet Vth0'] = TestCompare.assert_between_closed_interval(2.0, self._radfet_mos_voltage(res['Vth0']), 2.3)
        self.data['Radfet Vth0'] = ResultData(res['Vth0'], self._radfet_mos_voltage(res['Vth0']), 'V')

        self.result['Radfet Vth1'] = TestCompare.assert_between_closed_interval(2.0, self._radfet_mos_voltage(res['Vth1']), 2.3)
        self.data['Radfet Vth1'] = ResultData(res['Vth1'], self._radfet_mos_voltage(res['Vth1']), 'V')

        self.result['Radfet Vth2'] = TestCompare.assert_between_closed_interval(2.0, self._radfet_mos_voltage(res['Vth2']), 2.3)
        self.data['Radfet Vth2'] = ResultData(res['Vth2'], self._radfet_mos_voltage(res['Vth2']), 'V')

        res = self.obc.payload_radfet_off()
        self.log.debug("OBC response - payload_radfet_off: {}".format(res))
        self.result['Radfet Off Status'] = TestCompare.assert_equal(res['Status'], 32)
        self.data['Radfet Off Status'] = ResultData(res['Status'], None, None)

        self.obc.disable_lcl(5)