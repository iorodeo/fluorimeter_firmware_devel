import constants
from count_measurement_screen import CountMeasurementScreen
from irradiance_measurement_screen import IrradianceMeasurementScreen
from light_sensor import LightSensorOverflow

class Measurement:

    NAME  = 'Measurment'
    LABEL = 'Label'
    UNITS = None

    def __init__(self, sensor_90, sensor_180):
        self.sensor_90  = sensor_90
        self.sensor_180 = sensor_180

    @property
    def name(self):
        return self.NAME

    @property
    def label(self):
        return self.LABEL

    @property
    def units(self):
        return self.UNITS

    @property
    def value(self):
        return 0.0

    @property
    def create_screen(self):
        return None


class RawCount(Measurement):
    
    NAME  = 'Raw Count'
    LABEL = 'Count @90', 'Count @180'

    @property
    def value(self): 
        try:
            value_90  = self.sensor_90.value
        except LightSensorOverflow:
            value_90 = constants.OVERFLOW_STR
        try:
            value_180 = self.sensor_180.value 
        except LightSensorOverflow:
            value_180 = constants.OVERFLOW_STR
        return value_90, value_180

    def create_screen(self):
        return CountMeasurementScreen()


class Irradiance(Measurement):

    NAME  = f'Irradiance'
    LABEL = f'{NAME} @90', f'{NAME} @180' 
    UNITS = f'{constants.MU}W/{constants.CM2}'

    @property
    def value(self):
        try:
            value_90 = self.sensor_90.irradiance
        except LightSensorOverflow:
            value_90 = constants.OVERFLOW_STR
        try:
            value_180 = self.sensor_180.irradiance
        except LightSensorOverflow:
            value_180 = constants.OVERFLOW_STR
        return value_90, value_180

    def create_screen(self): 
        return IrradianceMeasurementScreen()

class RelativeUnit(Measurement):

    NAME  = f'Relative Unit'
    LABEL = f'{NAME} @90'
    UNITS = f'{constants.MU}W/{constants.CM2}'

    @property
    def value(self):
        return 0.0

MEASUREMENTS = [RawCount, Irradiance, RelativeUnit]
NAME_TO_MEASUREMENT = {item.NAME:item for item in MEASUREMENTS}

def from_name(name, sensors):
    return NAME_TO_MEASUREMENT[name](*sensors)
