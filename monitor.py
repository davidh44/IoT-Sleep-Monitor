from maxmain import maxrun
from mpumain import mpurun
from time import time
from datetime import datetime
from streamdata import upload_to_ts
from threading import Thread

first = True

while True:
    start = time()
    results = [None] * 3
    t1 = Thread(target=mpurun, args=(results,))
    t2 = Thread(target=maxrun, args=(results,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    hr = results[0]
    spo2 = results[1]
    motion = results[2]
    end = time()
    elapsed = end - start
    print('Time:' + str('{:.4f}'.format(elapsed)))
    upload_to_ts(hr, spo2, motion)

    if first:
        first = False
        with open("./sleep_readings.log", "w") as f:
            f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S') + ',' + str(hr) + ',' + str(spo2) + ',' + str(motion) + '\n')
    else:
        with open("./sleep_readings.log", "a") as f:
            f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S') + ',' + str(hr) + ',' + str(spo2) + ',' + str(motion) + '\n')





