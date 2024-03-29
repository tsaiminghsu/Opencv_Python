import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('tp1.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('test.jpg', 0)

w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
 
cv2.imwrite('res.png',img)
plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result')#, plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Detected Point')#, plt.xticks([]), plt.yticks([])
plt.suptitle('threshold): ' + threshold)
plt.show()
