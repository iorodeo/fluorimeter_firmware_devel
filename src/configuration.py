import os
import json
import constants
from collections import OrderedDict
from json_settings_file import JsonSettingsFile

class ConfigurationError(Exception):
    pass

class Configuration(JsonSettingsFile):

    FILE_TYPE = 'configuration'
    FILE_NAME = constants.CONFIGURATION_FILE
    LOAD_ERROR_EXCEPTION = ConfigurationError


    def __init__(self):
        super().__init__()

    def check(self):

        for sensor_name in ('sensor_90', 'sensor_180'):

            if sensor_name in self.data:
                # Check Gain
                gain_key = f'gain_{sensor_name}'
                try:
                    gain_str = self.data[gain_key]
                except KeyError:
                    error_msg = f'{self.FILE_TYPE} missing gain'
                    error_dict[gain_key] = error_msg
                else:
                    try:
                        gain = constants.STR_TO_GAIN[gain_str]
                    except KeyError:
                        error_msg = f'{self.FILE_TYPE} unknown gain {gain_str}'
                        error_dict[gain_key] = error_msg

                # Check integration time
                itime_key = f'itime_{sensor_name}'
                try:
                    itime_str = self.data[itime_key]
                except KeyError:
                    error_msg = f'{self.FILE_TYPE} missing integration time'
                    error_dict[item_key] = error_msg
                else:
                    try:
                        itime = constants.STR_TO_INTEGRATION_TIME[itime_str]
                    except KeyError:
                        error_msg = f'{self.FILE_TYPE} unknown integration time {itime_str}'
                        error_dict[itime_key] = error_msg

        # Remove configurations with errors
        for name in self.error_dict:
            del self.data[name]

    def itime(self, sensor_name):
        itime_key = f'itime_{sensor_name}'
        try:
            itime_str = self.data[itime_key]
        except KeyError:
            itime = None
        else:
            itime = constants.STR_TO_INTEGRATION_TIME[itime_str]
        return itime

    def gain(self, sensor_name):
        gain_key = f'gain_{sensor_name}'
        try:
            gain_str = self.data[gain_key]
        except KeyError:
            gain = None
        else:
            gain = constants.STR_TO_GAIN[gain_str]
        return gain

    @property
    def itime_sensor_90(self):
        return self.itime('sensor_90')

    @property
    def itime_sensor_180(self):
        return self.itime('sensor_180')

    @property
    def gain_sensor_90(self):
        return self.gain('sensor_90')

    @property
    def gain_sensor_180(self):
        return self.gain('sensor_180')

    @property
    def startup(self):
        return self.data.get('startup', None)



            
            
    
