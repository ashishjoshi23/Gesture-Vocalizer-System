import cv2
import numpy as np
import os

mode = 'trainingData'
directory = 'dataSet/' + mode + '/'
minValue = 70

capture = cv2.VideoCapture(0)
interrupt = -1

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {
        'zero': len(os.listdir(directory + "/0")),
        'a': len(os.listdir(directory + "/A")),
        'b': len(os.listdir(directory + "/B")),
        'c': len(os.listdir(directory + "/C")),
        'd': len(os.listdir(directory + "/D")),
        'e': len(os.listdir(directory + "/E")),
        'f': len(os.listdir(directory + "/F")),
        'g': len(os.listdir(directory + "/G")),
        'h': len(os.listdir(directory + "/H")),
        'i': len(os.listdir(directory + "/I")),
        'j': len(os.listdir(directory + "/J")),
        'k': len(os.listdir(directory + "/K")),
        'l': len(os.listdir(directory + "/L")),
        'm': len(os.listdir(directory + "/M")),
        'n': len(os.listdir(directory + "/N")),
        'o': len(os.listdir(directory + "/O")),
        'p': len(os.listdir(directory + "/P")),
        'q': len(os.listdir(directory + "/Q")),
        'r': len(os.listdir(directory + "/R")),
        's': len(os.listdir(directory + "/S")),
        't': len(os.listdir(directory + "/T")),
        'u': len(os.listdir(directory + "/U")),
        'v': len(os.listdir(directory + "/V")),
        'w': len(os.listdir(directory + "/W")),
        'x': len(os.listdir(directory + "/X")),
        'y': len(os.listdir(directory + "/Y")),
        'z': len(os.listdir(directory + "/Z")),
    }
    
    # Display counts on frame
    y_pos = 60
    for key, value in count.items():
        cv2.putText(frame, f"{key.upper()} : {value}", (10, y_pos), 
                   cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
        y_pos += 10
    
    # ROI coordinates
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    
    # Draw ROI
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    
    # Extract ROI
    roi = frame[y1:y2, x1:x2]
    
    # Image processing
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY_INV, 11, 2)
    ret, test_image = cv2.threshold(th3, minValue, 255, 
                                   cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    test_image = cv2.resize(test_image, (300, 300))
    cv2.imshow("Frame", frame)
    cv2.imshow("Processed", test_image)
    
    # Save images
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # ESC key
        break
    elif interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory + '0/' + str(count['zero']) + '.jpg', roi)
    elif interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory + 'A/' + str(count['a']) + '.jpg', roi)
    # Add similar conditions for other letters...

capture.release()
cv2.destroyAllWindows()
