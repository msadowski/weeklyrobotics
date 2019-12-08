---
title: "Weekly Robotics"
description: "In the 68th issue issue of Weekly Robotics newsletter: bare metal quadrotor programming pt 2, a desktop robot arm, small farming robots and more!"
date: 2019-12-08
tags: [Robotics, Careers, Drones, ROS, RobotArm, Cobots, Research, Space]
idx: 68
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

1) GLUON丨Modular Desktop Collaborative Robotic Arm by SCA.
<br>[Kickstarter](https://www.kickstarter.com/projects/1383636492/the-smallest-servomotor-robotic-arm)<br>
INFO: Have you heard of this desktop robot arm that has been live on Kickstarter for quite a while now? The company managed to beat the funding goal over 40 times (as I'm writing this over 366k Euro had been pledged, with the funding goal being only 9k Euro). The robot is using BLDC motors, the 6-axis model can handle a payload of 0.5 kg and an advertised precision of 0.1mm. You can see a review of this robot arm by Skyentific on [YouTube](https://youtu.be/ZlJENPxR7yM). Big thanks to [Krzysztof](https://www.linkedin.com/in/kzurad/) for letting me know about this campaign.

2) Skydio 2 Review: This Is the Drone You Want to Fly.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/drones/skydio-2-review-this-is-the-drone-you-want-to-fly)<br>
INFO: This article is an in-depth review of Skydio 2, an autonomous tracking drone equipped with six 4K cameras feeding information to the system running on NVIDIA Jetson TX2. I found this short [behind the scenes video](https://youtu.be/3KfP40oMxlY) to be a good watch, especially the camera calibration process (you will find it at 20s timestamp). I so wish these drones came with an API we could interface to!

3) The Zebracorn’s TileRunner Nano Tutorial.
<br>[Google Docs](https://docs.google.com/document/d/1012NdhGdX1eb00tZwitfiZv5klTbQH0zX_nKdXa0vU8/edit)<br>
INFO: Zebracorns, a FIRST® Robotics Competition team, had prepared a tutorial on deploying ROS on a TileRunner mobile robot chassis. At 47 pages the document is going to a good amount of depth.

4) Quadcopter Programming Part 2: Using the CMSIS Library and First Takeoff.
<br>[timakro.de](https://timakro.de/blog/quadcopter-programming-part-2/)<br>
INFO: Back in [Weekly Robotics #29](https://weeklyrobotics.com/weekly-robotics-29) I had posted the first tutorial from Tim on bare metal STM32 programming of a quadrotor. This is the second post in the series where you actually get to take off.

5) cozmo_ros2_ws.
<br>[GitHub](https://github.com/solosito/cozmo_ros2_ws)<br>
INFO: It looks like Anki Cozmo can run ROS2 now. If you would like to try this out but don't have Cozmo then you might want to hurry up, while some shops still have these robots in stock since Anki had closed last year (as I reported in [#37](https://weeklyrobotics.com/weekly-robotics-37)).

6) What Went Down at ROSCon 2019.
<br>[ROS-Industrial](https://rosindustrial.org/news/2019/12/6/what-went-down-at-roscon-2019)<br>
INFO: Are you like me and missed the whole ROSCon 2019? If you are looking for some succinct notes then this article is a good start.

7) Publication of the Week - The Robots are Coming – to Your Farm! AKA: Autonomous and Intelligent Robots in Unstructured Field Environments (2019).
<br>[Carnegie Mellon University](https://www.ri.cmu.edu/event/ri-seminar-girish-chowdhary-university-of-illinois-at-urbana-champaign-assistant-professor-2019-11-15/)<br>
INFO: I love these CMU seminars. I learn so much from every one of them (the [last one](https://weeklyrobotics.com/weekly-robotics-60) I posted was in October). In this one Girish Chowdhary talks about automation in unstructured environments plant monitoring. The robots presented are quite small and are deployed in corn fields but due to the canopy occlusion the GPS was not precise enough and hence the team decided to use a LiDAR. The second half of the talk focuses on using AI for robotics.

### Careers

1) FarmWise (San Francisco, CA, US) - [Various Positions](https://farmwise.io/careers).
<br>
INFO: FarmWise builds autonomous farming devices that help solve the labor shortage encountered by many farmers in the US and we also drastically reduce the amount of chemical used in the farming process.

2) Liquid Robotics (Sunnyvale, CA, US) - [Senior Software Engineer](http://jobs.jobvite.com/liquid-robotics-inc/job/os7ybfw2).
<br>
INFO: Liquid Robotics builds autonomous, wave- and solar- powered maritime sensor vehicles that return real-time data from the open ocean to customers on shore.

3) Dyson (Malmesbury, UK) - [VR Software Engineer](https://careers.dyson.com/en-gb/job-description/vr-software-engineer-robotics-research/30391), [Embedded Software Engineer](https://careers.dyson.com/en-gb/job-description/embedded-software-engineer-applied-robotics/29797).
<br>
INFO: Dyson’s Robotics Research Software Team specialises in creating early stage proof-of-concept systems that utilise state-of-the-art software algorithms, frameworks, techniques, and tooling.

### Announcements

1) Join the AWS JPL Open-Source Rover Challenge.
<br>[spacechallenge.tech](https://spacechallenge.tech/)<br>
INFO: AWS and JPL announced a challenge where teams will use machine learning to autonomously operate [JPL's Open Source Rover](https://opensourcerover.jpl.nasa.gov/) (I had featured this project in the [first issue of this newsletter](https://weeklyrobotics.com/weekly-robotics-1)). In the challenge participants will use AWS RoboMaker for the simulation and Amazon SageMaker to build and train RL models. The competition is open until the 21st of February 2020.
