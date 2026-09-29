
def temperature():
    #read the temperature
    #display the temperature
    
class HS3003:
    def __init__(self, bus=None):
        if bus is None:
            bus = machine.I2C(1, scl=machine.Pin(15), sda=machine.Pin(14))
        self.bus = bus
           
    def _read_raw(self):
        self.bus.writeto(ADDR, b'') # ask the chip for a measurement
        time.sleep_ms(50) # give it time to finish
        return self.bus.readfrom(ADDR, 4)
     
    