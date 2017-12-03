import logging
import os
import termios

log = logging.getLogger(__name__)

class USBTMCError(Exception):
	def __init__(self, command, errno):
		Exception.__init__(self, "Command '%s' caused error %d" % (
			command[:100], errno))

class USBTMC:
	def __init__(self, device):
		self.device = device
		self.f = os.open(device, os.O_RDWR)

		a = termios.tcgetattr(self.f)
		a[0] &= ~termios.INLCR
		a[0] &= ~termios.ICRNL
		a[3] &= ~termios.ECHO
		termios.tcsetattr(self.f, termios.TCSANOW, a)

		self.write("*CLS")

	def write(self, command):
		s = command + '\n'
		log.debug("write %s: %r" % (self.device, s))
		os.write(self.f, s.encode('ascii'))

	def read(self, length=4000):
		r = os.read(self.f, length)
		log.debug("read  %s: %r" % (self.device, r))
		return r.decode('ascii')

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
