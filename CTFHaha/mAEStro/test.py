from os import urandom

key = IV = urandom(16)

def pad(msg):
	return msg + (chr(16 - (len(msg) % 16)) * (16 - (len(msg) % 16)))

text1 = '0f'.decode('hex')
text2 = '0e0e'.decode('hex')
test1 = 0x9bf9699c9d513a551b78e857d317c3e5
test2 = 0x818819b9d94bc39835995e8e2f33abf7
print(pad(text1), pad(text2))