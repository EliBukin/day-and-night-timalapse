# day-and-night-timalapse
Shoot Day and Night TimeLapse with RaspberryPI Camera - Python

Automatic mechanism for shooting timelapse sequences both for day and night conditions.

For that we will use python3.
Raspberry PI (choose your flavour, i've used 3B+).
PIcamera (i am using v1.3 but i guess you can go with NOIR as well).


For start i will analyze light conditions:

check_light_func.py contains functions to analyze an image for it's brightness, consist of main function and another three functions:
check_light - is the main function, will be called by timelapse loops to analyze the photos taken.
brightness_GreyScaleMean + brightness_GreyScaleRMS + brightness_Perceived - summed together will be used to determine of the conditions are for night or day.


Then the main script that actually shoots the photos:
the script built of two main functions, each function consist a call for light analyzation function and a loop that breaks when the light conditions are met.

Last there is a script that stitches all the photos to a video, this piece is not automated and should be started manually whenever you want to create your timelapse clip.


i want to give credits to KB sources i used:
light detection was inspired by https://github.com/NestBoxTech/Ambient-Light-Monitoring/blob/master/ambient_lightMonitor.py
timelapse was inspired by https://picamera.readthedocs.io/en/release-1.10/recipes1.html#capturing-timelapse-sequences
stitching process was adopted from https://tsaith.github.io/combine-images-into-a-video-with-python-3-and-opencv-3.html
* in the comments of the stitching process there is a dude who modified the script to a much better version (which is shown here) so i think you should use it instead of the original.
