import cv2
import numpy as np

cap = cv2.VideoCapture('http://192.168.178.33/800x600.jpg')

# (x, y, w, h) = cv2.boundingRect(c)
# cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 20)
# roi = frame[y:y+h, x:x+w]

while True:
    ret, frame = cap.read()
    # (height, width) = frame.shape[:2]
    sky = frame[0:100, 0:200]
    cv2.imshow('Video', sky)

    if cv2.waitKey(1) == 27:
        exit(0)
