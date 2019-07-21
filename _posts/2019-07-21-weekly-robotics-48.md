---
title: "Weekly Robotics #48"
description: "In this issue of Weekly Robotics newsletter we explore soft robotics, agricultural robots, wall climbing robots and even some robotics algorithms"
date: 2019-07-21
tags: [Robotics, Careers, Agriculture, SoftRobotics, Software, ROS, Algorithms, Space, Drones]
---
![HeaderImage](/img/headers/48.jpg "Header image")

> This week I had a chance to present Weekly Robotics newsletter during a [ROS Agriculture](http://rosagriculture.org/) community meeting. It was nice to share the results of the project and learn something about open source agricultural robots. You can see the meeting recording on [YouTube](https://youtu.be/dgBTCRYIthg). Really looking forward to see the autonomous tractor!

1) Soft Robots - Computerphile.
<br>[YouTube](https://youtu.be/BLE5yhS3k3I)<br>
INFO: In this episode of his vlog Computerphile visits Kirstin Petersen's Lab at Cornell where a Grad Student Steven Ceron showcases some projects the Researchers are working on.

2) Robotics Library.
<br>[roboticslibrary.org](https://www.roboticslibrary.org/)<br>
INFO: Via website: "The Robotics Library (RL) is a self-contained C++ library for robot kinematics, motion planning and control. It covers mathematics, kinematics and dynamics, hardware abstraction, motion planning, collision detection, and visualization." The project is open sourced under a BSD licence and you can find it on [GitHub](https://github.com/roboticslibrary/rl).

3) ROS 2 - Is it Time to Switch?
<br>[Rover Robotics](https://blog.roverrobotics.com/ros-2-is-it-time-to-switch-tutorial-included/)<br>
INFO: In this article from Rover Robotics we can learn a good bit on advice whether to switch from ROS to ROS 2 aimed at 7 different user groups.

4) PythonRobotics.
<br>[GitHub](https://github.com/AtsushiSakai/PythonRobotics)<br>
INFO: PythonRobotics is a collection of robotics related algorithms with nice visualizations and source code. I covered this project in [Weekly Robotics #2](https://weeklyrobotics.com/weekly-robotics-2) but recently I visited the repository again and I was surprised how much it grew since August 2018. Big thanks to Atsushi Sakai and all the maintainers of the project!

5) NASA Climbing Robot Scales Cliffs and Looks for Life.
<br>[YouTube](https://youtu.be/q2SKa9IEG4M)<br>
INFO: This 4 minute documentary from NASA JPL showcases the LEMUR (Limbed Excursion Mechanical Utility Robot) robot with micro-spine grippers in its feet allowing it to scale rock walls. The LiDAR setup looks quite interesting - it looks like a sensor is placed at the end of a rotating boom allowing the robot to createa a 3D map of the wall while it's climbing it.

6) Build Your Own Selfie Drone With Computer Vision.
<br>[Hackaday](https://hackaday.com/2019/06/30/build-your-own-selfie-drone-with-computer-vision/)<br>
INFO: This Hackaday post showcases a video tutorial by YouTube user [geaxgx1](https://youtu.be/RHRQoaqQIgo) on enabling a DJI Ryze Tello to follow a person. The author is using [openpose library](https://github.com/CMU-Perceptual-Computing-Lab/openpose) for pose estimation from the video feed. You can find the geaxgx1 source code in his [GitHub repository](https://github.com/geaxgx/tello-openpose)

7) Publication of the Week - A Field‐tested Robotic Harvesting System for Iceberg Lettuce (2019).
<br>[Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.21888)<br>
INFO: I found this paper through [this article from the University of Cambridge](https://www.cam.ac.uk/research/news/robot-uses-machine-learning-to-harvest-lettuce). The system developed consists of an UR10 robot arm with custom end-effector, two cameras and a non-actuated mobile platform. The system is controlled using ROS and is using two convolutional neural networks (CNN): one for lettuce localization and the other for lettuce classification. I especially liked the notes about moving the system from the lab to the field and noticing a calibration is needed (it was achieved using Aruco markers). The average cycle time achieved by the team during trials was 31.7s, mainly due to the end-effector weight of 8 kg.

### Careers

1) [Locus Robotics](https://www.smartrecruiters.com/LocusRobotics/743999687519607-software-engineer-systems) (Wilmington, MA, US) - Software Engineer - Systems.
<br>
INFO: Locus Robotics’ innovative autonomous mobile robots make it easy to optimize your warehouse operation, respond to e-commerce volume growth and seasonal peaks while giving you control over your labor costs.

2) [Iron Ox](https://jobs.lever.co/ironox/39992c38-df6d-41de-b8e0-6260486ea2ea) (San Carlos, CA, US) - Software Architect.
<br>
INFO: Iron Ox is reimagining the modern farm, utilizing robotics and AI to grow fresh, consistent, and responsibly farmed produce for everyone. Our experienced team of growers, plant scientists, engineers, and innovators are passionate about deeply understanding and developing this new wave of technology to feed an ever-growing population.
