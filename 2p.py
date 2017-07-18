import numpy
import matplotlib.pyplot as plt


class filter:
	
	def __init__(self):
		self.f = 0.0;
		self.q = 0.0;
		self.lp = 0.0;
		self.hp = 0.0;
		self.bp = 0.0;
		self.buf0 = 0.0;
		self.buf1 = 0.0;

	def setFc(self, fc):
		#self.f = fc/1000;		#make the sampling rate the same as the length of the singal to make it easier
		self.f = 2.0 * numpy.sin(3.14159 * fc / 1000);		#make the sampling rate the same as the length of the singal to make it easier

	def setQ(self, Q):
		self.q = Q + Q/(1.0 - self.f);

	def process(self, ip):
		self.buf0 = self.buf0 + self.f * (ip - self.buf0 + self.q * (self.buf0 - self.buf1));
		self.buf1 = self.buf1 + self.f * (self.buf0 - self.buf1);
		self.lp = self.buf1;
		#move these before the filter ?
		self.bp = self.buf0 - self.buf1;
		self.hp = ip - self.buf0;


#variables for making a waveform...
phase = 0.002;			#should produce 2 periods per 1000 samples
signal_now = -0.5;
signal = [];

#variables for a filter...
lp_signal = [];
bp_signal = [];
hp_signal = [];

f = filter();

f.setFc(30.0);
f.setQ(0.8);

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
