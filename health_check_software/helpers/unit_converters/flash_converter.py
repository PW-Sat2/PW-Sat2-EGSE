try:
    from emulator.beacon_parser.units import MappedValue
    from emulator.beacon_parser.parser import CategoryParser
except ImportError:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../PWSat2OBC/integration_tests'))
    from emulator.beacon_parser.units import MappedValue
    from emulator.beacon_parser.parser import CategoryParser


flash_conversion = {'Flash 1': MappedValue.with_values({0: 'ID Not Valid', 1: 'ID Valid'}),
                             'Flash 2': MappedValue.with_values({0: 'ID Not Valid', 1: 'ID Valid'}),
                             'Flash 3': MappedValue.with_values({0: 'ID Not Valid', 1: 'ID Valid'})}
