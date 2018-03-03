from test_result import TestResult
from prettytable import PrettyTable
from termcolor import colored
import datetime
import time
import pprint
import re

class Visualizer(object):

    @staticmethod
    def colour_result(result):
        if result == TestResult.PASS:
            return colored('[PASS]', 'white', 'on_green')
        elif result == TestResult.FAIL:
            return colored('[FAIL]', 'white', 'on_red')
        elif result == TestResult.ABORTED:
            return colored('[ABORTED]', 'white', 'on_cyan')


    @staticmethod
    def from_timestamp(timestamp):
        if timestamp != None:
            return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        else:
            return ""


    @staticmethod
    def test_result_name(item):
        if isinstance(item.result, type(dict())):
            name = '[ ] '
            name += colored(item.name, 'blue', 'on_white')
            name += '\n'
            for key, value in sorted(item.result.iteritems()):
                name += ' |-- ' + key + '\n'
            return name
        else:
            return item.name + '\n'


    @staticmethod
    def test_result(item):
        if isinstance(item.result, type(dict())):
            results = '\n'
            for key, value in sorted(item.result.iteritems()):
                results += Visualizer.colour_result(value) + '\n'
            return results
        else:
            return Visualizer.colour_result(item.result)


    @staticmethod
    def test_result_values_raw(item):
        if isinstance(item.data, type(dict())):
            results = '\n'
            for key, value in sorted(item.data.iteritems()):
                results += "{}\n".format(value.raw)
            return results
        else:
            return "{}\n".format(item.data.raw)


    @staticmethod
    def test_result_values_converted(item):
        if isinstance(item.data, type(dict())):
            results = '\n'
            for key, value in sorted(item.data.iteritems()):
                try:
                    unit = value.unit
                    if value.unit == None:
                        unit = ""
                except:
                    unit = ""

                try:
                    converted = "{:.2f}".format(value.converted)

                except:
                    converted = value.converted

                results += "{} {}\n".format(converted, unit)
            return results
        else:
            try:
                unit = item.data.unit
                if item.data.unit == None:
                    unit = ""
            except:
                unit = ""

            try:
                converted = "{:.2f}".format(item.data.converted)
            except:
                converted = item.data.converted

            return "{} {}\n".format(converted, unit)


    @staticmethod
    def build_results(results_table):
        table = PrettyTable(['#', 'Timestamp', 'Result', 'Name', 'Raw', 'Converted'])
        table.align["Name"] = "l"
        table.align["Raw"] = "l"
        table.align["Converted"] = "l"
        index = 0
        for item in results_table:
            table.add_row([index,
                           Visualizer.from_timestamp(item.timestamp), 
                           Visualizer.test_result(item), 
                           Visualizer.test_result_name(item),
                           Visualizer.test_result_values_raw(item),
                           Visualizer.test_result_values_converted(item)])
            index+=1
        return table


    @staticmethod
    def build_single_test_result(item):
        table = PrettyTable(['Result', 'Raw', 'Converted', 'Name'])
        table.align["Name"] = "l"
        table.align["Raw"] = "l"
        table.align["Converted"] = "l"
        table.add_row([Visualizer.test_result(item), 
                       Visualizer.test_result_values_raw(item), 
                       Visualizer.test_result_values_converted(item), 
                       Visualizer.test_result_name(item)])
        return table


    @staticmethod
    def build_test_list(loaded_list):
        table = PrettyTable(['#', 'Name', 'Description'])
        index = 0
        for item in loaded_list:
            table.add_row([index, item.name, item.description])
            index+=1
        return table


    @staticmethod
    def display_test_intro(number, test):
        print "\n\n"
        table = PrettyTable(['You are about running a test #{}.'.format(number)])
        table.align['You are about running a test #{}.'.format(number)] = "l"
        if len(test.kwargs) > 0:
            table.add_row([colored("{}".format(test.name), 'blue', 'on_white') + " with parameters:\n\n" + pprint.pformat(test.kwargs)])
        else:
            table.add_row(["{}. {}".format(number, test.name)])
        print table