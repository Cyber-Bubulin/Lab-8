import cv2


image = cv2.imread('images/variant-8.jpg')
height, width = image.shape[:2]

cropped = image[(height//2)-200:(height//2)+200, (width//2)-200:(width//2)+200]

cv2.imwrite('cropped_cat.jpg', cropped)