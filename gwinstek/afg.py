from usbtmc import USBTMC

class AFG2000(USBTMC):
	NMAX = 4096

	R = 511

	def set_waveform(self, fo, data):
		"""Set waveform for arbitrary waveform generator.

		Output function is switched to ARB.

		sampling rate = fo * len(data)

		fo -- repetition frequency of the waveform in hertz.
		data -- sequence of data points for the waveform between -1.0
		(minimum level) and 1.0 (maximum level)
		"""
		assert len(data) <= self.NMAX
		assert max(data) <= 1.0
		assert min(data) >= -1.0

		data *= self.R
		vec = ','.join("%.0f" % i for i in data)

		self.command("DATA:DAC VOLATILE,0,%s" % (vec,))
		self.command("SOURCE1:FREQ %.1f" % (fo,))
