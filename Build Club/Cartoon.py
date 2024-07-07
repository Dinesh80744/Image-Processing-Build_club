import cv2
import argparse
import sys

def cartoonizer(image_name):
    # Load the image to cartoonize.
    image_to_animate = cv2.imread(image_name)

    # Apply a bilateral filter to smoothen the image while preserving edges.
    smoothened_image = cv2.bilateralFilter(image_to_animate, d=9, sigmaColor=75, sigmaSpace=75)

    # Convert image to gray and create an edge mask using adaptive thresholding.
    gray_image = cv2.cvtColor(smoothened_image, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Combine the smoothened image and the edge mask to create a cartoon-like effect.
    to_cartoon = cv2.bitwise_and(smoothened_image, smoothened_image, mask=edges)

    # Save the cartoon image in the current directory.
    cartooned_image = f"cartooned_{image_name}"
    cv2.imwrite(cartooned_image, to_cartoon)

    # Display the result.
    cv2.imshow("Cartooned Image", to_cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image_path = "Leo-Dicarprio-Face-Front-ipad.jpg"
    cartoonizer(input_image_path)
    cv2.imshow("Origina Image",input_image_path)
