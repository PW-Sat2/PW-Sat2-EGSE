
class ConvertDict(object):
    @staticmethod
    def convert(data, conversion):
        converted_data = {}
        for key, value in data.iteritems():
            converted_data[key] = conversion[key](value)
        return converted_data
