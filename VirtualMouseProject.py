import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction for movement region
smoothening = 7  # For smooth mouse movement
##########################

pTime = 0
plocX, plocY = 0, 0  # Previous location
clocX, clocY = 0, 0  # Current location

# Open the webcam
cap = cv2.VideoCapture(0)  # Try 1 or 2 if 0 doesn't work
cap.set(3, wCam)  # Width
cap.set(4, hCam)  # Height

# Initialize hand detector
detector = htm.handDetector(maxHands=1)

# Get screen size
wScr, hScr = autopy.screen.size()
print(f"Screen Size: {wScr}x{hScr}")

while True:
    # 1. Read webcam frame
    success, img = cap.read()
    if not success or img is None:
        print("❌ Failed to read frame from webcam.")
        continue

    # 2. Find hands in the frame
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 3. If landmarks are detected
    if len(lmList) != 0:
        # Get positions of index and middle finger tips
        x1, y1 = lmList[8][1:]  # Index finger
        x2, y2 = lmList[12][1:]  # Middle finger

        # 4. Check which fingers are up
        fingers = detector.fingersUp()

        # Draw movement area
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        # 5. Only index finger up => Move mouse
        if fingers[1] == 1 and fingers[2] == 0:
            # Convert coordinates from camera to screen
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # Smooth the values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move the mouse
            try:
                autopy.mouse.move(wScr - clocX, clocY)  # Flip X axis
            except Exception as e:
                print("❌ Mouse move error:", e)

            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 6. Both index and middle fingers up => Click
        if fingers[1] == 1 and fingers[2] == 1:
            # Calculate distance between tips
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
                time.sleep(0.2)  # Small delay to avoid multiple clicks

    # 7. Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # 8. Show the image
    cv2.imshow("Virtual Mouse", img)

    # 9. Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
cv2.destroyAllWindows()
