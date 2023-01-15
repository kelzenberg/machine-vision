# Analysis of algorithms

## Findings

For both matching algorithms using an image with a smaller base width to the image compared against results in better outcomes in detecting the depth of the image.

For example:  
_Comparing view0 (left image) with view2 (right image) resulted in a better stereo-detection than comparing view0 against e.g. view4 (right image)._

**Furthermore, the SGBM tended to perform better than the default BM.**

The following settings returned the best stereo-detection results:

### Block Matcher

- **Matcher:** `BM`
- **Right Image:** `view2`
- **Disparity:** `112`
- **BlockSize:** `19`
- **PreFilterSize:** `5`
- **PreFilterCap:** `8`
- **TextureThreshold:** `8`
- **MinDisparity:** `4`

### Semi-global Block Matcher

- **Matcher:** `SGBM`
- **Right Image:** `view2`
- **Disparity:** `112`
- **BlockSize:** `13`
- **PreFilterSize:** `5`
- **PreFilterCap:** `10`
- **TextureThreshold:** `8`
- **MinDisparity:** `9`
