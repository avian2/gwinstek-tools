from usbtmc import USBTMC

class AFG(USBTMC):
	NMAX = 4096

	R = 511

	def set_waveform(self, fo, data):
		assert len(data) <= self.NMAX
		assert max(data) <= self.R
		assert min(data) >= -self.R

		data *= self.R
		vec = ','.join("%.0f" % i for i in data)

		self.command("data:dac VOLATILE,0,%s" % (vec,))
		self.command("source1:freq %f" % (fo,))
