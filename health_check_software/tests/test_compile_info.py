import sys
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare

class TestCompileInfo(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Compile Info"
        self.default_description = "Basic OBC test - request compile info"


    def test_script(self):
        result = self.obc.compile_info()
        self.log.debug("OBC response: {}".format(result))
        self.result = TestCompare.assert_equal(result, 'Release Build from \'07208653\' branch: master\nMCU: FlightModel\nPayload: FlightModel\nMachine: FP-PC3266\nBuilt in C:/Jenkins/jobs/OBC/branches/master/workspace/build\nGCC:5.4.1 20160919 (release) [ARM/embedded-5-branch revision 240496] ')
        self.data = ResultData(result, None, None)