from ultralytics import YOLO
import cv2
import math

model = YOLO("rigisterplate.pt")

def video_detection(frame, model=model):
    results = model.predict(source=frame,conf=0.75,show=False)
    # print(frame_resized.shape)
    for result in results:
        boxes = result.boxes
        if len(boxes) != 0:
            for box in boxes:
                x,y,w,h = int(box.xyxy[0][0]),int(box.xyxy[0][1]),int(box.xyxy[0][2]),int(box.xyxy[0][3])
                sub_frame = frame[y:h,x:w]
                try:
                    text = reader.readtext(sub_frame)
                    if text[0][-1] > 0.8:
                        cv2.putText(frame,f"{text[0][-2]}",(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,2)
                except:
                    cv2.putText(frame,f"No text",(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,2)
                # print(text)
                # cv2.imshow("Video2",sub_frame)
            cv2.rectangle(frame,(x,y),(w,h),(255,0,255),4)

    return frame