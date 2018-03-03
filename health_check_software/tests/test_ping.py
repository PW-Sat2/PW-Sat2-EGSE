import sys
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare

class TestPing(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Ping"
        self.default_description = "Basic OBC test - ping - pong"


    def test_script(self):
        result = self.obc.ping()
        self.log.debug("OBC response: {}".format(result))
        self.result = TestCompare.assert_equal(result, 'pong')
        self.data = ResultData(result, result, None)