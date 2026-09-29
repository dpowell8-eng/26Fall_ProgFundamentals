# main.py - reads the sensor and prints the values
# Needs hs3003.py uploaded to the board as well.
 
import time
from hs3003 import HS3003

sensor = HS3003()

while True:
    print("Please choose from the following options:")
    print("T - Temperature")
    print("H - Humidity")
    print("0 - Both")

    choice = input("Enter your choice: ")

    if choice == "T":
        t, h = sensor.read()
        print("Temp: {:.1f} C".format(t))

    elif choice == "H":
        t, h = sensor.read()
        print("Humidity: {:.1f} %".format(h))

    elif choice == "0":
        t, h = sensor.read()
        print("Temp: {:.1f} C".format(t))
        print("Humidity: {:.1f} %".format(h))
        time.sleep(2)