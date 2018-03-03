from test_result import TestResult, ResultData

class TestCompare(object):
    @staticmethod
    def assert_equal(x, y):
        if x == y:
            return TestResult.PASS
        else:
            return TestResult.FAIL


    @staticmethod
    def assert_less(x, y):
        if x < y:
            return TestResult.PASS
        else:
            return TestResult.FAIL


    @staticmethod
    def assert_greater(x, y):
        if x > y:
            return TestResult.PASS
        else:
            return TestResult.FAIL


    @staticmethod
    def assert_less_or_equal(x, y):
        if x <= y:
            return TestResult.PASS
        else:
            return TestResult.FAIL


    @staticmethod
    def assert_greater_or_equal(x, y):
        if x >= y:
            return TestResult.PASS
        else:
            return TestResult.FAIL


    @staticmethod
    def assert_between_open_interval(lower_boundary, test_value, higher_boundary):
        if test_value > lower_boundary and test_value < higher_boundary:
            return TestResult.PASS
        else:
            return TestResult.FAIL


    @staticmethod
    def assert_between_closed_interval(lower_boundary, test_value, higher_boundary):
        if test_value >= lower_boundary and test_value <= higher_boundary:
            return TestResult.PASS
        else:
            return TestResult.FAIL


    @staticmethod
    def assert_within_closed_interval_dict(test_dict, range_dict):
        result_dict = {}
        for key, value in sorted(test_dict.iteritems()):
            result_dict[key] = TestCompare.assert_between_closed_interval(range_dict[key][0], value, range_dict[key][1])
        return result_dict


    @staticmethod
    def assert_within_closed_interval_dict_converted(test_dict, range_dict):
        result_dict = {}
        for key, value in sorted(test_dict.iteritems()):
            result_dict[key] = TestCompare.assert_between_closed_interval(range_dict[key][0], value.converted, range_dict[key][1])
        return result_dict


    @staticmethod
    def assert_equal_dict(test_dict, const_value):
        result_dict = {}
        for key, value in sorted(test_dict.iteritems()):
            result_dict[key] = TestCompare.assert_equal(value, const_value)
        return result_dict


    @staticmethod
    def assert_dict_differentially(values_before, values_after, checks):
        result_dict = {}
        data_dict = {}
        for check in checks:
            diff_raw = values_after[check[0]].raw - values_before[check[0]].raw
            diff_converted = values_after[check[0]].converted - values_before[check[0]].converted

            res = None
            if check[1] == '>':
                res = TestCompare.assert_greater(diff_converted, check[2])
            elif check[1] == '<':
                res = TestCompare.assert_less(diff_converted, check[2])
            elif check[1] == '<>':
                res = TestCompare.assert_between_open_interval(check[2], diff_converted, check[3])
            elif check[1] == '=':
                res = TestCompare.assert_equal(diff_converted, check[2])
            else:
                raise ValueError('Wrong comparision symbol')

            result_dict[check[0]] = res

            try:
                unit = values_after[check[0]].unit
            except:
                unit = ""

            data_dict[check[0]] = ResultData(diff_raw, diff_converted, unit)

        return [result_dict, data_dict]