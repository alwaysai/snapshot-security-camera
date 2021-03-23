# Snapshot Security Camera App

This app expands on the *realtime_object_detector* starter app to build a
simple security camera app that takes a picture of each new person who enters
the frame. The full tutorial can be found on the
[alwaysAI blog](https://alwaysai.co/blog/detect-people-using-alwaysai).

## Setup

This app requires an alwaysAI account. Head to the
[Sign up page](https://www.alwaysai.co/dashboard) if you don't have an account
yet. Follow the instructions to install the alwaysAI toolchain on your
development machine.

## Usage

Once you have the alwaysAI tools installed, run the following CLI commands at
the top level of the repo:

```
aai app configure
aai app install
aai app start
```

Images will be saved in the app directory with a person detection index and the
timestamp. The timezone is set in the `Dockerfile` and may need to be changed
based on your location.

Once started, a link will appear for the Streamer which displays the camera
feed and detections in your browser:

```
Loaded model:
alwaysai/mobilenet_ssd

Engine: Engine.DNN
Accelerator: Accelerator.GPU

Labels:
['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

[INFO] Streamer started at http://localhost:5000
```

## Support

* [Docs](https://alwaysai.co/docs)
* [RealSense API](https://alwaysai.co/docs/edgeiq_api/real_sense.html)
* [Community Discord](https://discord.gg/R2uM36U)
* [Email](contact@alwaysai.co)
