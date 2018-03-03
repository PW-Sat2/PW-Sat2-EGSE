import sys
import time
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.convert_dict import *

class TestIMTQSelfTest(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test iMTQ"
        self.default_description = "Performs iMTQ self-test"


    def test_script(self):
        self.result = {}
        self.data = {}
        ret = self.obc.enable_lcl(7)
        self.log.debug("OBC response LCL enable: {}".format(ret))
        time.sleep(5)

        test_result = self.obc.perform_self_test()
        self.log.debug("OBC response: {}".format(test_result))

        ret = self.obc.disable_lcl(7)
        self.log.debug("OBC response LCL disable: {}".format(ret))

        self.result['INIT'] = TestCompare.assert_equal(test_result[0][0], 0)
        self.result['+X'] = TestCompare.assert_equal(test_result[1][0], 0)
        self.result['-X'] = TestCompare.assert_equal(test_result[2][0], 0)
        self.result['+Y'] = TestCompare.assert_equal(test_result[3][0], 0)
        self.result['-Y'] = TestCompare.assert_equal(test_result[4][0], 0)
        self.result['+Z'] = TestCompare.assert_equal(test_result[5][0], 0)
        self.result['-Z'] = TestCompare.assert_equal(test_result[6][0], 0)
        self.result['FINA'] = TestCompare.assert_equal(test_result[7][0], 0)

        self.data['INIT'] = ResultData(test_result[0], None, None)
        self.data['+X'] = ResultData(test_result[1], None, None)
        self.data['-X'] = ResultData(test_result[2], None, None)
        self.data['+Y'] = ResultData(test_result[3], None, None)
        self.data['-Y'] = ResultData(test_result[4], None, None)
        self.data['+Z'] = ResultData(test_result[5], None, None)
        self.data['-Z'] = ResultData(test_result[6], None, None)
        self.data['FINA'] = ResultData(test_result[7], None, None)