# TASK 4 — Object Detection and Tracking
## Beginner Student Version — VIDEO FILE


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

Search for:

**people walking**

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
<img width="1125" height="387" alt="image" src="https://github.com/user-attachments/assets/d90daa07-9c66-4726-aacc-e9d7f6758a1e" />

---


That's the core idea of Task 4.
