"""
U2 app
"""
import cv2
import images
import imageWindow
import filterWindow
import edgesWindow

"""
Main function
"""

print('(Main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(Main) Closing all windows.')
cv2.destroyAllWindows()
