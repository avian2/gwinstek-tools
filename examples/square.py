from gwinstek.afg import AFG2000
import numpy

def main():
	afg = AFG2000("/dev/ttyACM0")

	w = numpy.array([-511,511])
	afg.set_waveform(10e6/len(w), w)

main()
