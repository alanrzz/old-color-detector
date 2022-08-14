import cv2
import numpy as np

lower = np.array([15,150,20])
upper = np.array([35,255,255])

capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    
    if ret:
        frame = cv2.flip(frame, 1)
        mask = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(mask, lower, upper)

        outlines, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(outlines) != 0:
            for outline in outlines:
                if cv2.contourArea(outline) > 500:
                    x, y, w, h = cv2.boundingRect(outline)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),3)

        cv2.imshow("mask", mask)
        cv2.imshow("original", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        print("No se pudo iniciar la camara.")
        break