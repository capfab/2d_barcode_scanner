import cv2
import barcode_reader

from barcode_reader import MarkerDetector

image_path = 'F:/Intel/3.jpg'
frame = cv2.imread(image_path, cv2.IMREAD_COLOR)

cv2.imshow('a',frame)
cv2.waitKey()

if frame is None:
    raise ValueError("Image could not be read")

detector = MarkerDetector(min_contour_length_allowed=10000)
detected_markers = detector.process_frame(frame)

print("%d markers detected:" % len(detected_markers))
for marker in detected_markers:
    print(marker.points)