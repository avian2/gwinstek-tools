from gwinstek.afg import AFG2000
import numpy

def main():
	afg = AFG2000("/dev/ttyACM0")

	w = numpy.array([-1.0,1.0])
	afg.set_waveform(10e6/len(w), w)

main()
