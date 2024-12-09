import cv2
import numpy as np
### CROPS
number1 = ((10, 26), (78, 126))

def load(path: str):
    img = cv2.imread(path)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("image", img)
    # cv2.waitKey(0);
    # cv2.destroyAllWindows() 
    return img

img = load("tiles.png")
template = load("1.png")
# template = img[number1[0][1]:number1[1][1], number1[0][0]:number1[1][0]]
img_rgb = load("63842-3135712419.jpg")

h, w = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # Switch columns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('result.png', img_rgb)