from usbtmc import USBTMC

class AFG2000(USBTMC):
	NMAX = 4096

	R = 511

	def set_waveform(self, fo, data):
		assert len(data) <= self.NMAX
		assert max(data) <= self.R
		assert min(data) >= -self.R

		data *= self.R
		vec = ','.join("%.0f" % i for i in data)

		self.command("DATA:DAC VOLATILE,0,%s" % (vec,))
		self.command("SOURCE1:FREQ %f" % (fo,))
