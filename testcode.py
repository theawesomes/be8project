# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:55:32 2017

@author: Priya
"""
from PIL import Image
import sys, os
import numpy as np

class Picture:
	"""Picture"""
	def __init__(self, path):
		self.__path = path
		self.__threshold = 128.0
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
p=Picture("test.jpg")
x=p.getVector()
a=np.array([x])
c=np.array([x])
teda.append((a.T,c.T))
tedaa1=['x']
tedaa1.append(teda[0][0])

