"""
U2 app
"""
import cv2
import Images
import imageWindow
import filterWindow
import sobelScharrWindow
import cannyWindow

"""
Main function
"""

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
