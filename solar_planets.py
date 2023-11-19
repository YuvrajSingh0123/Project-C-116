import cv2
image = cv2.imread("solar-system.jpg")
cv2.puText(image,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    0.5,
    (255,255,255)
)
cv2.imshow("Sun",image)
cv2.waitKey(0)