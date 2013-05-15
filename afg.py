from usbtmc import usbtmc

class AFG:
	NMAX = 4096

	R = 511

	def __init__(self, path):
		self.usbtmc = usbtmc(path)

	def write(self, command):
		return self.usbtmc.write(command)

	def read(self):
		return self.usbtmc.read()

	def set_waveform(self, fo, data):
		data *= self.R
		vec = ','.join("%.0f" % i for i in data)

		self.usbtmc.write("source1:freq %f" % (fo,))
		self.usbtmc.write("data:dac VOLATILE,0,%s" % (vec,))
		self.usbtmc.write("source1:function arb")
