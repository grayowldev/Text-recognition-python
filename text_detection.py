import cv2
import pytesseract

# Reading and displaying an image with cv2
img = cv2.imread('testimg.jpg')
#change from BGR to RGB color format
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Result",img)
cv2.waitKey(0)



