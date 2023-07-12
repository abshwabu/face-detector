import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface')

img = cv2.imread('photo.jpg')

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()