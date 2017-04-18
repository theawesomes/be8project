import os,sys
import numpy as np
from trandata import *
print "Training Data is Generated"
import network
import ctypes
net=network.Network([784,60,50,26])
net.SGD(training_data,100,10,3.0)
print "Network is Trained. Commencing Testing Sequence..."
from PIL import Image
import sys, os
import numpy as np
class Picture:
	"""Picture"""
	def __init__(self, path):
		self.__path = path
		self.__threshold = 64.0
		self._vector = []

	def getVector(self):
		try:
			im = Image.open(self.__path)
		except:
			sys.stderr.write("ERROR: File %s doesn't exist.\n" % self.__path)
			sys.exit()

		tupleList = list(im.getdata())
		#print tupleList
		for i in tupleList:
			greyscale = 0.3*i[0] + 0.59*i[1] + 0.11*i[2]
			if (self.__threshold < greyscale):
				self._vector.append(0.)
			else:
				self._vector.append(0.5625)
		f = open("lol.txt",'w')
		f.write(str(self._vector))
		return tuple(self._vector)

	def printVector(self, width):
		if self._vector == []:
			self.getVector()

		for x in range(0,len(self._vector)):
			if x % width == 0:
				print
			print self._vector[x],


teda=[]
tedaa1=[]
k=0
choice=raw_input("Do You Want To Predict a Character? (y or n): ")
while(choice=='y'):
    execfile('paint.py')
    i1=Image.open('test.jpg')
    i2=i1.resize((426,426),Image.BILINEAR)
    i2.save('test.jpg')
    execfile('segwrap2.py')    
    l1=os.listdir(os.getcwd())
    p=[]
    for ele in l1:
        if ele.startswith('$') and ele.endswith('.jpg'):
            p.append(ele)
    ans=""
    for path in p:
        p=Picture(path)
        x=p.getVector()
        a=np.array([x])
        c=np.array([x])
        teda.append((a.T,c.T))
        tedaa1.append(teda[k][0])
        ans=ans+" "+net.predict1(tedaa1[k])
        k+=1
    uni = unicode(ans, "utf-8")
    ctypes.windll.user32.MessageBoxW(0, uni, u"Your Output is:", 1)
    choice=raw_input("Do You Want To Predict a Character? (y or n): ")
    
    