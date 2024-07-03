from pymodbus.client.serial import ModbusSerialClient
from pymodbus.transaction import ModbusAsciiFramer
from pymodbus.exceptions import ModbusException

import time

client = ModbusSerialClient(framer=ModbusAsciiFramer, port = "COM7", stopbits = 1, bytesize = 7, parity = "E", baudrate = 9600)

# analog_memory和register重複的 address視機型而有所不同
input_start = 1024 #input address: 1024-1279, digit
output_start = 1280 #output address: 1280-1536, digit
timer_start = 1536 #timer address: 1536-1791, analog
counter_start = 3584 #counter address: 3584-3839, analog
digit_memory_start = 2048 #digit_memory address: 2048-3583, digit
analog_memory_start = 5056 # analog_memory address: 5056-7615, analog
register_start = 4096 #register address: 4096-7615, analog

#plc只要有通電，無論run或stop狀態都可以connect
# plc_connection = client.connect()


# if plc_connection:
print("PLC連接成功")

try:
    i = 0
    y = [False, False, False, False]
    while True:
        y[i % 4] = True
        # client.write_coils(address=output_start, values=y, slave=1)
        print(y)
        time.sleep(1)
        y = [False, False, False, False]
        # client.write_coils(address=output_start, values=y, slave=1)
        i += 1


except ModbusException as e:
    print(f'Error: {e}')

finally:
    client.close()
    print("PLC關閉連接")