---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: Dead Robots series launch, Unity3D used for robot simulation, porting a project from ROS1 to ROS2, ballistically launched multirotor and more!"
date: 2020-05-25
tags: [Robotics, SoftRobots, ModularRobots, Drones, MobileRobots, Rovers, simulation]
idx: 92
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> I've started a WeeklyRobotics [YouTube channel](https://www.youtube.com/channel/UCCRTqp-rykFr905qQfVqZYg) that I kicked off with an [Astrobee teaser video](https://youtu.be/oc57_l4M5YY). Is a video like this something that you would find interesting? My idea for this mini project is to create a series of < 1 minute videos highlighting interesting things about some robotics projects and as always providing a heaps of links for further research. If you love or hate this idea then I'd like to hear from you! You can send me an e-mail at [mat@weeklyrobotics.com](mailto:mat@weeklyrobotics.com). The most clicked last week was [fastbook.ai notebooks](https://github.com/fastai/fastbook) with 13.8% opens.

1) Dead Robots - MegaBots.
<br>[Medium](https://medium.com/dead-robots/dead-robots-megabots-cbbaca2bc4a1)<br>
INFO: Conrad Gray, the author of [H+ Weekly](https://hplusweekly.com/) had created a new series telling stories of failed robots and companies behind them. In this article Conrad tells the story of MegaBots - a company that was building giant fighting robots. I like how well researched this article is!

2) Use Articulation Bodies to Easily Prototype Industrial Designs with Realistic Motion and Behavior.
<br>[Unity](https://blogs.unity3d.com/2020/05/20/use-articulation-bodies-to-easily-prototype-industrial-designs-with-realistic-motion-and-behavior/)<br>
INFO: Unity, a 3D game engine, is becoming more and more robotics friendly. In the next release Unity will support articulated joints, making it easier to create realistic robot arm simulations. If you happen to work with ROS then [ROS#](https://github.com/siemens/ros-sharp) is a set of libraries, maintained by Siemens, that you can use to bridge ROS and Unity3D.

3) Self-reconfiguring Modular Robot.
<br>[Wikipedia](https://en.wikipedia.org/wiki/Self-reconfiguring_modular_robot)<br>
INFO: [Julius](https://www.linkedin.com/in/juliussust/) pointed out to me that the Wikipedia page on self-reconfiguring modular robots is a very good read with many examples of physical systems created (among them [Roombots](https://www.epfl.ch/labs/biorob/research/modular/roombots/), about which I chatted during [my interview](https://weeklyrobotics.com/podcast-ep-1) with Auke Ijspeert).

4) Patent approved for Posable Hubs for Robotic Platforms.
<br>[CSIRO](https://research.csiro.au/robotics/patent-approved-for-posable-hubs-for-robotic-platforms/)<br>
INFO: These posable hubs for mobile robots allow to change the chassis pose using actuators attached to the wheel rim.

5) Porting a Project from ROS1 to ROS2 — Our Experience.
<br>[Medium](https://medium.com/husarion-blog/porting-a-project-from-ros1-to-ros2-our-experience-ef27b1748915)<br>
INFO: In this post Łukasz Mitka from [Husarion](https://husarion.com/) describes the issues they've solved when looking to support ROS2 in their GUI tool.

6) Inspired by Cheetahs, Researchers Build Fastest Soft Robots yet.
<br>[technology.org](https://www.technology.org/2020/05/18/inspired-by-cheetahs-researchers-build-fastest-soft-robots-yet/)<br>
INFO: Looking at [the video](https://youtu.be/Z5QAwAOxORo) this galloping robot was way faster than I was expecting based on all the soft robots I've seen up to date. I'm curious how a design like this can be scaled to perform any of the functions mentioned in the article (search and rescue, industrial manufacturing).

7) Publication of the Week - Design and Autonomous Stabilization of a Ballistically Launched Multirotor (2019).
<br>[arXiv](https://arxiv.org/abs/1911.10269)<br>
INFO: This is a paper is an update to the "Caltech and JPL Firing Quadrotors Out of Cannons" article that you might have seen in [issue 66](https://weeklyrobotics.com/weekly-robotics-66). In this iteration of the project SQUID is a 3.3kg hexacopter that can be launched from a T-Shirt cannon at 12m/s. Researchers calculated that the aircraft experiences 21g acceleration on launch (the IMU used saturated at 16g) and the maximum height achieved with this system was 32m (104 feet). [ROVIO](https://github.com/ethz-asl/rovio) is used for active stabilization using the onboard camera and the IMU - the steps that need to get the VIO readings are interesting - you'll find more info about it in section IV. You can find the videos with launches [on YouTube](https://youtu.be/mkotvIK8Dmo).

### Announcements

1) Hackaday Prize 2020.
<br>[Supplyframe](https://prize.supplyframe.com/)<br>
INFO: Hackaday Prize 2020 is on! Hackaday Prize is a worldwide hardware design challenge focused on globally impactful innovation. This year, we are partnering with leading nonprofits to tackle some of the world’s toughest problems across conservation, disaster relief, renewable resources, and assistive devices. The Hackaday Prize connects you to engineers, expert mentors, and other powerful resources to develop dynamic solutions for those who need it most. You can enter the competition until August 31st.
