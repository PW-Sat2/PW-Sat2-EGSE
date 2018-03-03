import sys
import time
import pprint
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.timer import *

import re

class TestTimeBasic(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Current Time"
        self.default_description = "Current time returned by OBC"


    def test_script(self):
        result = self.obc.current_time()
        self.log.debug("OBC response: {}".format(result))
        self.result = TestCompare.assert_less(result, self.kwargs['time'])
        self.data = ResultData(result, result, None)


class TestRTCRange(SingleTest):
    def _parse_rtc_info(self, rtc_info):
        return re.search("(.*)\(([0-9]+) sec since epoch\)\\r", rtc_info).groups()

    def set_default_title_description(self):
        self.default_name = "Test RTC Time"
        self.default_description = "Current time returned by RTC"

    def test_script(self):
        result = self.obc.rtc_info()
        self.log.debug("RTC response: {}".format(result))
        parsed_rtc_info = self._parse_rtc_info(result)
        self.log.debug("Parsed response: {}".format(parsed_rtc_info))
        self.result = TestCompare.assert_less(int(parsed_rtc_info[1]), self.kwargs['max_time'])
        self.data = ResultData(result.strip(), parsed_rtc_info[1], None)


class TestDuration(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Duration"
        self.default_description = "Tests RTC and OBC duration"

    def test_script(self):
        self.data = {}
        self.result = {}
        timer1 = Timer(datetime.timedelta(seconds=5))
        timer2 = Timer(datetime.timedelta(seconds=5))

        timer1.start()
        t_start_1 = self.obc.rtc_duration()
        self.log.debug("RTC response t_start_1: {}".format(t_start_1))
        self.log.debug("Waiting 1 minute")
        time.sleep(60)
        t_stop_1 = self.obc.rtc_duration()
        timer1.stop()
        self.log.debug("RTC response t_stop_1: {}".format(t_stop_1))
        timedelta_1 = t_stop_1 - t_start_1
        self.log.debug("RTC timedelta: {}".format(timedelta_1))


        timer2.start()
        t_start_2 = self.obc.current_time()
        self.log.debug("OBC time response t_start_2: {}".format(t_start_2))
        self.log.debug("Waiting 1 minute")
        time.sleep(60)
        t_stop_2 = self.obc.current_time()
        timer2.stop()
        self.log.debug("OBC time response t_stop_2: {}".format(t_stop_2))
        timedelta_2 = (t_stop_2 - t_start_2).total_seconds()
        self.log.debug("OBC timedelta: {}".format(timedelta_2))

        self.result['RTC duration'] = TestCompare.assert_between_closed_interval(55, timedelta_1, 65)
        self.result['OBC duration'] = TestCompare.assert_between_closed_interval(55, timedelta_2, 65)
        
        self.data['RTC duration'] = ResultData(timedelta_1, timedelta_1, 's')
        self.data['OBC duration'] = ResultData(timedelta_2, timedelta_1, 's')
