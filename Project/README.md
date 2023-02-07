# Project

Continuous people recognition and recording of a live (web)cam feed.  
<sub>Use case: Software for an offline home intruder security camera.</sub>

## Requirements

- Python version `v3.10.4`
- Opencv-python-rolling `v5.0.0.20221015`

  or higher.

## Features

- [x] Continuous video analysis (e.g. of a feed from a built-in/connected webcam)
- [x] A live view in an OpenCV window to monitor the feed
- [x] During the analysis the program tries to recognize
  - upper bodies and
  - faces of people
- [x] If a torso or face is recognized, a recording of the live feed starts on a timer (e.g. 10s), which is then saved on the hard disk as a video file afterwards (e.g. `./records/2023-02-07T13/30/44_recording.mp4`)
- [x] If the person looks into the camera and a face is recognized, a recording of the face is additionally stored as an image on the hard disk (e.g. `./records/2023-02-07T13/30/44_face-0.jpg`)
- [x] In the live video feed as well as on the recordings (videos & images) there is a continuous timestamp printed, to trace back when the recordings were taken
- [x] Timestamps are also used in naming the outputted files
- [x] The camera feed as well as the functions writing files to hard disk are threaded and run asynchronously to unblock the main thread for the OpenCV image analysis

## How to run

Execute the `app.py` file to start the application:  
<small>The other files are only parts of _app.py_ and are not executables.</small>

```sh
python3 ./app.py
```

## Keyboard Shortcuts

- `ESC` quits the program
