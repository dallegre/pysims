#state variable filter modelling.  Useful for seeing how far you can push things without it going unstable.

import numpy
import matplotlib.pyplot as plt


class filter:
	
	def __init__(self):
		self.f = 0.0;
		self.q = 0.0;
		self.hp = 0.0;
		self.bp = 0.0;
		self.lp = 0.0;
		self.bp_1 = 0.0;
		self.lp_1 = 0.0;

	def setFc(self, fc):
		self.f = 2.0 * numpy.sin(3.14159 * fc / 1000);		#make the sampling rate the same as the length of the singal to make it easier

	def setQ(self, Q):
		self.q = 0.1 * (1/Q);

	def process(self, ip):
		self.hp = ip - (self.q * self.bp_1) - self.lp;
		self.bp = self.bp_1 + (self.f * self.hp);
		self.lp = self.lp_1 + (self.f * self.bp_1);
		#do integratio for next time around
		self.lp_1 = self.lp;
		self.bp_1 = self.bp;

#variables for making a waveform...
phase = 0.002;			#should produce 2 periods per 1000 samples
signal_now = -0.5;
signal = [];

#variables for a filter...
hp_signal = [];
bp_signal = [];
lp_signal = [];

f = filter();

f.setFc(30.0);			#30 is about as high as you can go without weirdness (30/1000 is the ratio of interest).  This indicates that at 48KHz, 16x upsampling should be good enough.
f.setQ(0.3);			#from about 0.05 (minimum) to 0.5 (oscillating).  I have 0.1 as an effective maximum in my c++ code..

for i in range(0, 1000):
	signal.insert(i, signal_now);
	signal_now += phase;
	if(signal_now > 0.5):
		signal_now = -0.5;
	f.process(signal_now);
	hp_signal.insert(i, f.hp);
	bp_signal.insert(i, f.bp);
	lp_signal.insert(i, f.lp);

plt.plot(signal);
plt.plot(hp_signal);
plt.plot(bp_signal);
plt.plot(lp_signal);
plt.show();
