# SORT tracker
# This file is used by main.py.
# You normally do not need to edit it.

import numpy as np
from filterpy.kalman import KalmanFilter
from scipy.optimize import linear_sum_assignment


def iou_batch(boxes1, boxes2):

    boxes1 = np.expand_dims(boxes1, 1)
    boxes2 = np.expand_dims(boxes2, 0)

    x1 = np.maximum(boxes1[..., 0], boxes2[..., 0])
    y1 = np.maximum(boxes1[..., 1], boxes2[..., 1])
    x2 = np.minimum(boxes1[..., 2], boxes2[..., 2])
    y2 = np.minimum(boxes1[..., 3], boxes2[..., 3])

    width = np.maximum(0, x2 - x1)
    height = np.maximum(0, y2 - y1)

    intersection = width * height

    area1 = (
        (boxes1[..., 2] - boxes1[..., 0]) *
        (boxes1[..., 3] - boxes1[..., 1])
    )

    area2 = (
        (boxes2[..., 2] - boxes2[..., 0]) *
        (boxes2[..., 3] - boxes2[..., 1])
    )

    union = area1 + area2 - intersection

    return intersection / (union + 1e-6)


def box_to_z(box):

    width = box[2] - box[0]
    height = box[3] - box[1]

    center_x = box[0] + width / 2
    center_y = box[1] + height / 2

    area = width * height
    ratio = width / (height + 1e-6)

    return np.array(
        [center_x, center_y, area, ratio]
    ).reshape((4, 1))


def x_to_box(x):

    width = np.sqrt(max(0, x[2] * x[3]))
    height = x[2] / (width + 1e-6)

    return np.array([
        x[0] - width / 2,
        x[1] - height / 2,
        x[0] + width / 2,
        x[1] + height / 2
    ]).reshape((1, 4))


class KalmanBoxTracker:

    count = 0

    def __init__(self, box):

        self.kf = KalmanFilter(dim_x=7, dim_z=4)

        self.kf.F = np.array([
            [1,0,0,0,1,0,0],
            [0,1,0,0,0,1,0],
            [0,0,1,0,0,0,1],
            [0,0,0,1,0,0,0],
            [0,0,0,0,1,0,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,0,1]
        ])

        self.kf.H = np.array([
            [1,0,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,0,1,0,0,0]
        ])

        self.kf.R[2:, 2:] *= 10
        self.kf.P[4:, 4:] *= 1000
        self.kf.P *= 10
        self.kf.Q[-1, -1] *= 0.01
        self.kf.Q[4:, 4:] *= 0.01

        self.kf.x[:4] = box_to_z(box)

        self.time_since_update = 0
        self.id = KalmanBoxTracker.count + 1
        KalmanBoxTracker.count += 1

        self.hits = 0
        self.hit_streak = 0
        self.age = 0
        self.history = []

    def update(self, box):

        self.time_since_update = 0
        self.history = []
        self.hits += 1
        self.hit_streak += 1

        self.kf.update(box_to_z(box))

    def predict(self):

        self.kf.predict()

        self.age += 1
        self.time_since_update += 1

        self.history.append(x_to_box(self.kf.x))

        return self.history[-1]

    def get_state(self):

        return x_to_box(self.kf.x)


def match_detections(detections, trackers, threshold):

    if len(trackers) == 0:

        return (
            np.empty((0, 2), dtype=int),
            np.arange(len(detections)),
            np.empty((0,), dtype=int)
        )

    matrix = iou_batch(detections, trackers)

    rows, columns = linear_sum_assignment(-matrix)

    matches = []

    for row, column in zip(rows, columns):

        if matrix[row, column] >= threshold:
            matches.append([row, column])

    if len(matches) > 0:
        matches = np.array(matches, dtype=int)
    else:
        matches = np.empty((0, 2), dtype=int)

    unmatched_detections = [
        i for i in range(len(detections))
        if i not in matches[:, 0]
    ]

    unmatched_trackers = [
        i for i in range(len(trackers))
        if i not in matches[:, 1]
    ]

    return (
        matches,
        np.array(unmatched_detections),
        np.array(unmatched_trackers)
    )


class Sort:

    def __init__(
        self,
        max_age=10,
        min_hits=1,
        iou_threshold=0.3
    ):

        self.max_age = max_age
        self.min_hits = min_hits
        self.iou_threshold = iou_threshold

        self.trackers = []

    def update(self, detections):

        trackers = []

        for tracker in self.trackers:

            prediction = tracker.predict()[0]
            trackers.append(prediction)

        trackers = np.array(trackers)

        if len(trackers) == 0:
            trackers = np.empty((0, 4))

        matched, unmatched_detections, unmatched_trackers = (
            match_detections(
                detections[:, :4],
                trackers,
                self.iou_threshold
            )
        )

        for match in matched:

            detection_index = match[0]
            tracker_index = match[1]

            self.trackers[tracker_index].update(
                detections[detection_index, :4]
            )

        for index in unmatched_detections:

            self.trackers.append(
                KalmanBoxTracker(
                    detections[index, :4]
                )
            )

        output = []

        for tracker in self.trackers:

            box = tracker.get_state()[0]

            if tracker.time_since_update < 1:

                output.append([
                    box[0],
                    box[1],
                    box[2],
                    box[3],
                    tracker.id
                ])

        self.trackers = [
            tracker for tracker in self.trackers
            if tracker.time_since_update <= self.max_age
        ]

        if len(output) > 0:
            return np.array(output)

        return np.empty((0, 5))
