import cv2

# Webcam
video = cv2.VideoCapture(0)
print(type(video))

# See how many frames
numbers_frames = 1
while True:
    numbers_frames = numbers_frames + 1
    check, frame = video.read()
    print(type(frame))
    print(frame)
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print("Frames: {}".format(numbers_frames))
video.release()
cv2.destroyAllWindows()

