---
title: "Weekly Robotics"
description: "This week in the Weekly Robotics newsletter: a plethora of space news, ROS in farming simulator, robot sensing in grains, a series of SLAM talks from AirLab and more! Also, WR meetups are back this week!"
date: 2021-05-31
tags: [Robotics, Space, ROS, OpenSource, Rovers, SLAM, Research]
idx: 145
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> I have an ask: did you ever work with any sort of LiDAR system and felt some eye fatigue afterwards? If yes, please [let me know](mailto:mat@weeklyrobotics.com), as I'm keen to compare notes! My space-related links backlog grew out of proportion this past week, so let me open up this newsletter issue by quickly going through them. As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). The most clicked link last week was [the JOSS paper on Slam Toolbox](https://joss.theoj.org/papers/10.21105/joss.02783) with 16.4% opens.

{:.post-entry-title}
#### Space Coverage

First on the radar is the [Ingenuity's flight anomaly](https://mars.nasa.gov/technology/helicopter/status/305/surviving-an-in-flight-anomaly-what-happened-on-ingenuitys-sixth-flight/) caused by a single camera frame drop that led to issues with timestamping following images, which in turn caused flight oscillations as high as 20 degrees in pitch and roll. Big thanks to Loy for sharing this news in the WR Slack channel.

[China's Zhurong rover](https://spectrum.ieee.org/automaton/robotics/space-robots/china-becomes-third-nation-to-successfully-land-rover-on-mars) had successfully landed on Mars. Unfortunately, there are not too many images available at the moment, but you will find some in [this BBC article](https://www.bbc.com/news/science-environment-57172346).

[Space debris hit space station robot arm](https://www.sciencealert.com/space-debris-has-damaged-the-international-space-station) - fresh news from Today, some small space debris hit [Canadarm2](https://www.asc-csa.gc.ca/eng/iss/canadarm2/about.asp) manipulator, puncturing the thermal blanket and damaging a boom beneath it. Fortunately, the module is still operational.

JAXA unveiled a [transofrmable lunar robot](https://global.jaxa.jp/press/2021/05/20210527-1_e.html) that will be used for data acquisition. The robot will weigh 250g and have a diameter of 80mm. Based on the renders I presume the robot will roll on the surface.

The Robot Report had published a good summary of [NASA's VIPER rover](https://www.therobotreport.com/viper-rover-could-help-long-term-human-exploration-of-moon/) - there were some rumors that this rover might run ROS2, which would be super exciting. [Here is a video](https://youtu.be/8GvldWevWCw) showing this rover's mobility testing.

----

{:.post-entry-title}
#### Farming Simulator 19 as a simulator for ROS

{:.post-source}
[YouTube](https://youtu.be/0muJvc4dhgU)

Researchers from TUDelft are working on creating a ROS plugin for Farming Simulator 19 (ROS Discourse topic [here](https://discourse.ros.org/t/first-beta-of-ros1-integration-for-farming-simulator19/20625)), and already showcasing some interesting results.

----

{:.post-entry-title}
#### Tartan SLAM Series

{:.post-source}
[AirLab](https://theairlab.org/tartanslamseries/)

AirLab is organizing a series of talks related to SLAM, with a very interesting lineup of speakers. The first talk with Sebastian Scherer is already published on [YouTube](https://youtu.be/acYBSrDpEdQ), and 9 more talks taking place weekly with a short break in June. I'll be definitely looking forward to watching this series. Huge thanks to Adrian for sharing this link in our WR Slack!

----

{:.post-entry-title}
#### Online PID Tuner

{:.post-source}
[pidtuner.com](https://pidtuner.com/)

Here is an online tool that allows you to autotune your controllers. I don't have a system that I could test this with, but if you do and give it a shot, feel free to share the outcomes with me, I'm really curious about the results!

----

{:.post-entry-title}
#### Slender robotic finger senses buried items

{:.post-source}
[MIT](https://news.mit.edu/2021/robotic-finger-buried-underground-0526)

We went through Gel Sight and similar devices utilizing deformable structure and cameras to detect shapes in a couple of issues ([#93](https://weeklyrobotics.com/weekly-robotics-93), [#101](https://weeklyrobotics.com/weekly-robotics-101)). This work introduces Digger Finger, again being able to detect shapes, but this time it can be used in grainy environments, such as sand or rice.

----

{:.post-entry-title}
#### Publication of the Week - Localization for Lunar Micro-Rovers (2021)

{:.post-source}
[CMU](https://www.ri.cmu.edu/publications/localization-for-lunar-micro-rovers/)

In the [WR #131 Perseverance Special Edition](https://weeklyrobotics.com/weekly-robotics-131), we discussed a paper describing all the cameras and microphones that are present on the rover. In this article, the author covers the localization system present in the MoonRanger, the first micro-rover that will perform a polar mission in situ to gather information on lunar ice. The polar regions of the moon lack light due to the low incident sun angle, making those terrains completely dark. Because of these environmental challenging conditions, the rover needs robust localization components, such as sensor fusion with IMU and wheel encoder data, sun sensor to correct heading drift, and even visual odometry. It is interesting to see that the MoonRanger project uses all of that with off-the-shelf components to save cost.

----

### Announcements

{:.post-entry-title}
#### WR Community Meeting #11 - Davide Faconti

{:.post-source}
[Eventbrite](https://www.eventbrite.co.uk/e/wr-meetup-11-davide-faconti-tickets-157466399239)

Weekly Robotics Community Meetings are back this week! This Thursday, at 7 PM CEST, we will be hosting Davide Faconti, an author of the two most useful tools I have used in ROS: [PlotJuggler](https://github.com/facontidavide/PlotJuggler) and [BehaviorTree.CPP](https://github.com/BehaviorTree/BehaviorTree.CPP). Looking forward to the chat, the topic of Davide's talk will be updated later this week. See you there!
