import cv2
import time

# Settings
CONFIRMATION_THRESHOLD = 15 # Wait 15 frames before flagging intruder
intruder_counter = 0

# Load Face Model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

print(">>> SYSTEM START: FRONTIER MONITOR ACTIVE")

while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        # If no clear face (motion blur), increment buffer but don't alarm yet
        intruder_counter += 1
    else:
        # Face found - reset buffer
        intruder_counter = 0
        cv2.putText(frame, "STATUS: OWNER VERIFIED", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 243, 0), 2)

    if intruder_counter > CONFIRMATION_THRESHOLD:
        cv2.putText(frame, "ALARM: UNKNOWN INTRUDER", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # Here is where you would call your JavaScript API to update the website

    cv2.imshow('Python Surveillance Agent', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
