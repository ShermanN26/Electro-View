import cv2
import datetime

# 1. Initialize the camera
# 0 is usually the built-in webcam
cap = cv2.VideoCapture(0)

# 2. Set the frame rate (The '120 frames' you asked for)
cap.set(cv2.CAP_PROP_FPS, 120)

# Take a starting frame to compare others against
ret, frame1 = cap.read()
ret, frame2 = cap.read()

print("Sheriff's System Active... Monitoring the Frontier.")

while cap.isOpened():
    # Find the absolute difference between two frames
    diff = cv2.absdiff(frame1, frame2)
    
    # Convert to grayscale (easier for the computer to 'see' motion)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Blur the image to remove 'noise' (false alarms)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Threshold the image: if a pixel changed enough, make it white
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    # Dilate the image to fill in holes
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    # Find contours (the outlines of the moving object)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 900: # Ignore small things like a fly
            continue
        
        # If we are here, something big moved!
        print(f"[{datetime.datetime.now()}] ALARM: Movement on the Frontier!")
        
        # Draw a rectangle around the 'intruder'
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Show the live feed
    cv2.imshow("Sheriff's Console (Press Q to Quit)", frame1)
    
    # Update frames for the next loop
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
      
