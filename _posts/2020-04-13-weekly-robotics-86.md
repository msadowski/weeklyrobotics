---
title: "Weekly Robotics"
description: "In the 86th issue of Weekly Robotics: SoftBank robot simulator, reviving an industrial robot arm, field oriented control for brushless motors and much more!"
date: 2020-04-13
tags: [Robotics, Careers, Simulators, Control, IndustrialRobot, LeggedRobots, Drones]
idx: 86
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> If you are wondering how Weekly Robotics is doing subscriber-wise then you might like to take a look at the [Q1 2020 report](https://weeklyrobotics.com/Q1-2020-report). In the past 4 months there was a 10% growth in subscriptions, while website visits were down. The most clicked last week were [software developer's thoughts on his low cost robot vacuum](https://dev.to/deciduously/i-am-mesmerized-by-our-new-robotic-vacuum-10pc) with 14.9% opens.

1) qiBullet.
<br>[SoftBank Robotics](https://developer.softbankrobotics.com/blog/qibullet)<br>
INFO: qiBullet is a bullet-based simulator for SoftBank robots, licenced under Apache 2.0. Looking at the [tutorials](https://github.com/softbankrobotics-research/qibullet/wiki/Tutorials:-Virtual-Robot) it makes the control of the simulated robots easy using the Python API. The simulator can be also interfaced with ROS. Many thanks to [Maxime](https://github.com/mbusy) for letting me know about this project!

2) Industrial Robot Given New Life And Controller.
<br>[Hackaday](https://hackaday.com/2020/04/08/industrial-robot-given-new-life-and-controller/)<br>
INFO: There are two interesting parts to this article. The first one is the [project itself](https://hackaday.io/project/170793-yasky-bot-an-industrial-robotic-arm-becomes-open) where Hackaday user caltadaniel managed to reverse engineer a Yaskawa motoman MH5LF industrial arm and creating a custom control box for it. The second interesting bit is the video where the robot flicks a switch of an useless box - I found this one quite entertaining.

3) What is FOC? (Field Oriented Control) And why you should use it! || BLDC Motor.
<br>[YouTube (GreatScott!)](https://www.youtube.com/watch?v=Nhy6g9wGHow)<br>
INFO: If you want to know more about Field Oriented Control for electric motors then this video by GreatScott! is a great introduction to the topic.

4) Blast From the Past: UBR-1.
<br>[Show Us Your Sensors](http://www.showusyoursensors.com/2020/04/blast-from-past-ubr-1.html)<br>
INFO: In this blog post Michael Ferguson, a Founder of Unbounded Robotics and Vanadium Labs and a former CTO at [Fetch Robotics](https://fetchrobotics.com/), describes some of the features of UBR-1, an alternative to the Willow Garage's PR2 robot for R&D. For the National Robotics Week Michael has written a series of posts [on his blog](http://www.showusyoursensors.com/), if you are into ROS and robots then you might want to check them out.

5) Building a Robotic Spider.
<br>[Medium](https://medium.com/@mr_koz/building-a-robotic-spider-4253bdae4b10)<br>
INFO: Bobbie is an 8-legged spider robot being developed by Adam Purdie. The robot will use Dynamixel servos as actuators and Jetson Nano for the brains. This post is a build log of the whole platform including wiring. I'll be looking forward to following the project updates, especially that the author plans to run ROS2 on it, make it walk on uneven surfaces, and perform some machine learning using a simulator.

6) Combating COVID-19—The Role of Robotics in Managing Public Health and Infectious Diseases.
<br>[ScienceRobotics](https://robotics.sciencemag.org/content/5/40/eabb5589)<br>
INFO: How can robots assist in fighting COVID-19? This article might be an entry point for your inner brainstorm, although let's not kid ourselves - if you are reading this newsletter you have probably thought about these things already.

7) Publication of the Week - Lecture 23 Guest Lecture: Drones -- CS287-FA19 Advanced Robotics at UC Berkeley (2020).
<br>[YouTube](https://youtu.be/Yizyv8MpYfg)<br>
INFO: If you are wondering how [Skydio drones](https://www.skydio.com/) perform state estimation and navigation then this lecture by Hayk Martirosyan is for you. It's fascinating that the depth estimation is running on their deep learning network at 1000 Hz. Another interesting insight is the camera calibration for thermal expansion (both for the camera location and the lens distortion). If you like this lecture then you might also like [this behind the scenes video](https://youtu.be/3KfP40oMxlY) that was showcased in the [issue #68](https://weeklyrobotics.com/weekly-robotics-68) and is showing, among other things, automated camera calibration.

### Sponsored

1) Humble Book Bundle: Artificial Intelligence & Machine Learning by Morgan & Claypool.
<br>[](https://www.humblebundle.com/books/artificial-intelligence-machine-learning-morgan-claypool-books?partner=weeklyrobotics
)<br>
INFO: "We've teamed up with Morgan & Claypool for our newest bundle! Get ebooks like Essentials of Game Theory, Natural Language Processing for Social Media, Creating Autonomous Vehicle Systems, and more" - as always with these book bundles if you decide to purchase it then you can choose to support this newsletter and make it better.

### Job Seekers

[In the issue #83](https://weeklyrobotics.com/weekly-robotics-83) I've started this section to try to help out those looking for work in the times of pandemic. If you are currently looking for work then feel free to [send me](mailto:mat@weeklyrobotics.com) your details in the same format as you can see in the entries below. Please note that I will be able to list up to 5 profiles a week here.

**Name**: Beau Everaert<br>
**Location**: Brugge, Belgium<br>
**Skills**: C/C++, ROS, Python, Gazebo, Linux, GIT, XACRO, Inventor, PLC Programming, Electric Drives, Microcontrollers, Assembly, JavaScript<br>
**Profile**: Graduated as a master in electromechanical engineering at the University of Ghent, I have experience as an automation consultant for a large enterprise and I am fluent in German, English and Dutch. I'm very eager to contribute, I learn quickly so wherever my skill set could be of use, I'd be happy to help!<br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/beaueveraert/)<br>
**Email**: beau.everaert@gmail.com<br>

### Announcements

1) RobotUnion Marketplace.
<br>[RobotUnion](https://robotunion.eu/marketplace/)<br>
INFO: RobotUnion Marketplace is the showcasing platform for all the potential robotics stakeholders, which aims to become a single point of entry & to know-how services of technical and non-technical nature. All the RobotUnion Community users are invited to share their products and services in order to get visibility and create new business opportunities. A marketplace is also a tool that is used by RobotUnion scaleups for external services which they would like to use during the acceleration program.

2) KUKA Innovation Award 2021.
<br>[Kuka](https://www.kuka.com/InnovationAward2021)<br>
INFO: Apply now with an innovative concept to the "Artificial Intelligence Challenge"! You will have the opportunity to implement your concept with a KUKA robot provided free of charge and you will receive hardware training and coaching from KUKA experts throughout the competition. At the finale, which will take place in April 2021, you will have the opportunity to present your application to trade visitors from industry and research, the press, investors and interested visitors and win €20,000 in the end.
