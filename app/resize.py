#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from app.video import myVideo

_f = 0  # frame counter

cap = cv2.VideoCapture(f"{myVideo.path_o}{myVideo.name}.{myVideo.format}")  # Open video
fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Aspect ratio of original video
w_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h_frame = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

new_width,new_height  = 520, 1080  # for vertical video

x, y = int(w_frame / 2), int(h_frame / 2)  # Center of new cropped video

# output
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(
    f"{myVideo.path_c}c_{myVideo.name}.{myVideo.format}", fourcc, fps, (new_height, new_width)
)

while cap.isOpened():
    ret, frame = cap.read()
    _f += 1  # Counting frames

    # Avoid problems when video finish
    if ret:
        crop_frame = frame[y : y + h_frame, x : x + new_width]

        if myVideo.PROGRESS:
            print(f"{int(_f * 100 / frames)} %")  # frames cropped

        out.write(crop_frame)  # Save video

        if myVideo.DISPLAY:
            cv2.imshow("frame", frame)
            cv2.imshow("cropped", crop_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()


git remote add origin https://github.com/SamuelSHernandez/test.git
git branch -M main
git push -u origin main