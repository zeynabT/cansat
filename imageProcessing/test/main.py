import cv2
# import normal
pic1 = cv2.imread('me.jpg')
# import gray scale
pic2 = cv2.imread('me.jpg', cv2.IMREAD_GRAYSCALE)
# import colord
pic3 = cv2.imread('me.jpg', cv2.IMREAD_COLOR)
# import not change
pic4 = cv2.imread('me.jpg', cv2.IMREAD_UNCHANGED)
# show pic < 1 name of window and 2 is pic

# window size do not change
cv2.namedWindow('auto_win', cv2.WINDOW_AUTOSIZE)

# window size can be change
cv2.namedWindow('normal', cv2.WINDOW_NORMAL)

# show image
cv2.imshow('auto_win', pic1)
cv2.imshow('normal', pic2)
# cv2.imshow('pic3', pic3)
# cv2.imshow('pic4', pic4)
# to wait window
cv2.imwrite('gray.png',pic2)
cv2.waitKey(0)
