class Gyro(object):
    @staticmethod
    def to_dict(gyro):
        gyro_dict = {}
        gyro_dict['X'] = int(gyro[0])
        gyro_dict['Y'] = int(gyro[1])
        gyro_dict['Z'] = int(gyro[2])
        gyro_dict['Temperature'] = int(gyro[3])
        return gyro_dict
