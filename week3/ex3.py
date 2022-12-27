
from PIL import Image

# open method used to open different extension image file
im = Image.open(r"D:\python\week3\TUM_old.jpg")

# This method will show image in any image viewer
# im.show()
width, height = im.size

# print(im.size)
new_img = im.resize([int(width/2), int(height/2)])
new_img.show()

# Saved in the same relative location
new_img.save("TUM_small.jpg")
