string = "6f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3266633130613130ffb0007d"

for i in range(0, len(string), 8):
    for k in range(i + 7, i - 1, -2):
        print(string[k - 1] + string[k], end='')