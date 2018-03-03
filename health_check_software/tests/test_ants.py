import sys
import time
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare

class TestANTSTelemetry(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test ANTS Telemetry"
        self.default_description = "Checks ANTS Telemetry values"


    def test_script(self):
        self.result = {}
        self.data = {}

        res_lcl = self.obc.enable_lcl(6)
        self.log.debug("OBC response: LCL enable {}".format(res_lcl))
        time.sleep(5)
        res = self.obc.antenna_get_telemetry()
        res_lcl = self.obc.disable_lcl(6)
        self.log.debug("OBC response: LCL disable {}".format(res_lcl))

        self.result['ActivationCount'] = TestCompare.assert_equal(res.ActivationCount, [0, 0, 0, 0, 0, 0, 0, 0])
        self.result['ActivationTime'] = TestCompare.assert_equal(res.ActivationTime, [0, 0, 0, 0, 0, 0, 0, 0])
        self.data['ActivationCount'] = ResultData(res.ActivationCount, None, None)
        self.data['ActivationTime'] = ResultData(res.ActivationTime, None, None)
        self.log.debug("OBC response: ActivationCount {}; ActivationTime {}".format(res.ActivationCount, res.ActivationTime))


class TestANTSStatusPrimary(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test ANTS Primary Status"
        self.default_description = "Checks ANTS Primary Status values"


    def test_script(self):
        self.result = {}
        self.data = {}

        res_lcl = self.obc.enable_lcl(6)
        self.log.debug("OBC response: LCL enable {}".format(res_lcl))

        time.sleep(5)
        res = self.obc.antenna_get_status("primary")
        res_lcl = self.obc.disable_lcl(6)
        self.log.debug("OBC response: LCL disable {}".format(res_lcl))

        self.result['DeploymentInProgress'] = TestCompare.assert_equal(res.DeploymentInProgress, [0, 0, 0, 0])
        self.result['DeploymentState'] = TestCompare.assert_equal(res.DeploymentState, [0, 0, 0, 0])
        self.result['DeploymentTimeReached'] = TestCompare.assert_equal(res.DeploymentTimeReached, [0, 0, 0, 0])

        self.result['IgnoringSwitches'] = TestCompare.assert_equal(res.IgnoringSwitches, 0)
        self.result['IndependentBurn'] = TestCompare.assert_equal(res.IndependentBurn, 0)
        self.result['Status'] = TestCompare.assert_equal(res.Status, True)
        self.result['SystemArmed'] = TestCompare.assert_equal(res.SystemArmed, 0)


        self.data['DeploymentInProgress'] = ResultData(res.DeploymentInProgress, None, None)
        self.data['DeploymentState'] = ResultData(res.DeploymentState, None, None)
        self.data['DeploymentTimeReached'] = ResultData(res.DeploymentTimeReached, None, None)

        self.data['IgnoringSwitches'] = ResultData(res.IgnoringSwitches, None, None)
        self.data['IndependentBurn'] = ResultData(res.IndependentBurn, None, None)
        self.data['Status'] = ResultData(res.Status, None, None)
        self.data['SystemArmed'] = ResultData(res.SystemArmed, None, None)


class TestANTSStatusSecondary(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test ANTS Secondary Status"
        self.default_description = "Checks ANTS Secondary Status values"


    def test_script(self):
        self.result = {}
        self.data = {}

        res_lcl = self.obc.enable_lcl(6)
        self.log.debug("OBC response: LCL enable {}".format(res_lcl))

        time.sleep(5)
        res = self.obc.antenna_get_status("backup")
        res_lcl = self.obc.disable_lcl(6)
        self.log.debug("OBC response: LCL disable {}".format(res_lcl))

        self.result['DeploymentInProgress'] = TestCompare.assert_equal(res.DeploymentInProgress, [0, 0, 0, 0])
        self.result['DeploymentState'] = TestCompare.assert_equal(res.DeploymentState, [0, 0, 0, 0])
        self.result['DeploymentTimeReached'] = TestCompare.assert_equal(res.DeploymentTimeReached, [0, 0, 0, 0])

        self.result['IgnoringSwitches'] = TestCompare.assert_equal(res.IgnoringSwitches, 0)
        self.result['IndependentBurn'] = TestCompare.assert_equal(res.IndependentBurn, 0)
        self.result['Status'] = TestCompare.assert_equal(res.Status, True)
        self.result['SystemArmed'] = TestCompare.assert_equal(res.SystemArmed, 0)


        self.data['DeploymentInProgress'] = ResultData(res.DeploymentInProgress, None, None)
        self.data['DeploymentState'] = ResultData(res.DeploymentState, None, None)
        self.data['DeploymentTimeReached'] = ResultData(res.DeploymentTimeReached, None, None)

        self.data['IgnoringSwitches'] = ResultData(res.IgnoringSwitches, None, None)
        self.data['IndependentBurn'] = ResultData(res.IndependentBurn, None, None)
        self.data['Status'] = ResultData(res.Status, None, None)
        self.data['SystemArmed'] = ResultData(res.SystemArmed, None, None)