import cv2
import numpy as np

# reading video
video = cv2.VideoCapture("s200.mp4")

while True:
	# reading frames
    ret, orig_frame = video.read()
    # until the video ends continue looping throug frames
    if not ret:
        video = cv2.VideoCapture("s200.mp4")
        continue
    # blurring the frames to detect edge accurately
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    # converting BGR(blue, green, red) color space to HSV(hue, saturation, value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower and higher hsv values of yellow color
    low_yellow = np.array([18, 94, 140])
    up_yellow = np.array([48, 255, 255])
    # masking the scenes except detected lanes
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    # detect edges
    edges = cv2.Canny(mask, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
    # drawing lines above detected lanes
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0] 
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("frame", frame)
    # cv2.imshow("edges", edges)
    # key = cv2.waitKey(25)
    # if key == 27:
    # 	break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
