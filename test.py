import cv2
import numpy as np

cap = cv2.VideoCapture("data/register.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

print(cv2.__version__)