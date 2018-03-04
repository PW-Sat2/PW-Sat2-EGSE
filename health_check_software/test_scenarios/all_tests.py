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
from tests.test_solar_cells import *

from ranges.comm_telemetry_ranges import *
from ranges.eps_telemetry_ranges import *
from ranges.gyro_ranges import *

tests_queue =   [TestPing(),
                 TestEPSA(None, None, ranges=eps_a_telemetry_ranges),
                 TestEPSB(None, None, ranges=eps_b_telemetry_ranges),
                 TestTimeBasic(None, None, time=datetime.timedelta(seconds=60)),
                 TestRTCRange(None, None, max_time=946784295000),
                 TestCOMMReceiver(None, None, ranges=receiver_telemetry_ranges),
                 TestCOMMTransmitter(None, None, ranges=transmitter_telemetry_ranges),
                 TestCompileInfo(),
                 TestMcuTemperature(),
                 TestDuration(),
                 TestFRAM(),
                 TestFLASH(),
                 TestListFiles(),
                 TestGyro(None, None, ranges=gyro_ranges),
                 TestLCL_iMTQ(),
                 TestLCL_ANTS(),
                 TestLCL_SENS(),
                 TestLCL_CAMwing(),
                 TestLCL_CAMnadir(),
                 TestLCL_SunS(),
                 TestANTSTelemetry(),
                 TestANTSStatusPrimary(),
                 TestANTSStatusSecondary(),
                 TestIMTQSelfTest(),
                 TestExperimentalSunSBasic(),
                 TestExperimentalSunSValues(),
                 TestPhoto(None, None, path=""),
                 TestLCL_RadFET(),
                 TestPayload(),
                 TestSolarCells()]