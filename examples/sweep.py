from gwinstek.afg import AFG2000
import time

def main():
	afg = AFG2000("/dev/ttyACM0")

	afg.command("source1:function sin")

	for n in xrange(10, 700, 10):
		afg.command("source1:frequency %f" % (n*1e3,))
		time.sleep(0.2)

main()
