import cv2
import numpy as np

cap = cv2.VideoCapture(2) #here we specify the camera (0, 2)

while True:
	#Capture frame-by-frame
	ret, frame = cap.read() #return true/false

	#Our operations on the frame come here
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([38, 86, 0])
	upper_blue = np.array([121, 255, 255])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	#Display the resulting frame
	cv2.imshow("Frame", frame)
	cv2.imshow("Mask", mask)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()