import cv2

cam = cv2.VideoCapture(0)

focus = 0  # min: 0, max: 255, increment:5
cam.set(28, focus)