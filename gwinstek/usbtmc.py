import os

class USBTMCError(Exception):
	def __init__(self, command, errno):
		Exception.__init__(self, "Command '%s' caused error %d" % (
			command[:100], errno))

class USBTMC:
	def __init__(self, device):
		self.device = device
		self.f = os.open(device, os.O_RDWR)
		self.write("*CLS")

	def write(self, command):
		os.write(self.f, command)
		os.write(self.f, "\n")

	def read(self, length=4000):
		return os.read(self.f, length)

	def query(self, command, length=300):
		self.write(command)
		return self.read(length)

	def command(self, command):
		self.write(command)

		error = self.query("SYSTEM:ERROR?")
		if error != "No Error\r\n":
			raise USBTMCError(command, int(error))

	def get_name(self):
		return self.query("*IDN?")

	def send_reset(self):
		self.write("*RST")

	def close(self):
		os.close(self.f)
