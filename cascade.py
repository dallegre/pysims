#state variable filter modelling.  Useful for seeing how far you can push things without it going unstable.

import numpy
import matplotlib.pyplot as plt


class filter:
	
	def __init__(self):
		self.f = 0.0;
		self.q = 0.0;
		self.lp = 0.0;
		self.b1 = 0.0;
		self.a0 = 0.0;
		self.z1 = 0.0;
		self.z2 = 0.0;
		self.z3 = 0.0;
		self.feedback = 0.0;

	def setFc(self, fc):
		self.b1 = numpy.exp(-2.0 * 3.14159 * fc / 1000 );
		self.a0 = 1.0 - self.b1;

	def setQ(self, Q):
		self.q = Q;

	def process(self, ip):
		self.z1 = (ip - self.q * self.feedback) * self.a0 + self.z1 * self.b1;
		self.z2 = self.z1 * self.a0 + self.z2 * self.b1;
		self.z3 = self.z2 * self.a0 + self.z3 * self.b1;
		self.lp = self.z3 * self.a0 + self.lp * self.b1;
		self.feedback = self.lp;
		

#variables for making a waveform...
phase = 0.002;			#should produce 2 periods per 1000 samples
signal_now = -0.5;
signal = [];

#variables for a filter...
lp_signals = [];

filters = [];

for count in xrange(100):
	f = filter();
	f.setFc(4.0 + count);
	f.setQ(0.1 + count/20.0);
	f.attr = count;
	filters.append(f);
	lp_signals.append([]);

for i in range(0, 1000):
	signal.insert(i, signal_now);
	signal_now += phase;
	if(signal_now > 0.5):
		signal_now = -0.5;
	for count in xrange(100):
		filters[count].process(signal_now);
		lp_signals[count].insert(i, filters[count].lp);

#plt.plot(signal);
for count in xrange(100):
	plt.plot(lp_signals[count]);
plt.show();
