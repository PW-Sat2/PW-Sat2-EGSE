from time import gmtime, strftime
import sys, os
from visualizer import Visualizer
from test_result import TestResult
from prettytable import PrettyTable
import datetime
import time
import pprint
import re
import pypandoc


def raw_input(text):
    sys.stdout.write(text)
    return sys.stdin.readline().strip()


class Reporter(object):
    def to_markdown_table(self, pt):
        """
        Print a pretty table as a markdown table
        
        :param py:obj:`prettytable.PrettyTable` pt: a pretty table object.  Any customization
          beyond int and float style may have unexpected effects
        
        :rtype: str
        :returns: A string that adheres to git markdown table rules
        """
        _junc = pt.junction_char
        if _junc != "|":
            pt.junction_char = "|"
        markdown = [row[1:-1] for row in pt.get_string().split("\n")[1:-1]]
        pt.junction_char = _junc
        return "\n".join(markdown)


    def text_result(self, result):
        if result == TestResult.PASS:
            return '[PASS]'
        elif result == TestResult.FAIL:
            return '[FAIL]'
        elif result == TestResult.ABORTED:
            return '[ABORTED]'


    def build_single_test_result(self, item):
        table = PrettyTable(['Result', 'Raw', 'Converted', 'Name'])
        table.align["Name"] = "l"
        table.align["Raw"] = "l"
        table.align["Converted"] = "l"
        table.add_row([self.test_result(item), 
                       Visualizer.test_result_values_raw(item), 
                       Visualizer.test_result_values_converted(item), 
                       self.test_result_name(item)])
        return table


    def test_result(self, item):
        if isinstance(item.result, type(dict())):
            results = '\n'
            for key, value in sorted(item.result.iteritems()):
                results += self.text_result(value) + '\n'
            return results
        if isinstance(item.result, type(list())):
            results = '\n'
            for value in item.result:
                results += self.text_result(value[1]) + '\n'
            return results
        else:
            return self.text_result(item.result)


    def test_result_name(self, item):
        if isinstance(item.result, type(dict())):
            name = item.name
            name += '\n'
            for key, value in sorted(item.result.iteritems()):
                name += key + '\n'
            return name
        elif isinstance(item.result, type(list())):
            name = item.name
            name += '\n'
            for item_data in item.result:
                name += item_data[0] + '\n'
            return name
        else:
            return item.name + '\n'


    def test_description(self):
        self.title = raw_input("Title: ")
        self.description = raw_input("Description: ")
        self.place = raw_input("Place: ")
        self.members = raw_input("Members: ")


    def generate(self, results_table, path, name):
        self.file = open(path + '/' + name + '.md', 'a')
        self.file.write('# {}\n\n'.format(self.title))

        self.file.write('* Date:\n{}\n'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
        self.file.write('* Place:\n{}\n'.format(self.place))
        self.file.write('* Members:\n{}\n\n'.format(self.members))
        self.file.write('**Description:**\n{}\n\n\n'.format(self.description))

        count = 0
        for item in results_table:
            self.file.write('## {}. {}\n\n'.format(count, item.name))
            self.file.write('{} | {}\n\n'.format(Visualizer.from_timestamp(item.timestamp), item.description))
            count += 1
            self.file.write(self.to_markdown_table(self.build_single_test_result(item)))
            self.file.write('\n\n')

        self.file.close()
        self.generate_pdf(path, name)

    def generate_pdf(self, path, name):
        output = pypandoc.convert_file('{}/{}.md'.format(path, name), 'pdf', outputfile="{}/{}.pdf".format(path, name), format='markdown_github')
        print(output)
