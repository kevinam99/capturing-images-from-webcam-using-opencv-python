# capture image using webcam
import cv2
0.7
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:  # infinite loop as webcam require infite amount of shots
        ret, frame = cap.read()
        cv2.imshow('live sketch', frame)
        if cv2.waitKey(1) == 13:  # 13 is ASCII of Enter key
            break
            cap.release

else:
    ret = False
cv2.destroyAllWindows()
img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.title("Captured img")
plt.xticks([])
plt.yticks([])
plt.show()


cap.release()
cv2.destroyAllWindows()
