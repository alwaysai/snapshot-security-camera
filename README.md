# Snapshot Security Camera App
This app expands on the *realtime_object_detector* starter app to build a simple security camera app that takes a picture of each new person who enters the frame. The full tutorial can be found on the [alwaysAI blog](https://learn.alwaysai.co/detect-people-using-alwaysai).

## Setup
This app requires access to alwaysAI's Beta program. To sign up go to the [Sign up page](https://www.alwaysai.co/dashboard)

Once accepted to the program, follow the setup instructions located on the [Docs page](https://www.alwaysai.co/docs/getting_started/introduction.html) - Note this link is accessible only to beta users.

## Usage
Once the alwaysAI toolset is installed on your development machine (or edge device if developing directly on it) you can run the following CLI commands:

To set up the target device & folder path

`aai app configure`

To build and deploy the docker image of the app to the target device

`aai app deploy`

To start the app

`aai app start`

Images will be saved in the app directory with the person's detection index and the timestamp.
