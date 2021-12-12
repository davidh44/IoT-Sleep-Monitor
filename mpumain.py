import mpu6050
import time


def mpurun(results):
    mpu = mpu6050.mpu6050(0x68)

    tracker = []

    for i in range(28):
        gyro_data = mpu.get_gyro_data()
        gx = abs(gyro_data['x'])
        gy = abs(gyro_data['y'])
        gz = abs(gyro_data['z'])
        g = max([gx, gy, gz])
        tracker.append(g)
        print('Gyro: ' + str(g))
        time.sleep(.5)

    motion = max(tracker)
    results[2] = motion


