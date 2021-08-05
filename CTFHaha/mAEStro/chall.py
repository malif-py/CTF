from Crypto.Cipher import AES
from os import urandom
import sys

key = IV = urandom(16)

class Unbuffered(object):
	def __init__(self, stream):
		self.stream = stream
	def write(self, data):
		self.stream.write(data)
		self.stream.flush()
	def writelines(self, datas):
		self.stream.writelines(datas)
		self.stream.flush()
	def __getattr__(self, attr):
		return getattr(self.stream, attr)

def pad(msg):
	return msg + (chr(16 - (len(msg) % 16)) * (16 - (len(msg) % 16)))

def enc(pt):
	global key, IV
	cipher = AES.new(key, AES.MODE_CBC, IV)
	return cipher.encrypt(pad(pt))

def dec(ct):
	global key, IV
	cipher = AES.new(key, AES.MODE_CBC, IV)
	return cipher.decrypt(ct)

def main():
	menu = """Welcome apprentice...
1. Encrypt message
2. Decrypt message
3. Input Maestro's password
4. Exit
Do what you need..."""
	while True:
		print menu
		op = raw_input()
		if op == '1':
			print "Input your message (in hex):"
			pt = raw_input()
			try:
				pt = pt.decode('hex')
			except Exception as e:
				print "Invalid input! Bye..."
				exit(0)
			print "This is your encrypted message"
			print enc(pt).encode('hex')
		elif op == '2':
			print "Input your encrypted message (in hex):"
			ct = raw_input()
			try:
				ct = ct.decode('hex')
				assert len(ct) % 16 == 0
				assert len(ct) > 16
			except Exception as e:
				print "Invalid input! Bye..."
				exit(0)
			print "This is your decrypted message"
			print dec(ct).encode('hex')
		elif op == '3':
			print "Input Maestro's password (in hex):"
			pswd = raw_input()
			if pswd.decode('hex') == key:
				print "Welcome Maestro..."
				print FLAG
			else:
				print "You're not Maestro..."
				exit(0)
		else:
			print "Bye apprentice..."
			exit(0)

# Unbuffer stdout
sys.stdout = Unbuffered(sys.stdout)

if __name__ == '__main__':
	main()