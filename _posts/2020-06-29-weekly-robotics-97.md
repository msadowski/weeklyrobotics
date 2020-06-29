---
title: "Weekly Robotics"
description: "Issue #97 of Weekly Robotics: virtual swashplate for a helicopter, open source software for wiring diagrams, slow conservation robots, a mobile robot for radioactivity monitoring, event cameras, and more!"
date: 2020-06-29
tags: [Robotics, Careers, Drones, Sensors, MobileRobots, OpenSource, Research]
idx: 97
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> Remeber the Gundam robot from Japan ([#76](https://weeklyrobotics.com/weekly-robotics-76) and [#77](https://weeklyrobotics.com/weekly-robotics-77))? [It's moving](https://www.reddit.com/r/robotics/comments/hgalvk/d_the_gundam_robot_in_yokohama_japan_is_moving/)! It's been a while since I've added 2 projects to [Awesome Weekly Robotics](https://github.com/msadowski/awesome-weekly-robotics) in one issue. If you are looking for some open source projects to check out then feel free to check that list! The most clicked last week was [AR 2 & AR 3 open plan robot arms](https://www.anninrobotics.com/) with 13.1% opens.

1) Drone Helicopter Hybrid.
<br>[YouTube](https://youtu.be/d80oXSCcHTk)<br>
INFO: Tom Stanton is at it again. This time he has built a helicopter that instead of using [traditional swashplate](https://en.wikipedia.org/wiki/Swashplate_(aeronautics)) slows the motor down at appropriate times to achieve a 'virtual swashplate'. If you liked this video then you have to watch the follow up on [Tom's second channel](https://youtu.be/Y31BhQToh_U) that's way more technical and covers what Tom had tried to get to the first working prototype.

2) Building & Flying an Exercise Ball RC Plane!
<br>[YouTube](https://youtu.be/GgGxkxREIOs)<br>
INFO: While we are on the subject of custom UAVs FliteTest had created a remotely piloted fixed wing UAV that uses an exercise ball as an (under)carriage.

3) WireViz.
<br>[GitHub](https://github.com/formatc1702/WireViz)<br>
INFO: 'WireViz is a tool for easily documenting cables, wiring harnesses and connector pinouts. It takes plain text, YAML-formatted files as input and produces beautiful graphical output (SVG, PNG, ...) thanks to GraphViz. It handles automatic BOM (Bill of Materials) creation and has a lot of extra features'.

4) ‘SlothBot in the Garden’ Demonstrates Hyper-Efficient Conservation Robot.
<br>[Georgia Tech](http://news.gatech.edu/2020/06/16/slothbot-garden-demonstrates-hyper-efficient-conservation-robot)<br>
INFO: The SlothBot that was featured in [issue #44](https://weeklyrobotics.com/weekly-robotics-44) is getting a field test! It looks like the Robotics Engineers at Georgia Institute of Technology had updated the design quite a lot - I really like that the current design comes with a head! Having "slowness" as a design principle is an interesting idea for this kind of project. Looking forward to seeing how the first demonstrator goes!

5) An Open Torque-Controlled Modular Robot Architecture for Legged Locomotion Research.
<br>[Open Dynamic Robot Initiative](https://open-dynamic-robot-initiative.github.io/)<br>
INFO: Quoting the linked website: 'This website is the entry point to the resources of the Open Dynamic Robot Initiative. This project originated in an effort to build a low cost and low complexity actuator module using brushless motors that can be used to build different types of torque controlled robots with mostly 3D printed and off-the-shelves components. This module, and extensions, can be used to build legged robots or manipulators. A paper describing the actuator module and the quadruped design can be found [here](https://arxiv.org/abs/1910.00093)'.

6) CARMA 2.
<br>[University of Manchester](https://uomrobotics.com/robots/carma-2.html)<br>
INFO: Continuous Autonomous Radiometric Monitoring Assistant (CARMA) is a Jackal based platform designed for automatic radiation monitoring and is developed by Robotics for Extreme Environments Group at The University of Manchester. The robot is equipped with 2 Hokuyo LidarS, an Orbec depth camera, and two radiation probes. [Here](https://youtu.be/ZBr2DIpNeNI) you can see a recent video showing the robot operating in a controlled environment.

7) Publication of the Week - Event Cameras: Opportunities and the Road Ahead (CVPR 2020).
<br>[YouTube](https://youtu.be/6Sn9-M7qXLk)<br>
INFO: Every now and then I like to check on the progress of event cameras and every time I do I end up looking at what UZH Robotics and Perception Group (RPG) is up to. In this talk, Davide Scaramuzza shares the current state of event cameras and shows some of the research done by his group. Compared to traditional cameras these cameras output a change of brightness of every pixel, resulting in a continuous sensor feed and low power consumption (as little as 1mW!). It looks like there are already 4 companies producing these sensors and the examples shown in this talk makes some very good points. I'll be looking forward to seeing these sensors going more mainstream.

### Sponsored

1) Ouster OS1 - First Impressions.
<br>[msadowski.github.io](https://msadowski.github.io/ouster-os1-ros-review/)<br>
INFO: Recently I had a chance to play with Ouster OS1-16, a 16 plane automotive grade LiDAR. The above blog post describes some of the setup steps I have performed, integration with Cartographer, and workflow for extracting localized point clouds from a bag file.

### Job Seekers

[In the issue #83](https://weeklyrobotics.com/weekly-robotics-83) I've started this section to try to help out those looking for work in the times of pandemic. If you are currently looking for work then feel free to [send me](mailto:mat@weeklyrobotics.com) your details in the same format as you can see in the entries below.

**Name**: Seth King<br>
**Location**: Central Virginia,  USA(Remote primary focus)<br>
**Skills**:  C, C++(11,14), Python, , Linux, Yocto, ROS, ROS2<br>
**Profile**: Embedded software engineer with 15 plus years of experience in Unix/Linux OS. Georgia Tech OMSCS Grad in 2018 with a specialization in Robotics and Perception<br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/nerdking/), [GitHub](https://github.com/Neuromancer2701), [Side Project](https://openrover.com/#open)<br>
**Email**: king.seth@gmail.com<br>

### Announcements

1) The FPV Drone Racing VIO Competition.
<br>[RPG](https://uzh-rpg.github.io/IROS2020-FPV-VIO-Competition/)<br>
INFO: The participants are required to run their VIO algorithms on sequences selected from the public [UZH-FPV Drone Racing Dataset](http://rpg.ifi.uzh.ch/uzh-fpv.html), which include images, IMU measurements, and event-based camera data recorded with an FPV drone racing quadrotor flown aggressively by an expert pilot. The goal is to estimate the quadrotor motion as accurately as possible, utilizing any desired sensor combinations. The winning entry can win up to $2k and the deadline for submissions is September 27th, 2020.
