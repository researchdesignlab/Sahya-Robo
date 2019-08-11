import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

option = {
    'model': 'cfg/yolo.cfg', #cfg file location
    'load': 'bin/yolov.weights', #weights location
    'threshold': 0.15, 
    'gpu':1.0, #put this if you have tensorflow gpu version
    
    
}

tfnet = TFNet(option)

capture = cv2.VideoCapture(0) #0 for inbuilt camera and 1 for external camera
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame) 
        #next section is used to display output in a window with a camera feed and bounding boxes
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y']) #top left cordinates of the detected object
            br = (result['bottomright']['x'], result['bottomright']['y']) #bottom right cordinates of detected object
            label = result['label'] #lable/name of the object
            frame = cv2.rectangle(frame, tl, br, color, 2)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press q to quit
            break
        
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
   
