# Snapshot Security Camera App
This app expands on the *realtime_object_detector* starter app to build a simple security camera app that takes a picture of each new person who enters the frame. The full tutorial can be found on the [alwaysAI blog](https://learn.alwaysai.co/detect-people-using-alwaysai).

## Setup
This app requires an alwaysAI account. Head to the [Sign up page](https://www.alwaysai.co/dashboard) if you don't have an account yet. Follow the instructions to install the alwaysAI toolchain on your development machine.

Next, create an empty project to be used with this app. When you clone this repo, you can run `aai app configure` within the repo directory and your new project will appear in the list.

## Usage
Once you have the alwaysAI tools installed and the new project created, run the following CLI commands at the top level of the repo:

To set the project, and select the target device run:

```
aai app configure
```

To build your app and deploy to the target device:

```
aai app deploy
```

To start the app:

```
aai app start
```

Images will be saved in the app directory with a person detection index and the timestamp. The timezone is set in the `Dockerfile` and may need to be changed based on your location.

Once started, a link will appear for the Streamer which displays the camera feed and detections in your browser:

```
Loaded model:
alwaysai/mobilenet_ssd

Engine: Engine.DNN
Accelerator: Accelerator.GPU

Labels:
['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

[INFO] Streamer started at http://localhost:5000
```
