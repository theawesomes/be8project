import cv2
import numpy as np
from PIL import Image
img=Image.open('test.jpg')
img1=img.rotate(90)
img1.save('new.jpg')
image=cv2.imread('new.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
_,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
i1,contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours
x=[]
y=[]
w=[]
h=[]
for contour in contours:
# get rectangle bounding contour
  [a,b,c,d]=cv2.boundingRect(contour)
  x.append(a)
  y.append(b)
  w.append(c)
  h.append(d)
  
# discard areas that are too large
#if h>300 and w>300:
# continue

# discard areas that are too small
#if h<40 or w<40:
#continue

# draw rectangle around contour on original image
print len(x)

for i in range(len(x)-1):
 cv2.rectangle(image,(x[i],y[i]),(x[i]+w[i],y[i]+h[i]),(255,0,255),2)
 crop_img=image[y[i]:y[i]+h[i],x[i]:x[i]+w[i]]
 cv2.imwrite("$"+str(i)+".jpg",crop_img)
cv2.imwrite('contoured.jpg', image)
"""i2=cv2.imread('contoured.jpg')
f=open("lol.txt","w")
f.write(str(i2))
f.close()
#image = cv2.imread('contoured.jpg')
idx=range(len(contours))
mask = np.zeros_like(image) # Create mask where white is what we want, black otherwise
for i in idx:
 cv2.drawContours(mask, contours, i, 255, -1) # Draw filled contour in mask
 out = np.zeros_like(image) # Extract out the object and place into output image
 out[mask == 255] = image[mask == 255]
 cv2.imshow('Output',out)
 cv2.waitKey(0)

# write original image with added contours to disk
"""