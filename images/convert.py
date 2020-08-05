import cv2
from PIL import Image
img = cv2.imread("./20.jpg")
original_img = Image.open("./../data/Figaro1k/GT/Training/Frame01009-gt.pbm")
print(img.shape)
print(len(original_img))
