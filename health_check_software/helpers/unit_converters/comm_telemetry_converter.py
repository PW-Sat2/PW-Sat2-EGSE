try:
    from emulator.beacon_parser.units import TelemetryUnit, unit, BoolType, TimeFromSeconds, MappedValue
    from parser import CategoryParser
except ImportError:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../PWSat2OBC/integration_tests'))
    from emulator.beacon_parser.units import TelemetryUnit, unit, BoolType, TimeFromSeconds, MappedValue
    from emulator.beacon_parser.comm_telemetry_parser import *
    from emulator.beacon_parser.parser import CategoryParser


receiver_telemetry_conversion = {'LastReceived Doppler': DopplerOffset,
                                 'LastReceived RSSI': SignalStrength,
                                 'Now Doppler': DopplerOffset,
                                 'Now Oscillator Temperature': CommTemperature,
                                 'Now Power Amp Temperature': CommTemperature,
                                 'Now Power Supply Voltage': Voltage,
                                 'Now RSSI': SignalStrength,
                                 'Now RX current': ReceiverCurrent,
                                 'Uptime': TimeFromSeconds}


BitrateMappedValue = MappedValue.with_values({1: '1200', 2: '2400', 3: '4800', 4: '9600'})
BitrateMappedValue.units = 'bps'

transmitter_telemetry_conversion = {'Beacon': MappedValue.with_values({0: 'Off', 1: 'On'}),
                                    'Bitrate': BitrateMappedValue,
                                    'Idle state': MappedValue.with_values({0: 'Off', 1: 'On'}),
                                    'LastTransmitted Power Amp Temperature': CommTemperature,
                                    'LastTransmitted RF Forward power': RFPower,
                                    'LastTransmitted RF Reflected power': RFPower,
                                    'LastTransmitted TX Current': TransmitterCurrent,
                                    'Now RF Forward power': RFPower,
                                    'Now TX Current': TransmitterCurrent,
                                    'Uptime': TimeFromSeconds}