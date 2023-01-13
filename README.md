# Snapshot Security Camera App

This app expands on the *realtime_object_detector* starter app to build a
simple security camera app that takes a picture of each new person who enters
the frame. The full tutorial can be found on the
[alwaysAI blog](https://alwaysai.co/resources/tutorials/detect-people-using-object-detection).

## Requirements
* [alwaysAI account](https://alwaysai.co/auth?register=true)
* [alwaysAI Development Tools](https://alwaysai.co/docs/get_started/development_computer_setup.html)

## Usage
Once the alwaysAI tools are installed on your development machine (or edge device if developing directly on it) you can install and run the app with the following CLI commands:

To perform initial configuration of the app:
```
aai app configure
```

To prepare the runtime environment and install app dependencies:
```
aai app install
```

To start the app:
```
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
* [Documentation](https://alwaysai.co/docs/)
* [Community Discord](https://discord.gg/alwaysai)
* Email: support@alwaysai.co
