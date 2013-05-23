from afg import AFG
import time

def main():
	afg = AFG("/dev/ttyACM0")

	afg.write("source1:function sin")

	for n in xrange(10, 700, 10):
		afg.write("source1:frequency %f" % (n*1e3,))
		time.sleep(0.2)

main()
