import os
from PIL import Image
l1=os.listdir(os.getcwd())
p=[]
for ele in l1:
 if ele.startswith('$') and ele.endswith('.jpg'):
  p.append(ele)
for path in p:
 im1=Image.open(path)
 im2=im1.rotate(-90)
 im2.save(path)