---
title: "Weekly Robotics"
description: "In the 61st issue of Weekly Robotics newsletter we look at a new visual SLAM library, Coanda Effect Hovercraft, an R&D setup for prosthesis development and robot hand solving Rubik's Cube"
date: 2019-10-20
tags: [Robotics, Careers, Drones, Research, SLAM, ROS, Safety, AI]
idx: 61
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> All the stickers I dedicated for the giveaway [last week](https://weeklyrobotics.com/weekly-robotics-60) were claimed within 48 hours. There are now on their way to the 20 of you that expressed interest in them. I hope that in the future I will be able to repeat the giveaway! In other news this week I attended [Robotics and ROS meetup](https://www.meetup.com/Robotics-and-ROS-in-Zurich/) in Zurich where I presented Weekly Robotics and had a chance to attend presentation of [ANYbotics ANYmal C](https://www.anybotics.com/). I've learned a ton and the demo was amazing. ANYbotics has many [open source repositories](https://github.com/ANYbotics) that I recommend you to check out, especially if you are working with ROS.

1) Coanda Effect Hovercraft.
<br>[YouTube](https://youtu.be/ebqQxLwjWfY)<br>
INFO: Yet another interesting project log from Tom Stanton. This time he is building a hovercraft using [Coandă Effect](https://en.wikipedia.org/wiki/Coand%C4%83_effect) to create a cushion of air for the hovercraft to lift off the ground. You can find other Tom's projects in [issue #26](https://weeklyrobotics.com/weekly-robotics-26) and [issue #43](https://weeklyrobotics.com/weekly-robotics-43).

2) Assembler Robots Make Large Structures From Little Pieces.
<br>[MIT](http://news.mit.edu/2019/robots-large-structures-little-pieces-1016)<br>
INFO: Benjamin Jenett, a PhD student at MIT had developed robots capable of assembling structures, while also in a way being a part of them. In the article this concept is called "relative robotics" and I can't wait to see more projects like these.

3) Kimera Library.
<br>[GitHub](https://github.com/MIT-SPARK/Kimera)<br>
INFO: Via the linked page: "Kimera is a C++ library for real-time metric-semantic simultaneous localization and mapping, which uses camera images and inertial data to build a semantically annotated 3D mesh of the environment. Kimera is modular, ROS-enabled, and runs on a CPU". The [ROS wrapper](https://github.com/MIT-SPARK/Kimera-VIO-ROS) of this package contains launch files for a Realsense D435i camera. I'm really tempted to try it out.

4) Stanford Engineers Develop New Tool for Designing Prosthetic Limbs.
<br>[YouTube](https://youtu.be/MKOBk3oFj8M)<br>
INFO: This video presents work done by Stanford Researchers with prosthesis emulators - a testbed for rapid prosthesis design and testing.

5) PCB Thermal Management Techniques.
<br>[All About Circuits](https://www.allaboutcircuits.com/technical-articles/pcb-thermal-management-techniques/)<br>
INFO: This article from All About Circuits describes good design practices for Printed Circuit Board design and inspection when it comes to heat dissipation. Big thanks to [Illia](https://www.linkedin.com/in/illia-sheremet-68bbab105/) for the tip!

6) LIPO Batteries Fail Explosion Compilation How Not to Burn Down your Home.
<br>[YouTube](https://youtu.be/foodLXgCilc)<br>
INFO: I might have fallen into a YouTube rabbit hole of RC models crashing and what not and thought it would be a good idea to to talk safety again. I think being reminded every now and then that the LiPO batteries can catch fire if not handled properly is a good thing. Stay safe!

7) Publication of the Week - Solving Rubik's Cube With a Robot Hand (2019).
<br>[arXiv](https://arxiv.org/abs/1910.07113)<br>
INFO: This paper presents the work of OpenAI Researchers on creating a whole system capable of solving a Rubik's cube with a humanoid robot hand that made [the news](https://techcrunch.com/2019/10/15/watch-openais-human-like-robot-solve-a-rubiks-cube-one-handed/) this week. The setup for this project looks quite interesting, starting with [Shadow Robot Dexterous Hand](https://www.shadowrobot.com/products/dexterous-hand/), a motion capture system to track the hand's fingertips, RGB cameras for vision pose estimation and bluetooth enabled Rubik's Cube. To train the model the Researchers used ADR (Automatic Domain Randomization) in simulation. My favourite part of the paper is when the AI gets annoyed: "We also observe that the policy appears more likely to drop the cube after being stuck on a challenging face rotation for a while". You can find the video of the hand solving the cube on [YouTube](https://youtu.be/kVmp0uGtShk).

### Sponsored

1) Intel Realsense T265 Tracking Camera for Mobile Robotics - First Impressions.
<br>[msadowski.github.io](https://msadowski.github.io/Realsense-T265-First-Impressions/)<br>
INFO: I've spent a fair bit of time working with T265 on [Robosynthesis](https://www.robosynthesis.com/) development platform. The above blog post summarizes my experience with this camera and provides some tips on how to set it up.

### Careers

1) [ANYbotics](https://www.anybotics.com/career/) (Zurich, Switzerland) - Various Positions.
<br>
INFO: We provide solutions for robot applications with the most advanced mobility and autonomy requirements in challenging terrain.

2) [Magazino](https://magazino-jobs.personio.de/job/147552?language=en) (Munich, Germany) - Performance & Quality Roboticist.
<br>
INFO: Magazino develops and builds intelligent, mobile robots for intralogistics.
