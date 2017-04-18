from PIL import Image
import os
from PIL import Image
l1=os.listdir(os.getcwd())
p=[]
for ele in l1:
 if ele.startswith('$') and ele.endswith('.jpg'):
  p.append(ele)
for path in p:
	img = Image.open(path, 'r')
	img_w, img_h = img.size
	background = Image.new('RGBA', (30, 30), (255, 255, 255, 255))
	bg_w, bg_h = background.size
	offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
	background.paste(img, offset)
	background.save(path)