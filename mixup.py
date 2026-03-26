import cv2

image1 = cv2.imread('img/corrosionLevel1_355.jpg')
image1 = cv2.resize(image1, (600, 600))
image2 = cv2.imread('img/corrosionLevel3_445.jpg')
image2 = cv2.resize(image2, (600, 600))
new_image = image1 * 0.9+ image2 * 0.1

cv2.imwrite('mixup.jpg', new_image)
