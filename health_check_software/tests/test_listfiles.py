import sys
import pprint
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare

class TestListFiles(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test List Files"
        self.default_description = "Checks whether file list can be returned"


    def test_script(self):
        try:
            res = self.obc.list_files_with_sizes('/')
            self.result = TestCompare.assert_equal(True, True)
            self.data = ResultData(pprint.pformat(res), None, None)
            self.log.debug("OBC response: {}".format(res))
        except:
            self.result = TestCompare.assert_equal(False, True)
            self.data = ResultData(None, None, None)
            self.log.debug("Exception!")
