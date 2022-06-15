#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from app.video import video

_f = 0  # frame counter

cap = cv2.VideoCapture(f"{video.path_o}{video.name}.{video.format}")  # Open video
fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Aspect ratio of original video
w_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

new_width,new_height  = 520, 1080  # for vertical video

x, y = int(w_frame / 2), int(h_frame / 2)  # Center of new cropped video

# output
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(
    f"{video.path_c}c_{video.name}.{video.format}", fourcc, fps, (new_height, new_width)
)

while cap.isOpened():
    ret, frame = cap.read()
    _f += 1  # Counting frames

    # Avoid problems when video finish
    if ret:
        crop_frame = frame[y : y + h_frame, x : x + new_width]

        if video.show_progress:
            print(f"{int(_f * 100 / frames)} %")  # frames cropped

        out.write(crop_frame)  # Save video

        if video.show_video:
            cv2.imshow("frame", frame)
            cv2.imshow("cropped", crop_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
