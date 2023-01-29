## Project

Execute the `app.py` file to start the application:  
<small>The other files are only parts of _app.py_ and are not executables.</small>

```sh
python3 ./app.py
```

### TODO

- [x] continuous video analysis (e.g. of a built-in/connected webcam)
- [x] during the analysis the program tries to recognize bodies of people
- [ ] if a body is recognized, a recording of the video starts, which is saved on the hard disk as a video file after "loss of recognition" of the body
- [x] ~~furthermore, after a successful recognition of a body, the face recognition is started~~ ==> now happens simultaneously
- [x] if the person looks into the camera and a face is recognized, a recording of the face is stored as JPG on the hard disk
- [x] in the video feed as well as on the recordings (video & JPG) there is a continuous timestamp to track when the recordings were taken
- [x] (optional) there is additionally a live view in an OpenCV window

### Keyboard Shortcuts

- `ESC` quits the program

### Requirements

- Python version `v3.10.4`
- Opencv-python-rolling `v5.0.0.20221015`

  or higher.
