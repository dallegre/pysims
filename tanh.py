import numpy
import matplotlib.pyplot as plt

k = []
q = []
j = 0.0;

for i in range (0,60):
	k.insert(i,0.1 * (i-30));
	q.insert(i,numpy.tanh(0.1 * (i-30)));
	print("k is %f and q is %f" % (k[i],q[i]))
	#print("k is %f" % k[i])


plt.plot(k)
plt.plot(q)
plt.show()

