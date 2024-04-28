from smbus import SMBus

addr = 0x8 # Bus address
bus = SMBus(1) # indicates /dev/ic2-1
bus.write_byte(addr, 0x1) # Switch it ON
input("Press return to exit")
bus.write_byte(addr, 0x0) # Switch it ON
