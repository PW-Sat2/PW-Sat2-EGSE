from prettytable import PrettyTable
from termcolor import colored
import datetime
import sys
from test_result import TestResult
import time
from visualizer import Visualizer
import copy
import logging


def raw_input(text):
    sys.stdout.write(text)
    return sys.stdin.readline().strip()


class Executor(object):
    def __init__(self, obc, lock):
        self.results_table = []
        self.obc = obc
        self.lock = lock
        self.loaded_list = []
        self.execution_queue = []
        self.log = logging.getLogger()


    def load_tests_list(self, test_list):
        self.loaded_list = test_list

    def show_test_list(self):
        print(Visualizer.build_test_list(self.loaded_list))

    def show_results(self):
        print(Visualizer.build_results(self.results_table))


    def statistics(self):
        failed = 0
        passed = 0
        aborted = 0

        for item in self.results_table:
            if item.result == TestResult.FAIL:
                failed+=1
            elif item.result == TestResult.PASS:
                passed+=1
            elif item.result == TestResult.ABORTED:
                aborted+=1
        return {'passed' : passed, 'failed' : failed, 'aborted' : aborted}


    def run_confirmation(self, number, test):
        user = None
        Visualizer.display_test_intro(number, test)

        while True:
            user = raw_input(colored("Type: c to continue, a to abort: ", 'white', 'on_blue'))

            if user  == 'a':
                print colored("Aborted test: {}. {}".format(number, test.name), 'white', 'on_red')
                print "\n\n"
                return False
            elif user == 'c':
                return True
                '''
                user = raw_input(colored("Are you sure? Type: Yes or No: ", 'white', 'on_blue'))
                if user == 'Yes':
                    print "\n\n"
                    return True
                elif user == 'No':
                    print colored("Aborted test: {}. {}".format(number, test.name), 'white', 'on_red')
                    print "\n\n"
                    return False
                else:
                    print "Start over..."
                '''


    def run_single(self, number):
        if (len(self.loaded_list) - 1 < number):
            self.log.error("Incorrect test number: {}/{}".format(number, len(self.loaded_list) - 1))
        else:
            current = copy.copy(self.loaded_list[number])
            if self.run_confirmation(number, current):
                try:
                    current.run(self.obc, self.lock)
                    self.results_table.append(current)
                    print("")
                    print(Visualizer.build_single_test_result(current))
                    print("")
                except:
                    self.log.error("Exception in test!")



    def run_range(self, start, stop):
        num = start
        while num != stop + 1:
            self.run_single(num)
            if num != stop:
                user = raw_input("Press \'r\' to repeat test, or any other key to proceed with next tests ({} more in the queue)".format(stop-num))
            else:
                user = raw_input("Press \'r\' to repeat test, or any other key to finish")

            if user != 'r':
                num += 1


    def run_all(self):
        self.run_range(0, len(self.loaded_list) - 1)