# TASK 4: Object Detection and Tracking
# Beginner Student Version
# Using a VIDEO FILE (No Webcam Needed)
# YOLO + OpenCV + SORT

import cv2
import numpy as np
from ultralytics import YOLO
from sort.sort import Sort


# --------------------------------------------------
# STEP 1: Load the YOLO model
# --------------------------------------------------
# YOLO detects objects such as people, cars, dogs, etc.
model = YOLO("yolov8n.pt")


# --------------------------------------------------
# STEP 2: Start the SORT tracker
# --------------------------------------------------
# SORT gives objects tracking IDs.
tracker = Sort()


# --------------------------------------------------
# STEP 3: Open our VIDEO FILE
# --------------------------------------------------
# Put your video inside the "videos" folder.
#
# IMPORTANT:
# Rename your video to:
# test.mp4
#
# Then this line will work without changing anything.
video = cv2.VideoCapture("videos/test.mp4")


# Check if the video opened successfully.
if not video.isOpened():
    print("ERROR: Could not open the video.")
    print("Make sure your video is inside the videos folder")
    print("and is named test.mp4")
    exit()


# --------------------------------------------------
# STEP 4: Read the video frame by frame
# --------------------------------------------------
while True:

    # Read one frame from the video.
    success, frame = video.read()

    # If there are no more frames, stop.
    if not success:
        print("Video finished!")
        break


    # --------------------------------------------------
    # STEP 5: Detect objects using YOLO
    # --------------------------------------------------
    results = model(frame, verbose=False)

    # This list stores the detected objects.
    detections = []


    # Go through YOLO's results.
    for result in results:

        # Get all detected boxes.
        boxes = result.boxes

        # Check every detected object.
        for box in boxes:

            # Confidence = how sure YOLO is.
            confidence = float(box.conf[0])

            # Ignore weak detections.
            if confidence < 0.40:
                continue

            # Get the box coordinates.
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Save the detection for SORT.
            detections.append(
                [x1, y1, x2, y2, confidence]
            )


    # Convert detections to a NumPy array.
    if len(detections) > 0:
        detections = np.array(detections)
    else:
        detections = np.empty((0, 5))


    # --------------------------------------------------
    # STEP 6: Track the detected objects
    # --------------------------------------------------
    tracked_objects = tracker.update(detections)


    # --------------------------------------------------
    # STEP 7: Draw boxes and tracking IDs
    # --------------------------------------------------
    for object_data in tracked_objects:

        # Get the box coordinates and tracking ID.
        x1, y1, x2, y2, object_id = object_data

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        object_id = int(object_id)

        # Draw a green rectangle.
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Write the tracking ID.
        label = "Object ID: " + str(object_id)

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )


    # --------------------------------------------------
    # STEP 8: Display the final video
    # --------------------------------------------------
    cv2.imshow(
        "Task 4 - Object Detection and Tracking",
        frame
    )


    # Press Q to stop early.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# --------------------------------------------------
# STEP 9: Close the video window
# --------------------------------------------------
video.release()
cv2.destroyAllWindows()

print("Program finished!")
