from cvzone.FaceDetectionModule import FaceDetector
import cv2
import serial,time
cap = cv2.VideoCapture(1)
detector = FaceDetector()
ArduinoSerial = serial.Serial('com11', 9600)


def sendingdata(x,y):
    string = 'X{0:d}Y{1:d}'.format((x), (y))
    ArduinoSerial.write(string.encode('utf-8'))
    print(string)

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        bbox = bboxs[0]["bbox"]
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        x, y, w, h = bbox
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Draw a rectangle around the face
        center = bboxs[0]["center"] 
        sendingdata(x,y)

    cv2.imshow("Image", img)
    cv2.waitKey(1)