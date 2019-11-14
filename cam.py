# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:30:03 2019

@author: GH057R007
"""


import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import cv2
import numpy as np
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
vcap = cv2.VideoCapture("rtsp://172.30.16.149:8080/camera", cv2.CAP_FFMPEG)
while(1):
    ret, frame = vcap.read()
    if ret == False:
        print("Frame is empty")
        break;
    else:
        cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)