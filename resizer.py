import os
from PIL import Image
l1=os.listdir(os.getcwd())
p=[]
for ele in l1:
 if ele.startswith('$') and ele.endswith('.jpg'):
  p.append(ele)
for path in p:
 img = Image.open(path)
 img = img.resize((28, 28), Image.BILINEAR)
 img.save(path)