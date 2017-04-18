
from PIL import Image
 
width = 500
height = 500
 
# Open the image file.
img = Image.open('test.jpg')
 
# Resize it.
img = img.resize((28, 28), Image.BILINEAR)
 
# Save it back to disk.
img.save('test.jpg')
#print "Image Resized!"


