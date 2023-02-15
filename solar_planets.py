import cv2

img= cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(70,50),cv2.FONT_HERSHEY_SIMPLEX,1,(130,20,60),2)
cv2.putText(img,"Mercury",(130,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(130,20,60),2)
cv2.putText(img,"Venus",(190,170),cv2.FONT_HERSHEY_SIMPLEX,0.5,(130,20,60),2)
cv2.putText(img,"Earth",(290,180),cv2.FONT_HERSHEY_SIMPLEX,0.5,(130,20,60),2)

cv2.imshow("Solar system",img)

cv2.waitKey(5000)