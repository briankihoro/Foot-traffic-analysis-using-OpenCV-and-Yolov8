import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
from tracker import *

model = YOLO('best.pt')
tracker = Tracker()

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('fdoor.avi')

my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n")
# print(class_list)

count = 0
area1 = [(715, 273), (688, 272), (737, 487), (783, 484)]
area2 = [(701, 272), (688, 272), (737, 487), (758, 486)]
pin = {}
enter = []

# Set up the video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can also use 'MP4V' or 'MJPG'
out = cv2.VideoWriter('foottraffic_video.avi', fourcc, 20.0, (1020, 500))

while True:    
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    count += 1
    if count % 2 != 0:
        continue
    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)
    # print(results)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    # print(px)
    list = []      
    for index, row in px.iterrows():
        # print(row)
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        list.append([x1, y1, x2, y2])

    bbox_idx = tracker.update(list)
    for bbox in bbox_idx:
        x3, y3, x4, y4, id = bbox
        cx = int(x3 + x4) // 2
        cy = int(y3 + y4) // 2
        w, h = x4 - x3, y4 - y3
        result = cv2.pointPolygonTest(np.array(area1, np.int32), ((cx, cy)), False)
        if result >= 0:
            pin[id]= (cx, cy)
        if id in pin: 
           result = cv2.pointPolygonTest(np.array(area2, np.int32), ((cx, cy)), False)
        if result >= 0:
            # Draw a rectangle with rounded corners
            cvzone.cornerRect(frame, (x3, y3, w, h), 10, 5)
            # Draw a circle at the center of the bounding box
            cv2.circle(frame, (cx, cy), 4, (255, 0, 255), -1)
            # Put text with a rectangle around it
            cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 1)
            if enter.count(id) == 0:
                enter.append(id)

    # Draw polygons
    ep = len(enter)
    cv2.polylines(frame, [np.array(area1, np.int32)], True, (0, 0, 255), 2)
    # cvzone.putTextRect(frame, f'area1', (613, 232), 1, 1)
    cv2.polylines(frame, [np.array(area2, np.int32)], True, (0, 0, 255), 2)
    cvzone.putTextRect(frame, f'counter:-{ep}', (50, 60), 2, 2)
    
    # Write the frame to the video file
    out.write(frame)
    
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()  # Release the video writer
cv2.destroyAllWindows()
