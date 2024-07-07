#Task 1
#Opening and changing colour 
import cv2
path = "./task_1/tom.jpg"
image = cv2.imread("Leo-Dicarprio-Face-Front-ipad.jpg")
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Output",image)
cv2.imshow("Output_gray",image_gray)
cv2.waitKey()
cv2.destroyAllWindows()