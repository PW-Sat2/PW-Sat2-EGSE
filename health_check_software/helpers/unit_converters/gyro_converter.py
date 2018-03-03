try:
    from emulator.beacon_parser.units import TelemetryUnit, unit, BoolType, TimeFromSeconds, MappedValue, PlainNumber
    from parser import CategoryParser
except ImportError:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../PWSat2OBC/integration_tests'))
    from emulator.beacon_parser.units import TelemetryUnit, unit, BoolType, TimeFromSeconds, MappedValue, PlainNumber
    from emulator.beacon_parser.gyroscope_telemetry_parser import *
    from emulator.beacon_parser.parser import CategoryParser

gyro_conversion = {'X' : AngularRate,
                    'Y' : AngularRate,
                    'Z' : AngularRate,
                    'Temperature' : GyroTemperature}