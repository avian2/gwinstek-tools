import os

class usbtmc:
	def __init__(self, device):
		self.device = device
		self.f = os.open(device, os.O_RDWR)

	def write(self, command):
		os.write(self.f, command + "\n");

	def read(self, length=4000):
		return os.read(self.f, length)

	def query(self, command, length=300):
		self.write(command)
		return self.read(length)

	def get_name(self):
		return self.query("*IDN?\n")

	def send_reset(self):
		self.write("*RST")

	def close(self):
		os.close(self.f)
