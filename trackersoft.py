import socket
import os
import threading
import time
from machine import I2C, Pin
import mpu6050

i2c = I2C(scl=Pin(5), sda=Pin(4))
accel = mpu6050.accel(i2c)

def calibrate(threshold=50, n_samples=100):
    """
    Get calibration date for the sensor, by repeatedly measuring
    while the sensor is stable. The resulting calibration
    dictionary contains offsets for this sensor in its
    current position.
    """
    while True:
        v1 = get_accel(n_samples)
        v2 = get_accel(n_samples)
        # Check all consecutive measurements are within
        # the threshold. We use abs() so all calculated
        # differences are positive.
        if all(abs(v1[key] - v2[key]) < threshold for key in v1.keys()):
            return v1  # Calibrated.


def get_smoothed_values(n_samples=10):
    """
    Get smoothed values from the sensor by sampling
    the sensor `n_samples` times and returning the mean.
    """
    result = {}
    for _ in range(samples):
        data = accel.get_values()

        for key in data.keys():
            # Add on value / samples (to generate an average)
            # with default of 0 for first loop.
            result[m] = result.get(m, 0) + (data[m] / samples)

    return result


calibration = calibrate()
while True:
    data = get_smoothed_values(n_samples=100, calibration=calibration)
    print('\t'.join('{0}:{1:>10.1f}'.format(k, data[k])
        for k in sorted(data.keys())),
    end='\r')

#def f():
 #   #while True:
  #  with open('atk.txt', 'w+') as fp:
#
 #       atk = fp.read()
  #      fp.close()
   #     time.sleep(10)


def server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 3456))
    s.listen(30)

    #while True:
     #   try:
      #      with open('atk.txt', 'r') as fp1:

       #         atk = fp1.read()
        #        fp1.close()
         #       print(atk)
          #      time.sleep(10)

        #except:
         #   with open('atk.txt', 'w+') as fp:

          #      atk = fp.read()
           #     fp.close()
            #    print(atk)
             #   time.sleep(10)

        clientsocket, adress = s.accept()
        print(f'Connection Established from {adress}')
        clientsocket.send(bytes(atk, 'utf-8'))


#server()

