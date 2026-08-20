# TASK 4 — Object Detection and Tracking
## Beginner Student Version — VIDEO FILE

### ⭐ Important

This version uses a **saved video file**.

You do **NOT** need to open or use your webcam.

The project uses:

- Python
- OpenCV
- YOLO
- SORT

---

# 📁 Project Structure

After extracting the ZIP, you will have:

```text
Task4_Beginner_Video_Object_Detection_Tracking/
│
├── main.py
├── requirements.txt
├── README.md
│
├── sort/
│   └── sort.py
│
└── videos/
    └── test.mp4
```

The `videos` folder is where you put your downloaded video.

---

# 🎥 STEP 1 — Download a video

Good websites for this assignment are:

### Pexels

Search for:

**people walking**

Pexels has free stock videos, and its license says videos can be downloaded and used for free. Attribution is not required. 

https://www.pexels.com/search/videos/people%20walking/

### Pixabay

Search for:

**people walking**

Pixabay has thousands of free people-walking videos.

https://pixabay.com/videos/search/people%20walking/

### Mixkit

Mixkit also has free people-walking stock videos.

https://mixkit.co/free-stock-video/people-walking/

---

# 🎯 What video should you choose?

For your first test, choose:

- 10–30 seconds long
- people walking
- good lighting
- objects clearly visible
- preferably 720p or 1080p
- landscape video if possible

A video with **2–5 people walking** is ideal because you can clearly see the tracking IDs.

---

# 📥 STEP 2 — Put the video in the project

After downloading your video:

1. Open the project folder.
2. Open the `videos` folder.
3. Put your downloaded video there.
4. Rename it:

```text
test.mp4
```

So you should have:

```text
videos/
└── test.mp4
```

### ⚠️ Make sure it is actually `.mp4`

Not:

```text
test.mp4.mp4
```

and not:

```text
test.mov
```

For this beginner version, use an MP4 video.

---

# 💻 STEP 3 — Open the project in VS Code

Open VS Code.

Go to:

**File → Open Folder**

Select:

```text
Task4_Beginner_Video_Object_Detection_Tracking
```

---

# ⌨️ STEP 4 — Open the terminal

In VS Code:

**Terminal → New Terminal**

A terminal will appear at the bottom.

---

# 📦 STEP 5 — Install the libraries

Type:

```bash
pip install -r requirements.txt
```

Press Enter.

Wait until installation finishes.

---

# ▶️ STEP 6 — Run the program

Type:

```bash
python main.py
```

Press Enter.

The first time you run it, YOLO may automatically download:

```text
yolov8n.pt
```

This is normal.

---

# 👀 STEP 7 — Watch the result

Your video will open in a new window.

You should see green boxes around detected objects.

You should also see:

```text
Object ID: 1
Object ID: 2
Object ID: 3
```

The IDs are created by SORT.

---

# 🛑 STEP 8 — Stop the program

Press:

```text
Q
```

on your keyboard.

You can also wait for the video to finish.

---

# 🧠 How the project works

The basic process is:

```text
Video File
     ↓
   OpenCV
     ↓
Read one frame
     ↓
    YOLO
     ↓
Detect objects
     ↓
Bounding Boxes
     ↓
    SORT
     ↓
Tracking IDs
     ↓
Display result
```

---

# 📚 Simple explanation

## What is OpenCV?

OpenCV is a Python library used for computer vision.

In our project, OpenCV:

- opens the video
- reads frames
- draws rectangles
- displays the final video

---

## What is YOLO?

YOLO means:

**You Only Look Once**

It is a pre-trained object detection model.

It can detect things such as:

```text
person
car
dog
cat
bicycle
chair
bottle
```

---

## What is a bounding box?

A bounding box is a rectangle drawn around an object.

For example:

```text
+----------------+
|     PERSON     |
|                |
+----------------+
```

---

## What is SORT?

SORT means:

**Simple Online and Realtime Tracking**

YOLO detects objects.

SORT then follows those objects between video frames.

---

## What is a tracking ID?

A tracking ID is a number given to an object.

For example:

```text
Person → ID 1
Person → ID 2
Car    → ID 3
```

If Person 1 moves to another position, the program tries to keep the same ID.

---

# 📝 Assignment Requirement Mapping

| Assignment requirement | Our project |
|---|---|
| Real-time/video input | OpenCV |
| Webcam or video file | Video file |
| Pre-trained model | YOLOv8 |
| Object detection | YOLO |
| Bounding boxes | OpenCV |
| Object tracking | SORT |
| Tracking IDs | SORT |
| Labels/IDs | OpenCV |
| Real-time display | OpenCV |

---

# 🎤 Very Simple Viva Answers

### Q: What is the purpose of this project?

**Answer:**

This project detects and tracks objects in a video using YOLO, OpenCV and SORT.

### Q: Why did you use YOLO?

**Answer:**

I used YOLO because it is a pre-trained object detection model and it is fast enough for real-time applications.

### Q: What does OpenCV do?

**Answer:**

OpenCV reads the video frame by frame, draws bounding boxes and displays the output.

### Q: What does SORT do?

**Answer:**

SORT tracks detected objects and gives them unique tracking IDs.

### Q: What is a bounding box?

**Answer:**

A bounding box is a rectangle drawn around a detected object.

### Q: What is an object tracking ID?

**Answer:**

It is a unique number used to identify and follow an object across different video frames.

---

# ⚠️ Common Problems

## "Could not open the video"

Check that:

```text
videos/test.mp4
```

exists.

The folder name must be:

```text
videos
```

and the file must be:

```text
test.mp4
```

---

## YOLO is downloading something

That's normal.

The first time you run the program, YOLO may download its pre-trained model.

Wait for it to finish.

---

## The program is slow

Try a shorter or lower-resolution video.

For a beginner assignment, 720p is more than enough.

---

# ⭐ What you actually need to understand

You don't need to memorize the entire SORT algorithm.

Understand this:

```text
OpenCV → reads video
YOLO → detects objects
SORT → tracks objects
OpenCV → displays result
```

That's the core idea of Task 4.
