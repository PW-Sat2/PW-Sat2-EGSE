try:
    from emulator.beacon_parser.units import MappedValue
    from emulator.beacon_parser.parser import CategoryParser
except ImportError:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../PWSat2OBC/integration_tests'))
    from emulator.beacon_parser.units import MappedValue
    from emulator.beacon_parser.parser import CategoryParser


fram_conversion = {'FRAM 0': MappedValue.with_values({-1: 'ID Not Valid', 0: 'ID Valid'}),
                             'FRAM 1': MappedValue.with_values({-1: 'ID Not Valid', 0: 'ID Valid'}),
                             'FRAM 2': MappedValue.with_values({-1: 'ID Not Valid', 0: 'ID Valid'})}
