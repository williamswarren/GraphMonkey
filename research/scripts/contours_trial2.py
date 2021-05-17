pic = '/Users/warrenwilliams/Documents/School/UCSC Extension/Quarter 3/mlproject/research/test_output_images/TRUNC.jpg'
import cv2 # Computer vision library
 
# Read the color image
image = cv2.imread(pic)
 
# Make a copy
new_image = image.copy()
 
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Display the grayscale image
cv2.imshow('Gray image', gray)  
cv2.waitKey(0) # Wait for keypress to continue
cv2.destroyAllWindows() # Close windows
 
# Convert the grayscale image to binary
ret, binary = cv2.threshold(gray, 100, 255, 
  cv2.THRESH_OTSU)
 
# Display the binary image
cv2.imshow('Binary image', binary)
cv2.waitKey(0) # Wait for keypress to continue
cv2.destroyAllWindows() # Close windows
 
# To detect object contours, we want a black background and a white 
# foreground, so we invert the image (i.e. 255 - pixel value)
inverted_binary = ~binary
cv2.imshow('Inverted binary image', inverted_binary)
cv2.waitKey(0) # Wait for keypress to continue
cv2.destroyAllWindows() # Close windows
 
# Find the contours on the inverted binary image, and store them in a list
# Contours are drawn around white blobs.
# hierarchy variable contains info on the relationship between the contours
contours, hierarchy = cv2.findContours(inverted_binary,
  cv2.RETR_TREE,
  cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)     
# Draw the contours (in red) on the original image and display the result
# Input color code is in BGR (blue, green, red) format
# -1 means to draw all contours
with_contours = cv2.drawContours(image, contours, -1,(255,0,255),3)
cv2.imshow('Detected contours', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Show the total number of contours that were detected
print('Total number of contours detected: ' + str(len(contours)))
 
# Draw just the first contour
# The 0 means to draw the first contour
first_contour = cv2.drawContours(new_image, contours, 0,(255,0,255),3)
cv2.imshow('First detected contour', first_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Draw a bounding box around the first contour
# x is the starting x coordinate of the bounding box
# y is the starting y coordinate of the bounding box
# w is the width of the bounding box
# h is the height of the bounding box
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(first_contour,(x,y), (x+w,y+h), (255,0,0), 5)
cv2.imshow('First contour with bounding box', first_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()

box_list = [] 
# Draw a bounding box around all contours
for c in contours:
  x, y, w, h = cv2.boundingRect(c)
 
    # Make sure contour area is large enough
  if (cv2.contourArea(c)) < 10000 and (cv2.contourArea(c)) > 500:
    cv2.rectangle(with_contours,(x,y), (x+w,y+h), (255,0,0), 5)
    box_list.append((x, y, w, h))
print(box_list)     
cv2.imshow('All contours with bounding box', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
