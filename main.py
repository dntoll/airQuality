# main.py -- put your code here!
# The MIT License (MIT)
# Copyright (c) 2018 Stephen Suffian

"""
import utime
import run_sds011

print("startup")
while True:
    utime.sleep(1)
    print('Attempt to Send')
    pm25, pm10 = run_sds011.run_sensor()
    print('Air Quality PM2.5: {}, PM10: {}'.format(pm25, pm10))
    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
"""
import time
from lib.bme import BME

sda = 'P7'
scl = 'P8'

bme = BME((sda, scl), calibration_time=5)

while True:
    # Get air condition values
    temp, humidity, pressure, air_quality = bme.get_values()

    # Print all
    print('Temperature:', temp, '°C')
    print('Humidity:', humidity, '%')
    print('pressure:', pressure, 'hPa')
    print('air_quality:', air_quality, 'IAQ')
    print()

    time.sleep(1)
