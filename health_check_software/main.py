import argparse
import imp
import os
import sys

from helpers.console_prompt import MyPrompt
from traitlets.config.loader import Config
from IPython.terminal.embed import InteractiveShellEmbed
from helpers.gpio import DummyGPIO
from app.time_guard import TimeGuard
import threading
from test_framework.executor import Executor

import time

import logging
import colorlog
import serial
import datetime
import atexit

from tests.test_ping import TestPing
from tests.test_time import *
from tests.test_comm import TestCOMMReceiver, TestCOMMTransmitter
from tests.test_eps import *
from tests.test_fram import *
from tests.test_flash import *
from tests.test_photo import *
from tests.test_gyro import *
from tests.test_compile_info import *
from tests.test_mcu_temperature import *
from tests.test_lcls import *
from tests.test_ants import *
from tests.test_listfiles import *
from tests.test_imtq import *
from tests.test_suns import *
from tests.test_payload import *

from ranges.comm_telemetry_ranges import *
from ranges.eps_telemetry_ranges import *
from ranges.gyro_ranges import *


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', required=True,
                    help="Config file (in CMake-generated integration tests format, only MOCK_COM required)", )

args = parser.parse_args()

config = imp.load_source('config', args.config)

try:
    from obc import OBC, SerialPortTerminal
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../PWSat2OBC/integration_tests'))
    from obc import OBC, SerialPortTerminal


def _setup_log():
    root_logger = logging.getLogger()

    handler = colorlog.StreamHandler()

    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)-15s %(levelname)8s: [%(name)s] %(message)s",
        "%Y-%m-%d %H:%M:%S",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )


    formatter_file = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler.setFormatter(formatter)

    root_logger.addHandler(handler)


    hdlr = logging.FileHandler('{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
    hdlr.setFormatter(formatter_file)
    root_logger.addHandler(hdlr) 

    root_logger.setLevel(logging.DEBUG)
    logging.getLogger('OBCTerm').setLevel(logging.WARNING)
    logging.getLogger('TIME GUARD').setLevel(logging.WARNING)


obc = OBC(SerialPortTerminal(config.config['OBC_COM'], DummyGPIO()))
lock = threading.Lock()

_setup_log()

stop_event = threading.Event()
time_guard = TimeGuard(obc, lock)
time_guard_thread = threading.Thread(target=time_guard.run, args=())

to_do = [TestPing("Test Ping", "Test of ping command"),
         TestTimeBasic("Test Time Basic", "Test of time", time=datetime.timedelta(seconds=60)),
         TestRTCRange("Test RTC Range", "Test of RTC value", max_time=946784295000),
         TestCOMMReceiver("Test COMM Receiver", "Test of COMM Receiver Telemetry", ranges=receiver_telemetry_ranges),
         TestCOMMTransmitter(None, "Dupa", ranges=transmitter_telemetry_ranges),
         TestEPSA(None, None, ranges=eps_a_telemetry_ranges),
         TestEPSB(None, None, ranges=eps_b_telemetry_ranges),
         TestFRAM(),
         TestFLASH(),
         TestPhoto(None, None, path="C:/Users/begreen/Desktop/TestPhoto"),
         TestGyro(None, None, ranges=gyro_ranges),
         TestDuration(),
         TestCompileInfo(),
         TestMcuTemperature(),
         TestLCL_ANTS(),
         TestLCL_SENS(),
         TestLCL_CAMwing(),
         TestLCL_CAMnadir(),
         TestLCL_SunS(),
         TestLCL_iMTQ(),
         TestANTSTelemetry(),
         TestANTSStatusPrimary(),
         TestANTSStatusSecondary(),
         TestListFiles(),
         TestIMTQSelfTest(),
         TestExperimentalSunSBasic(),
         TestExperimentalSunSValues(),
         TestLCL_RadFET(),
         TestPayload()]

executor = Executor(obc, lock)
executor.load_tests_list(to_do)

#executor.show_test_list()
#executor.run_single(0)
#executor.run_single(1)
#executor.show_results()
#executor.run_range(0, 1)
#executor.run_all()
#executor.show_results()

cfg = Config()
shell = InteractiveShellEmbed(config=cfg, user_ns={'time_guard_thread' : time_guard_thread, 'obc': obc, 'end' : time_guard.stop, 'executor' : executor}, banner2='PW-Sat2 Health Check')
shell.prompts = MyPrompt(shell)
#shell.run_code('time_guard_thread.start()')
shell()
