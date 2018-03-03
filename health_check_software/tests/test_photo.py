import sys
import datetime
sys.path.append('..')
from test_framework.test_result import TestResult, ResultData
from test_framework.single_test import SingleTest
from test_framework.compare import TestCompare
from helpers.unit_converters.fram_converter import *
from helpers.unit_converters.convert_dict import *
from helpers.timer import *

import re


class TestPhoto(SingleTest):
    def set_default_title_description(self):
        self.default_name = "Test Photo service"
        self.default_description = "Uses OBC photo command, downloads the pictures and saves as raw/jpg"


    def _find_in_file_list(self, file_list, name):
        for item in file_list:
            if item[0] == name:
                return True
        return False


    def _get_file_size(self, file_list, name):
        for item in file_list:
            if item[0] == name:
                return item[1]
        return -1


    def _download_photo(self, local_path, filename):
        data = self.obc.read_file('/' + filename)

        with open(local_path + '/' + filename + '.raw', 'wb') as f:
            f.write(data)

        result = []

        rem = data[4:]

        while len(rem) > 0:
            part = rem[0:512 - 6]

            result += part

            rem = rem[512:]
            rem = rem[0:]
        
        with open(local_path + '/' + filename + '.jpg', 'wb') as f:
            f.write(''.join(result))


    def test_script(self):
        self.result = {}
        self.data = {}
        timer = Timer(datetime.timedelta(seconds=5))
        step_no = 1

        # step 1 -- schedule photo
        self.log.debug("Schedule photo")
        timer.start()
        try:
            command_result = self.obc.photo()
        except:
            self.log.error("exception in photo")
            timer.stop()
        timer.stop()
        self.log.debug("OBC response - photo: {}".format(command_result))
        self.result['Schedule and take'] = TestCompare.assert_equal(command_result, 'Scheduling....Scheduled...Finished')
        self.data['Schedule and take'] = ResultData(command_result, command_result, None)

        # step 2 -- get list
        self.log.debug("Get file list")
        command_result = self.obc.list_files_with_sizes('/')
        self.log.debug("OBC response - file list: {}".format(command_result))

        names = ['p_wing128', 'p_nadir128', 'p_wing240', 'p_nadir240', 'p_wing480', 'p_nadir480']
        # step 3 -- look for files that should be present
        for name in names:
            self.result['File exist: {}'.format(name)] = TestCompare.assert_equal(self._find_in_file_list(command_result, name), True)

        # step 4 -- check files size
        for name in names:
            self.result['File size: {}'.format(name)] = TestCompare.assert_greater(self._get_file_size(command_result, name), 7)

        # step 5 -- download files
        for name in names:
            self.log.debug("Downloading {}".format(name))
            self._download_photo(self.kwargs['path'], name)