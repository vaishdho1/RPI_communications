'''
Request based communication between rpi and any microcontroller via zigbee
'''

import serial
import time

ser = serial.Serial('/dev/ttyUSB1', 9600)
while 1:
    i = 0
    j = 0
    d = 0
    std = 0x7E
    adr_64_8 = 0x00
    adr_64_7 = 0x00
    adr_64_6 = 0x00
    adr_64_5 = 0x00
    adr_64_4 = 0x00
    adr_64_3 = 0x00
    adr_64_2 = 0xFF
    adr_64_1 = 0xFF
    frame_id = 0x01
    frame_type = 0x10
    adr_16_1 = 0xFF
    adr_16_2 = 0xFF
    broadcast_radius = 0x00
    options = 0x00
    data = input("Enter:")
    data1 = []
    f_frame = []
    data_hex = data.encode("hex")
    data_l = len(data_hex)
    length_int = (data_l / 2) + 14
    a = "0x%04x" % length_int
    l_1 = int(a[2:4], 16)
    l_2 = int(a[4:6], 16)
    while i <= data_l - 2:
        data1.append(int(data_hex[i:i + 2], 16))
        # print data1
        d = d + int(data_hex[i:i + 2], 16)
        i = i + 2

    SUM = frame_id + frame_type + adr_64_1 + adr_64_2 + adr_64_3 + adr_64_4 + adr_64_5 + adr_64_6 + adr_64_7 + adr_64_8 + adr_16_1 + adr_16_2 + options + broadcast_radius + d
    C_S = 255 - (SUM & int("0x00FF", 16))
    frame = ([std, l_1, l_2, frame_type, frame_id, adr_64_8, adr_64_7, adr_64_6, adr_64_5, adr_64_4, adr_64_3, adr_64_2,
              adr_64_1, adr_16_1, adr_16_2, broadcast_radius, options, C_S])
    f_frame = frame[0:17] + data1 + frame[17:18]
    f = bytearray(f_frame)
    ser.write(f)
    time.sleep(.25)
    # Receiving
    k = 1
    len2 = 0
    val1 = ""
    data_rec = ""
    frame_rec = ""
    while k > 0:
        val = ser.read()
        # print val.encode("hex")
        if k == 2:
            val1 += val
        if k == 3:
            val1 += val
            length = val1.encode("hex")
            # print length
            val4 = int(length, 16)
            # print val4
            if val4 == 7:
                len2 = 11
            else:
                len2 = val4 + 5

            # print len2
        frame_rec += val

        # print val
        if k == len2:
            if len2 == 11:
                k = 0
            else:
                data_rec += frame_rec[16:len2 - 1]
                k = -1
            val1 = ""
            data_rec = ""
            frame_rec = ""
        k = k + 1
