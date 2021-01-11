---
title: "Weekly Robotics"
description: "This week in Weekly Robotics: six degrees of freedom multirotor flying at any orientation, a DIY quadruped robot build log, Akin's laws of spacecraft design and more!"
date: 2021-01-11
tags: [Robotics, SLAM, Omnicopter, Ardupilot, Px4, ArduCopter, ROS, MobileRobots, Quadrupeds, Space]
idx: 125
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Hackaday](https://hackaday.com/2021/01/09/six-degrees-of-freedom-omnicopter-with-ardupilot/)*

> Welcome to the first standard issue of the year! Hope you got some proper amount of rest during the holidays and are ready for what 2021 has in store for us. Last week I've published December's issue of [Monthly Robotics](https://www.patreon.com/posts/45889848), an executive summary for newsletter's patrons on what has been published that month in the newsletter with a super brief update on my robotics workshop progress. To celebrate everyone making it through 2020 I'd like to invite anyone that decides to [support the newsletter](https://www.patreon.com/WeeklyRobotics) this week to join the newsletter's Slack, regardless of the support amount. Looking forward to the deep technical chats!

{:.post-entry-title}
#### Six Degrees Of Freedom Omnicopter With Ardupilot

{:.post-source}
[Hackaday](https://hackaday.com/2021/01/09/six-degrees-of-freedom-omnicopter-with-ardupilot/)

An incredible build from Peter Hall: a multirotor build with six tetrahedrons with different orientation that supports flight in any orientation. The software was developed on [Ardupilot](https://ardupilot.org/), adding a new [attitude control mode](https://github.com/ArduPilot/ardupilot/pull/16105).

----

{:.post-entry-title}
#### PX4 MAVROS Python Tutorial

{:.post-source}
[YouTube](https://youtu.be/jBTikChu02E)

Farhang Naderi had prepared tutorials on integrating PX4 autopilot with ROS, perfect if you want some high-level autonomy on drones. I would definitely find these useful 4 years ago when I was looking into [controlling a drone with a haptic controller](https://msadowski.github.io/1ppm/uav-haptic-control-pt1/). [Here](https://youtu.be/rxt0aBnBeJI) you will find the second part of the tutorial.

----

{:.post-entry-title}
#### Making Lego Car CLIMB Obstacles

{:.post-source}
[YouTube](https://youtu.be/MwHHErfX9hI)

"Testing a Lego car against different obstacles and improving it until it becomes a capable climber. Demonstrates what you need to consider: wheel diameter, gear ratio, 4-wheel drive, tire grip, breakover angle, weight distribution". On [the Brick Experiment Channel](https://www.youtube.com/channel/UClsFdM0HzTdF1JYoraQ0aUw/videos) you will find lots of other interesting builds.

----

{:.post-entry-title}
#### How Boston Dynamics Taught Its Robots to Dance

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/humanoids/how-boston-dynamics-taught-its-robots-to-dance)

If you are like me and you are wondering how did they manage to do [this](https://youtu.be/fn3KWM1kuAw) then the above article/interview will shed some light on how the dance was developed.

----

{:.post-entry-title}
#### Akin's Laws of Spacecraft Design

{:.post-source}
[University of Maryland](https://spacecraft.ssl.umd.edu/akins_laws.html)

A very good set of 'laws' that I think are useful for anyone doing any kind of engineering. When researching the topic I also came across [this presentation](https://www.ece.uvic.ca/~elec399/201409/Akin's%20Laws%20of%20Spacecraft%20Design.pdf) that extends every law with some examples.

----

{:.post-entry-title}
#### K3lso Quadruped

{:.post-source}
[Hackaday](https://hackaday.io/project/176487/logs)

Robin Fröjd had been working on a slick-looking quadruped. I highly recommend browsing this project log!

----

{:.post-entry-title}
#### Publication of the Week - Monocular Camera Localization in Prior LiDAR Maps with 2D-3D Line Correspondences (2020)

{:.post-source}
[arXiv](https://arxiv.org/abs/2004.00740)

[Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/): Localization using LiDAR can be expensive in terms of cost and performance. This paper proposes a light-weight method for localization using a monocular camera with a prior LiDAR created map. The idea is to detect lines both in the monocular camera and in the 3D map, match both of them, and estimate the 6-DoF pose. Pretty cool idea for limited budget projects!
