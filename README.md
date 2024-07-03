# My Awesome Project

This project is designed to do awesome things with computer vision and robotics.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install this project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/username/repository.git
    ```
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use this project, run the following command:

```sh
python main.py



# mycobot

## Using MyCobot and WebCam OpenCV camera

![image](https://github.com/WeberSouzaWeb/mycobot_ai/assets/107212929/afb1a27b-4f69-4a19-9286-837bfcb819f8)

https://shop.elephantrobotics.com/products/mycobot-pi-worlds-smallest-and-lightest-six-axis-collaborative-robot?sscid=71k8_gzej

This is a webcam arm that always adjusts the position of the display to an appropriate distance in front of your eyes. It is mainly composed of an open source lib camera and a robot arm called "myCobot". The camera can obtain depth information as well as imagens, and calculate the distance from the camera to your face. MyCobot is a robot arm with six rotation axes that can create a variety of movements. The 3D position of your face is calculated from the images obtained through the Lib camera, and myCobot delivers the position display to right in front of your eyes. 

## Robot Arm Movement
![image](https://github.com/WeberSouzaWeb/mycobot_ai/assets/107212929/279eea02-c527-48fa-9752-77f7dc28ea62)

  X-direction movement: J1 axis rotation
  Y-direction movement: J4 axis rotation
  Z-direction movement: J2 and J3 axes rotation (opposite directions)

The J2 and J3 axes are used to move the object in the depth direction. Moving only J2 affects the Y direction, so J3 is rotated the same amount in the opposite direction to the J2 axis to reduce this effect.

## Face Tracking on the XY Plane
  By detecting faces in the images obtained from the Lib camera, we can obtain the coordinates (x,y) of the face on the camera frame.

  ![image](https://github.com/WeberSouzaWeb/mycobot_ai/assets/107212929/64eef99d-6bc8-461e-b484-9e2fca1fb0ec)

  The center coordinates of the camera frame are used as the target value, and the face coordinates (x,y) obtained by face recognition are used as the feedback value for PID control.

  ![image](https://github.com/WeberSouzaWeb/mycobot_ai/assets/107212929/16475f02-6c59-45a4-a59c-6e0a70af7912)

## Depth (Z) Face Tracking 
  The camera is equipped with a stereo WebCam camera, so it can obtain not only the surface but also the face coordinate z in the depth direction. The target value is the distance between the face and the display that is neither too close nor too far, and the face coordinate (z) measured by the stereo camera is used as the feedback value for PID control.

  ![image](https://github.com/WeberSouzaWeb/mycobot_ai/assets/107212929/99ed95fd-15c7-4fb1-a54d-45f152d1b2a5)

## MyCobot and WebCam
  The WebCam and the RaspberryPi that comes with myCobot are connected via USB.
  The WebCam camera determines the target coordinates of the face, and the RaspberryPi that comes with myCobot uses PID control to change the camera's orientation according to those coordinates.

## Set UP
  We will set up the environment for RaspberryPi that comes with myCobot.
  

  The RaspberryPi version of myCobot is ready to use as soon as you power it on. 
  The robot arm can be run with python and is officiolly supported.

  ### PID
    If the movement of MyCobot is unstable, please try adjusting the PID value.

  Setting Target Values
    The Code below determines the target value for where myCobot will pont the camera. nnData[0] indicate the coordinates of the four corners of the boundingBox surrounding the face detected by the camera. The sum of the coordinates of the four corners divided by 2 will give the center point of the BoundingBox surrounding the face. spatialCoordinates.z is a method that returns the measurement result of the distance between the camera and the face.

## Conclusion
  This time, i tried face tracking using face recognition with a Webcam and a robot arm capable of complex movements. You can see that if you capture human movements with computer vision and operate a robot arm accordingly, it can perform a wide variety of movements. We hope this will be helpful for your development.

