"""
Image Detector
"""

from GUI.Window import Window


def analyzeImage(name, image):
    print(f'(analyzeImage) Analyzing {name}')
    window = Window(name)
    window.show(name, image)
