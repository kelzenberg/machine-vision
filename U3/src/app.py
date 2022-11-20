"""
U3 app
"""
import cv2
from GUI.Window import Window

print('(main) Window loaded.')

"""
Main function
"""

mainWindow = Window('Test')

print('(main) Press ESC to exit...')
while cv2.waitKey(0) != 27:
    pass

print('(main) Closing all windows.')
cv2.destroyAllWindows()
