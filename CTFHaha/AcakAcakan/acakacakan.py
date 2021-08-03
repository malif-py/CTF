# -*- coding: utf-8 -*-

import random
random.seed("wadidaw")


flag = "REDACTED"
out = ""

for c in flag:
	part1 = (ord(c) ^ random.randint(0x00, 0xFF))
	part2 = random.randint(0x00, 0xFF)
	print(part2)
	out += hex( (part1 + part2) % 0xFF) + ' '

print ((out))