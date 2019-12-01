import cv2

image = cv2.imread("Y2.jpg")
cv2.namedWindow('Orjinal', cv2.WINDOW_NORMAL)
cv2.namedWindow('Blur', cv2.WINDOW_NORMAL)
blur_image = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow("Orjinal",image)
cv2.imshow("Blur",blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
