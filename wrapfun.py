from tester import *
def wrapper1(net):
	for i in range(26):
		net.predict1(test_data[i])
		
