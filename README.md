# Machine Vision – University Course – BHT Berlin

With the help of [OpenCv](https://opencv.org/).  
Use Python version `3.10.4` or higher.

## U1 (Exercise 1)

- Read in the image "lena.bmp", convert the image to a gray-scale image, display it on the monitor.
- Design a callback function to analyze mouse activity within the window, with which a colored framed rectangle is drawn into the image by pressing the left mouse button, the size of which is defined by dragging the mouse and fixed when the left mouse button is released.
- This process is to be repeated as often as desired by pressing the left mouse button within the image field and terminated by pressing a key, e.g. "ESC" (end of program). A previously drawn rectangle is to be deleted before drawing a new one.
- Display the image content enclosed by the frame zoomed in another image field. The magnification factor is to be adjustable between 1 and 4 by means of a slider.
- Use another slider to display the zoomed image content with adjustable false colors, as a gray-scale image or inverted gray-scale image.
- When displaying as a gray-scale image, the zoom factor is to be written into the new image field.

## U2 (Exercise 2)

- Read the image "stop.jpg" as a gray value image
- Filter the image with adjustable filter functions and operator parameters
  - No filter
  - Gaussian low pass (parameter: σ)
  - Median filter (parameter: size)
- Find outlines using
  - Sobel operator, Scharr operator
    - Maximum value of the amounts of the partial derivatives
    - Sum of the amounts of the partial derivatives
  - Canny operator
    - Choice of lower and upper threshold value
  - Difference of Gaussian (DoG)
    - Make the cutoff frequency of the low pass filter adjustable
- Binarize the outline image at an adjustable threshold value for
  - Sobel operator
  - Scrape operator
  - DoG
- Select operator, filter function and filter size by slider
- Visualize partial results (selection by slider)
  - Sobel: |X'|, |Y'|, Sum(|X'|,|Y'|) resp. Max(|X'|,|Y'|), Bin
  - Scharr: |X'|, |Y'|, Sum(|X'|,|Y'|) resp. Max(|X'|,|Y'|), Bin
  - DoG: Lowpass1, Lowpass2, Difference, Bin
- Hints:
  - The target images for the foldings (Sobel/Scharr operator) are signed
  - The cutoff frequency of the Gaussian low-pass filters should be adjustable from 0.1 ≤ σ ≤ 6.0

## U3 (Exercise 3)

- The images `DOWxx.png` show rubber bales which are partly contaminated by machine oil from a press.
- Contaminations show up as dark spots on the light-colored bale.
- Impurities are considered to be defects if the gray value of the spots is less than than 70% of the mean gray value of the bale.
- At the edge of the bale, an area of 15 pixels circumferentially should be excluded from the analysis.
- Detect impurities and determine the summary area of all impurities relative to the bale area.  
  Output Example:
  ```sh
    Mask area: 1337px
    Mask gray mean: x.xxx
    Error threshold: xx.xxx (70%)
    Error area: 42px
    Faulty area to mask: x.xxx%
  ```

## U4 (Exercise 4)

- Read the images `Fischx.png`.
- Find the contour, approximate it as a polygon with adjustable resolution and determine the convex hull of the object.
- Determine the features for the different representations:
  - Object centroid
  - Circumscribing axis-parallel rectangle
  - Smallest circumscribing rectangle
  - Smallest circumscribing circle
- Draw the features found in color in the original image and describe them on the console.
