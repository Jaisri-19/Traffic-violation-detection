import cv2
import numpy as np


cap = cv2.VideoCapture('tr.mp4')

def process_frame(frame):
    
    lower_range = np.array([58, 97, 222])  
    upper_range = np.array([179, 255, 255])
    lower_range1 = np.array([0, 43, 184])  
    upper_range1 = np.array([56,132, 255])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    mask = cv2.inRange(hsv, lower_range, upper_range)
    mask1 = cv2.inRange(hsv, lower_range1, upper_range1)

    
    combined_mask = cv2.bitwise_or(mask, mask1)

    
    _, final_mask = cv2.threshold(combined_mask, 254, 255, cv2.THRESH_BINARY)
    detected_label = None
             
    
    cnts, _ = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        if cv2.contourArea(c) > 50:
            x, y, w, h = cv2.boundingRect(c)
            
            
            cx = x + w // 2
            cy = y + h // 2
    

            
            if cv2.countNonZero(mask[y:y+h, x:x+w]) > 0:  
               color = (0, 255, 0)  
               text_color = (0, 255, 0)  
               label = "GREEN"
            elif cv2.countNonZero(mask1[y:y+h, x:x+w]) > 0:  
                color = (0, 0, 255)  
                text_color = (0, 0, 255)  
                label = "RED"
            else:
                continue
            
            detected_label = label 
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                
           
            cv2.circle(frame, (cx, cy), 1, (255, 0, 0), -1)  r
            
            
            cv2.putText(frame, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)
    
    return frame,detected_label

count = 0




while True:
    ret, frame = cap.read()
    count += 1
    if count % 3 != 0:
        continue
    if not ret:
        break

    frame = cv2.resize(frame, (1020, 600))
    processed_frame,detected_label = process_frame(frame)
    


    cv2.imshow("RGB", frame)
    if cv2.waitKey(0) & 0xFF == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()