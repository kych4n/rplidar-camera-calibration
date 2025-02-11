import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"2D pixel : ({x}, {y})")

cap = cv2.VideoCapture(2) # When `ls -ltrh /dev/video*` is entered in the terminal, enter the number corresponding to *

while cap.isOpened():
    _, frame = cap.read()

    cv2.imshow('frame', frame)
    cv2.setMouseCallback('frame', click_event)
    if cv2.waitKey(25) == ord('q'):
        break