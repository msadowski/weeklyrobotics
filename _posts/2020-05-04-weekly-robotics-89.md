---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: low cost Open Source quadruped from Stanford, drones powering your home, a DIY killer surgery robot, metric-semantic SLAM tutorial and more!"
date: 2020-05-04
tags: [Robotics, Careers]
idx: 89
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> The most clicked last week was [the video of Skyentific's robot joint based on pulleys](https://youtu.be/utDagouxM5U) with 18.6% opens.

1) Stanford Pupper.
<br>[Stanford Student Robotics](https://stanfordstudentrobotics.org/pupper)<br>
INFO: Pupper is an inexpensive ($600-$900) open-source quadruped robot that's pretty damn cute. The brains of the robot is a Raspberry Pi running [custom software](https://github.com/stanfordroboticsclub/StanfordQuadruped). I'm actually heavily considering building one after seeing it [in action](https://youtu.be/NIjodHA78UE).

2) Could High-Flying Drones Power Your Home One Day?
<br>[BBC](https://www.bbc.com/news/business-48132021)<br>
INFO: Some companies are working on alternatives to wind turbines that can fly to higher altitudes and generate energy making use of stronger winds. For a nice demonstrator of one uch technology you can see [this video](https://youtu.be/BBMms4LnEKw) from [Ampyx Power](https://www.ampyxpower.com/). In their solution the drone is generating energy by pulling a winch it is attached to to generate electricity.

3) I Built A Surgery Robot [NSFW][18+].
<br>[YouTube (Michael Reeves)](https://youtu.be/A_BlNA7bBxo)<br>
INFO: This video contains lots of profanity and at one point lots of fake blood so I would not recommend watching this in the office. What I find interesting about this video is how well this cartesian manipulator seems to reach the target position using BLDC motor and an encoder - all driven by [ODrive](https://odriverobotics.com/) motor controllers. Another interesting feature I found was gesture control using an IR tracking camera (If anyone knows the model used please feel free to let me know, I couldn't find it anywhere). What I find disturbing in these videos is Michael's disregard for safety. It looks like 2:20 and 10:09 were some close calls for a collision with a part of the robot.

4) Using MoveIt2 on a Industrial Open-Source Application.
<br>[ROS-Industrial](https://rosindustrial.org/news/2020/4/29/using-moveit2-on-a-industrial-open-source-application)<br>
INFO: This blog post is the first one I've seen about running Moveit2 with ROS2 using Gazebo as a simulation environment. The ecosystem seems to have been maturing rapidly in the past year.

5) Project ARchi3.
<br>[YouTube (Chris Boden)](https://www.youtube.com/playlist?list=PL-3Y2XexL9dTNKEhwgJxFhWum2wXZp7Ia)<br>
INFO: This YouTube playlist contains lots of videos from Chris Boden in which he builds a robot arm. Currently the playlist contains 35 videos. Looks like I have a bit of catching up to do!

6) Robots and Machines in Modern Farming Industry.
<br>[YouTube (Brainstorm HQ)](https://youtu.be/LGnNIs3VMWc)<br>
INFO: No voiceover, just you and 13 minutes of 8 agricultural robots. Is this what perfect Sunday evening looks like?

7) Publication of the Week - Metric-Semantic SLAM with Kimera: A Hands On Tutorial (2020).
<br>[YouTube (MIT SPARK Lab)](https://youtu.be/Zjevg5wQTdI)<br>
INFO: You might remember [Kimera library](https://github.com/MIT-SPARK/Kimera) from the [issue #61](https://weeklyrobotics.com/weekly-robotics-61). Kimera is a real-time metric-semantic simultaneous localization and mapping library written in C++. This tutorial shows the main components of Kimera and includes a ROS demo at around 15:00. I wish more software came with video tutorials like this!

### Job Seekers

[In the issue #83](https://weeklyrobotics.com/weekly-robotics-83) I've started this section to try to help out those looking for work in the times of pandemic. If you are currently looking for work then feel free to [send me](mailto:mat@weeklyrobotics.com) your details in the same format as you can see in the entries below. Please note that I will be able to list up to 5 profiles a week here.

**Name**: Gustavo Rezende<br>
**Location**: Uberlândia, Brazil. Willing to relocate.<br>
**Skills**: ROS, Python,  C/C++, Matlab, Java, BDI agents, Docker, image processing, gazebo, linux, git, scrum<br>
**Profile**: I am a Mechatronic Engineer and a MSc student in Automation and System Engineering, I expect to conclude my master's by the middle of June. My research is about active perception within BDI agents reasoning cycle, and the application of BDI agents to program robots intelligence. More specifically, I am using simulated UAVs as testbed, utilizing ROS, ardupilot, gazebo, and Jason to achieve this goal. I have already worked in the past with humanoid robots, wheeled robots, positioning systems, digital image processing and precision agriculture. I am fluent in Portuguese and English, also I speak French at an intermediate level and basic Japanese. <br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/gustavo-rezende-a1326731/), [GitHub](https://github.com/Rezenders) <br>
**Email**: gustavorezendesilva@hotmail.com<br>

### Careers

1) Convergent IT (Haid, Austria) - [Various Positions](https://convergent-it.com/job-offer/).
<br>
INFO: AUTOMAPPPS is a family of robot programming software tools developed by Convergent Information Technologies GmbH.  The robot programming software covers fast and easy robot offline programming (OLP), reactive robot programming and robot bin picking.

2) Rovenso (Villaz-St-Pierre, Switzerland) - [Various Positions](https://www.rovenso.com/#join).
<br>
INFO: Rovenso develops autonomous agile robots for security and safety monitoring of industrial sites.

### Announcements

1) Join us for World MoveIt Day 2020!
<br>[MoveIt](https://moveit.ros.org/events/world-moveit-day/2020/04/28/world-moveit-day-2020.html)<br>
INFO: We’re excited to announce the fifth annual World MoveIt Day is going virtual, and will be held on Tuesday, June 2, 2020 from wherever you are. World MoveIt Day is an international hackathon to improve the MoveIt code base, documentation, and community. Every year we close an impressive number of issues and merge nearly 100 pull requests, while exploring new areas of improvements for the now eight years strong framework.
