import numpy as np
import cv2 


cap = cv2.VideoCapture("sample1.mp4")

 
while cap.isOpened():
    flag = True
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (15, 15), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            a = x + (w // 2)
            b = y + (h // 2)
            cv2.line(frame, (a,0), (a,840), (255,0,0), 1)
            cv2.line(frame, (0,b), (840,b), (0,0,255), 1)
            
                

        cv2.imshow('frame', frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            flag = False 
            break
    if flag==False:
        break
           
   

    
 
cap.release()
cv2.destroyAllWindows()