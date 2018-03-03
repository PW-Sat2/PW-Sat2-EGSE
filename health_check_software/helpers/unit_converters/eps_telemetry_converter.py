try:
    from emulator.beacon_parser.units import TelemetryUnit, unit, BoolType, TimeFromSeconds, MappedValue, PlainNumber
    from parser import CategoryParser
except ImportError:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../PWSat2OBC/integration_tests'))
    from emulator.beacon_parser.units import TelemetryUnit, unit, BoolType, TimeFromSeconds, MappedValue, PlainNumber
    from emulator.beacon_parser.eps_controller_a_telemetry_parser import *
    from emulator.beacon_parser.eps_controller_b_telemetry_parser import *
    from emulator.beacon_parser.parser import CategoryParser


eps_a_telemetry_conversion = {'BATC.CHRG_CURR': DistributionCurrent,
                             'BATC.DCHRG_CURR': DistributionCurrent,
                             'BATC.STATE': PlainNumber,
                             'BATC.TEMP': LMT87Temperature,
                             'BATC.VOLT_A': BATCVoltage,
                             'BP.TEMP_A': TMP121Temperature,
                             'BP.TEMP_B': TMP121Temperature,
                             'CTRLA.PWR_CYCLES': PlainNumber,
                             'CTRLA.SAFETY_CTR': PlainNumber,
                             'CTRLA.SUPP_TEMP': LMT87Temperature,
                             'CTRLA.TEMP': LMT87Temperature,
                             'CTRLA.UPTIME': TimeFromSeconds,
                             'CTRLB.VOLT_3V3d': Local3V3dVoltage,
                             'DCDC3V3.TEMP': LMT87Temperature,
                             'DCDC5V.TEMP': LMT87Temperature,
                             'DISTR.CURR_3V3': DistributionCurrent,
                             'DISTR.CURR_5V': DistributionCurrent,
                             'DISTR.CURR_VBAT': DistributionCurrent,
                             'DISTR.LCL_FLAGB': PlainNumber,
                             'DISTR.LCL_STATE': PlainNumber,
                             'DISTR.VOLT_3V3': DistributionVoltage,
                             'DISTR.VOLT_5V': DistributionVoltage,
                             'DISTR.VOLT_VBAT': DistributionVoltage,
                             'MPPT_X.SOL_CURR': MPPTCurrent,
                             'MPPT_X.SOL_OUT_VOLT': MPPTVoltage,
                             'MPPT_X.SOL_VOLT': MPPTVoltage,
                             'MPPT_X.STATE': PlainNumber,
                             'MPPT_X.TEMP': MPPTTemperature,
                             'MPPT_Y_MINUS.SOL_CURR': MPPTCurrent,
                             'MPPT_Y_MINUS.SOL_OUT_VOLT': MPPTVoltage,
                             'MPPT_Y_MINUS.SOL_VOLT': MPPTVoltage,
                             'MPPT_Y_MINUS.STATE': PlainNumber,
                             'MPPT_Y_MINUS.TEMP': MPPTTemperature,
                             'MPPT_Y_PLUS.SOL_CURR': MPPTCurrent,
                             'MPPT_Y_PLUS.SOL_OUT_VOLT': MPPTVoltage,
                             'MPPT_Y_PLUS.SOL_VOLT': MPPTVoltage,
                             'MPPT_Y_PLUS.STATE': PlainNumber,
                             'MPPT_Y_PLUS.TEMP': MPPTTemperature}

eps_b_telemetry_conversion = {'BP.TEMP_C' : PT1000Temperature,
                            'BATC.VOLT_B' : BATCVoltage,
                            'CTRLB.SAFETY_CTR' : PlainNumber,
                            'CTRLB.PWR_CYCLES' : PlainNumber,
                            'CTRLB.UPTIME' : TimeFromSeconds,
                            'CTRLB.TEMP' : LMT87Temperature,
                            'CTRLB.SUPP_TEMP' : LMT87Temperature,
                            'CTRLA.VOLT_3V3d' : Local3V3dVoltage}