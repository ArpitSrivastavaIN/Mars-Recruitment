#EC24I1001
#Arpit Srivastava

''''''

import cv2
import numpy as np

def detect_arrow(image_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

    if len(approx) == 7:  # Arrows typically have 7 sides
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
        print("Arrow detected!")

        # Calculate bounding box
        x, y, w, h = cv2.boundingRect(approx)
        perceived_width = max(w, h)
        
        # Find distance (Function to be implemented)
        distance = find_distance(perceived_width)
        print(f"Estimated Distance: {distance:.2f} cm")

    # Show the result
    cv2.imshow('Detected Arrow', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def find_distance(perceived_width):
    # Implement the function to calculate distance
    focal_length = 7
    pass

# Provide the path to your image
image_path = 'arrow.jpg'
detect_arrow(image_path)
