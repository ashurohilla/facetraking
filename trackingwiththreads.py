import cv2
import mediapipe as mp
import serial
import threading
import time

# Initialize the FaceMesh model and the video capture device
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
cap = cv2.VideoCapture(1)

# Connect to the Arduino serial port
ArduinoSerial = serial.Serial('com4', 9600)

def sendingdata(results):
    for face_landmarks in results.multi_face_landmarks:
        for landmark in face_landmarks.landmark:
            x = int(landmark.x * image.shape[1])
            y = int(landmark.y * image.shape[0])
            cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)
            string = 'X{0:d}Y{1:d}'.format((x), (y))
            ArduinoSerial.write(string.encode('utf-8'))
            
            print(string)

def send_data_thread(results):
    while True:
        sendingdata(results)
        time.sleep(0.5)
        

while True:
    # Capture a frame from the video device
    success, frame = cap.read()
    if not success:
        break


    frame = cv2.resize(frame, (800, 400))

    # Convert the BGR image to RGB and process it with the FaceMesh model
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    # If landmarks are detected, draw them on the image
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])
                cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)

    # Display the image
    cv2.imshow('Face Mesh', frame)
    if cv2.waitKey(1) == ord('q'):
        break

    # Create and start the thread to send data to the Arduino
    send_data_t = threading.Thread(target=send_data_thread, args=(results,))
    send_data_t.start()

# Release the resources
cap.release()
cv2.destroyAllWindows()
