---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: Perseverance doing some AutoNav, Abundant robotics shutting down, old school research robots, CVPR overview and more!"
date: 2021-07-12
tags: [Robotics, research, sensors, vision_systems, mobile_robots]
idx: 151
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> In the next couple of days I'll be experimenting quite a bit with my schedule, so it's more than likely that the newsletter issues will stop arriving between 10-12 AM CEST as they did so far. I'll still try to send the issues on Mondays but cannot promise any particular time. As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). The most clicked link last week was [the visual SLAM roadmap](https://github.com/changh95/visual-slam-roadmap) with 19.0% opens.

{:.post-entry-title}
#### Abundant Robotics shuts down fruit harvesting business

{:.post-source}
[The Robot Report](https://www.therobotreport.com/abundant-robotics-shuts-down-fruit-harvesting-business/)

Making robots for agriculture is not an easy task. The biggest uncertainty I can imagine for these kinds of products is the seasonality - in many cases, you have a small window of opportunity to test your product, which is reduced by the issues you come across in your product and external factors such as weather etc. Now to the surprises: I've checked out the video in the LinkedIn post featured in the article and I'm really surprised with the shutdown. The robot seems to be working well in the video, using a vacuum attachment to pick up the apples, and reportedly averaging 2 seconds per pick and not bruising the fruits. I wonder what were the actual reasons for shut down.

----

{:.post-entry-title}
#### Some oldschool robots from the University of Michigan

{:.post-source}
[Twitter](https://twitter.com/UMRobotics/status/1413151638462812160)

These robots move way better than I did at the time these videos were recorded.

----

{:.post-entry-title}
#### Depth Sensor Visualizer

{:.post-source}
[Tangram Vision](https://www.tangramvision.com/resources/depth-sensor-visualizer)

Tangram Vision had released an interactive tool allowing you to visualise depth sensor max/min distance and the field of view. This tool can be helpful as the first thing to check when selecting a depth sensor.

----

{:.post-entry-title}
#### CVPR 2021: An Overview

{:.post-source}
[yassouali.github.io](https://yassouali.github.io//ml-blog/cvpr2021/)

Yassine Ouali did an amazing job summing up the [Conference on Computer Vision and Pattern Recognition](http://cvpr2021.thecvf.com/) and providing insights on some selected papers. If vision is your thing (or you don't believe in using LiDARS/radars for your autonomous cars) then I'm sure you will find some of the featured papers interesting.

----

{:.post-entry-title}
#### NASA’s Self-Driving Perseverance Mars Rover ‘Takes the Wheel’

{:.post-source}
[NASA](https://www.nasa.gov/feature/jpl/nasa-s-self-driving-perseverance-mars-rover-takes-the-wheel)

Perseverance has done its first auto navigation using the AutoNav module. The module creates 3D maps of the terrain and plan paths around any obstacles. It can reach a top speed of 120 meters per hour (Curiosity could pull off about 20 meters per hour). This looks like some very solid engineering. I would love to learn more about the details of how this module works.

----

{:.post-entry-title}
#### Publication of the Week - Learned Visual Navigation for Under-Canopy Agricultural Robots (2021)

{:.post-source}
[arXiv](https://arxiv.org/abs/2107.02792)

Agriculture is one of the major fields that play a significant role in robotics. The author presents CropFollow, a low-cost robot that uses a monocular RGB camera and is capable of autonomously navigate in challenging under-canopy terrains with many obstacles, uneven, and visually cluttered. The system uses a modular approach and decouples the perception and control system. The perception uses one convolutional network to predict the heading of the robot and another network to predict the displacement to the crop rows. Using these methods, the robot could perform better than a costly robot with a LiDAR.

----

### Careers

[Imperial College London](https://www.imperial.ac.uk/hamlyn-centre/opportunities/) (London, United Kingdom) - Facilities Manager

The Hamlyn Centre for Robotics Surgery is seeking a Project Support Officer to provide robust and professional support to the Co-Directors and Director of Operations of The Hamlyn Centre. In this role you will organise events including conferences, policy workshops, and public lectures; promote the Centre’s work via the website, social media, email, paper publications; develop the Centre’s outreach to different audiences; and manage the databases and communication methods.
