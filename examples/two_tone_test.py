from fractions import gcd
from gwinstek.afg import AFG2000
import numpy

def generate_waveform(f1, f2, n=4096):
	fo = gcd(f1, f2)
	fs = fo*n

	t = numpy.arange(0, 1.0/fo, 1.0/fs)
	assert len(t) == n

	print "f1 = %f Hz (%f points)" % (f1, fs/f1)
	print "f2 = %f Hz (%f points)" % (f2, fs/f2)

	w = numpy.sin(2*numpy.pi*t*f1) + numpy.sin(2*numpy.pi*t*f2)
	w = (w - min(w))/(max(w)-min(w)) * 2 - 1

	assert max(w) == 1
	assert min(w) == -1

	return fo, w

def main():
	afg = AFG2000("/dev/ttyACM0")

	fo, w = generate_waveform(700, 1900)

	afg.set_waveform(fo, w)

main()
