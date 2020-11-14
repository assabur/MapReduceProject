#!/usr/bin/python
#!/usr/bin/env python3
import serial.tools.list_ports as port_list
import serial
ports = list(port_list.comports())
for p in ports:
    print (p)
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
while True :
        with serial.Serial('/dev/ttyUSB0', 19200, timeout=1) as ser:
            x = ser.read()          # read one byte
            s = ser.read(10)        # read up to ten bytes (timeout)
            line = ser.readline()   # read a '\n' terminated line
            #print(x)
            print(s)
            print(line)
            #x.decode("utf-8")
            print(x)
            #print(bytearray.fromhex("0x61").decode()('utf-8'))
            #b'\x06\x06x\xf8\xfe\xfe
            #b'\xf8'



