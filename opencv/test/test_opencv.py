# description: this script creates a png image using OpenCV and saves it to disk.
# to test the image, the script is
import cv2
import numpy as np

# create a black image
image = np.zeros((512, 512, 3), dtype=np.uint8)

# draw a white rectangle
cv2.rectangle(image, (100, 100), (400, 400), (255, 255, 255), -1)

# showing an image will not work on a headless environment so the test saves the image to disk instead
cv2.imwrite('/app/output.png', image)

print("an output.png image has been created and saved to disk")
