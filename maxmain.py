import max30102
import hrcalc


def maxrun(results):
    m = max30102.MAX30102()
    red, ir = m.read_sequential(350) # if nothing is passed, this reads 100 values
    hr, hr_valid, spo2, spo2_valid = hrcalc.calc_hr_and_spo2(ir, red)
    print('Heart Rate',hr)
    print('SP02',spo2)
    if hr_valid:
        results[0] = hr
    if spo2_valid:
        results[1] = spo2
    m.shutdown()



