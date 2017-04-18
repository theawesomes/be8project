print "HELLO?"
import os,cv2
from PIL import Image
from rotatefun import *
print "starting"
l1=os.listdir(os.getcwd())
p=[]
for ele in l1:
 if ele.startswith('$') and ele.endswith('.jpg'):
  p.append(ele)
print l1
print "Why this Kolaveri"
print p
for path in p:
 im1=cv2.imread(path)
 im2=rotate_image(im1,-90)
 print "I rotated"
 cv2.imwrite(path,im2)