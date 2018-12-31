import cv2 

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
     
    check, frame = webcam.read()
    print(check) #prints true as long as the webcam is running
    print(frame) #prints matrix values of each framecd 
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('s'): 
        cv2.imwrite(filename='saved_img.jpg', img=frame)
         
        break
    elif key == ord('q'):
        break
webcam.release()
img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
img_new = cv2.imshow("Captured Image", img_new)
cv2.waitKey(1650)
cv2.destroyAllWindows()

img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
img_ = cv2.resize(gray,(28,28))
img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
