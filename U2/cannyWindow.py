from Window import Window
from Images import Images
from TrackbarValues import TrackbarValues
from utils import runCanny

CannyWindow = None
thresholdTrackbar = 'Threshold'
thresholdValueRange = (0, 300)

"""
Canny Utils
"""


def updateCannyWindow():
    match TrackbarValues.operator:
        case 0:
            TrackbarValues.updateThreshold(0)
            CannyWindow.setTrackbar(
                thresholdTrackbar + ' L: ', TrackbarValues.threshold)

            TrackbarValues.updateThreshold2(0)
            CannyWindow.setTrackbar(
                thresholdTrackbar + ' H: ', TrackbarValues.displayValue)
            CannyWindow.show('Canny', Images.filtered)
        case 3:
            # TODO: show Canny
            runCanny()
            CannyWindow.show('Canny', Images.canny)
        case _:
            pass


"""
Trackbar Functions
"""


def thresholdOnChange(value):
    if TrackbarValues.threshold == value:
        return

    print(f'(thresholdOnChange) {TrackbarValues.threshold} to {value}')
    TrackbarValues.updateThreshold(value)

    updateCannyWindow()


def threshold2OnChange(value):
    if TrackbarValues.threshold2 == value:
        return

    print(f'(threshold2OnChange) {TrackbarValues.threshold2} to {value}')
    TrackbarValues.updateThreshold2(value)

    updateCannyWindow()


"""
Window Functions
"""


def createCannyWindow():
    global CannyWindow

    if CannyWindow != None:
        CannyWindow.destroy()

    CannyWindow = Window('Operator Canny', scale=0.5, offset=(
        round(Images.filtered.shape[0]*0.4), 0))
    CannyWindow.addTrackbar(thresholdTrackbar + ' L: ',
                            thresholdValueRange, thresholdOnChange)
    CannyWindow.addTrackbar(thresholdTrackbar + ' H: ',
                            thresholdValueRange, threshold2OnChange)
    return CannyWindow
