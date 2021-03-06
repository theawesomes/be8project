
import os
from PIL import Image
import cv2
import math
def rotate_image(mat, angle):
    height, width = mat.shape[:2]
    image_center = (width / 2, height / 2)

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)

    radians = math.radians(angle)
    sin = math.sin(radians)
    cos = math.cos(radians)
    bound_w = int((height * abs(sin)) + (width * abs(cos)))
    bound_h = int((height * abs(cos)) + (width * abs(sin)))

    rotation_mat[0, 2] += ((bound_w / 2) - image_center[0])
    rotation_mat[1, 2] += ((bound_h / 2) - image_center[1])

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat
l1=os.listdir(os.getcwd())
p=[]
for ele in l1:
 if ele.startswith('$') and ele.endswith('.jpg'):
  p.append(ele)

for path in p:
 im1=cv2.imread(path)
 im2=rotate_image(im1,-90)
 cv2.imwrite(path,im2)