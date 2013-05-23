from fractions import gcd
from gwinstek.afg import AFG2000
import numpy

def generate_waveform(fc, fm, fdev, n=4096):
	fo = gcd(fc, fm)
	print "fo = %f Hz" % (fo,)
	fs = fo*n

	t = numpy.arange(0, 1.0/fo, 1.0/fs)
	assert len(t) == n

	print "fc = %f Hz (%f points)" % (fc, fs/fc)
	print "fm = %f Hz (%f points)" % (fm, fs/fm)

	w = numpy.sin(2*numpy.pi*t*fc + 2*numpy.pi*fdev*numpy.sin(2*numpy.pi*t*fm))
	#w = numpy.sin(2*numpy.pi*t*fc)
	w = (w - min(w))/(max(w)-min(w)) * 2 - 1

	assert max(w) == 1
	assert min(w) == -1

	return fo, w

def main():
	afg = AFG2000("/dev/ttyACM0")

	fo, w = generate_waveform(100e3, 4e3, .1e3)

	afg.set_waveform(fo, w)

main()
