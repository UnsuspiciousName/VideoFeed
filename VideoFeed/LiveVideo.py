#   LiveVideo is a testbed for getting to know basic
#       video formatting and how Python handles these addresses


#Reference Documents : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np  #Numpy also seems like one the libraries Harsh Reccomended
import cv2          #CV2 is one of the libraries Harsh Reccomended for Computer Vision
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() #cap.read() returns a bool (True/False), if frame is read correctly. So, you can check end of the video by checking this return value.

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
