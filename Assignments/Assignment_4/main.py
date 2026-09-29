import time
from hs3003 import HS3003

sensor = HS3003

while True:
    t, h =sensor.read()
    print("temp:{:.1f} C Humididty:{:.1f} %". fromat(t,h))
    time.sleep(2)