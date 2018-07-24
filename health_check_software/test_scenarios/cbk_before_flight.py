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

tests_queue_integration = [
# OBC communication test
TestPing(),

# Critical EPS telemetry
TestEPSA(None, None, ranges=eps_a_telemetry_standard_ranges),
TestEPSB(None, None, ranges=eps_b_telemetry_standard_ranges),

# Critical time
TestTimeBasic(None, None, time=datetime.timedelta(seconds=60)),

# PLD prior to PV tests
TestLCL_SENS(),

# Critical test of Solar Cells
TestSolarCells(None),
TestSolarCells(None),
TestSolarCells(None),
TestSolarCells(None),

# Critical test of COMM
TestCOMMReceiver(None, None, ranges=receiver_telemetry_ranges),
TestCOMMTransmitter(None, None, ranges=transmitter_telemetry_ranges),

# Critial LCLs test
TestLCL_iMTQ(),
TestLCL_ANTS(),
TestLCL_CAMwing(),
TestLCL_CAMnadir(),
TestLCL_SunS(),

# Critical subsystems communication tests
#TestANTSTelemetry(),
TestANTSStatusPrimary(),
TestANTSStatusSecondary(),
TestIMTQSelfTest(),

# OBC tests
TestCompileInfo(),
TestMcuTemperature(),
TestDuration(),
TestFRAM(),
TestFLASH(),
TestListFiles(),

# Payload board tests
TestGyro(None, None, ranges=gyro_standard_ranges),
TestLCL_RadFET(),
TestPayload(),

# Experimental SunS Tests
TestExperimentalSunSBasic(),
TestExperimentalSunSValues(),

# Camera photo test
TestPhoto(None, None, path="D:/Documents/GitHub/PW-Sat2-EGSE/health_check_software/test_outputs/2018-07-24_CBK_Before_Flight/foto"),

# Critical EPS telemetry
TestEPSA(None, None, ranges=eps_a_telemetry_standard_ranges),
TestEPSB(None, None, ranges=eps_b_telemetry_standard_ranges)]