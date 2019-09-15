---
title: "Weekly Robotics"
description: "In the 56th issue of Weekly Robotics newsletter we explore finalists of Hacaday Prize, a toolbox for SLAM, robocar dataset, space robot retiring and more!"
date: 2019-09-15
tags: [Robotics, Careers, Research, Drones, SLAM, Sensors, SelfDrivingCars, Space, SpaceRobots, Humanoids, SwarmRobots]
idx: 56
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> As I'm writing this newsletter I'm at [EPFL Open Days 2019](https://www.epfl.ch/campus/events/celebration-en/portes-ouvertes/) in Lausanne, Switzerland. It was quite cool to see some of the projects researchers work on at EPFL and in other Swiss organizations. Finally I was able to see ANYmal in action live! In other news every now and then I update the [awesome weekly robotics list](https://github.com/msadowski/awesome-weekly-robotics) and as I'm writing this issue the list has over 70 entries!

1) Meet The 20 Finalists In The 2019 Hackaday Prize.
<br>[Hackaday](https://hackaday.com/2019/09/10/meet-the-20-finalists-in-the-2019-hackaday-prize/)<br>
INFO: Hackaday announced 20 finalists of the Hackaday Prize. Among them we can find projects related to robotics such as [3D printed prosthesis with CV, BCI and EMG](https://hackaday.io/project/165075-3d-printed-prosthesis-with-cv-bci-and-emg), [Bobble-Bot](https://hackaday.io/project/164992-bobble-bot)([WR #38](https://weeklyrobotics.com/weekly-robotics-38)), [SmallKat](https://hackaday.io/project/164727-smallkat-an-adorable-dynamics-oriented-robot-cat), [Axiom: 100+kW Motor Controller](https://hackaday.io/project/164932-axiom-100kw-motor-controller) and [Blackbird Bipedal Robot](https://hackaday.io/project/160882-blackbird-bipedal-robot). I can also see myself using [OPEN Power](https://hackaday.io/project/164913-open-power) at some point in the future if they ever start selling those.

2) Slam Toolbox.
<br>[GitHub](https://github.com/SteveMacenski/slam_toolbox)<br>
INFO: slam_toolbox is a ROS package for 2D lifelong mapping and localization in potentially massive maps developed by [Steve Macenski](https://github.com/SteveMacenski). I started setting it up this week with [Robosynthesis](https://www.robosynthesis.com/) and if you are doing SLAM with ROS I highly recommend checking it out. My experience so far is that if you have a odom->base_link transform and a semi decent LiDAR then this package can work very well pretty much out of the box.

3) EU Long-term Dataset with Multiple Sensors for Autonomous Driving.
<br>[epan-utbm.github.io](https://epan-utbm.github.io/utbm_robocar_dataset/)<br>
INFO: Engineers from Université De Technologie De Belfort-Montbéliard released a number of datasets containing data from various sensors mounted on a car. Among the sensors used we can find 2 stereo cameras, 3 lidars, radar, GNSS receiver with RTK base station, IMU and 2 RGB cameras. The datasets are provided in the form of ROS bagfiles.

4) Russia Terminates Robot Fedor After Space Odyssey.
<br>[Phys.org](https://phys.org/news/2019-09-russia-scraps-robot-fedor-space.html)<br>
INFO: Skybot F-850 (Featured in [#53](https://weeklyrobotics.com/weekly-robotics-53) and [#54](https://weeklyrobotics.com/weekly-robotics-54)) completed his mission and according to the article it won't be coming back to the ISS any time soon. Apparently using legs in space is no easy feat!

5) Water Jet Powered Drone Takes Off With Explosions.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/drones/water-jet-powered-drone-takes-off-with-explosions)<br>
INFO: Researchers from Aerial Robotics Lab at Imperial College London had developed a 'fying fish' fixed-wing UAV that is propelled by gas explosions. The gas is created from the reaction of calcium carbide with water (you can see some experiments on that on [YouTube](https://youtu.be/-4cJnLcBtVA)) and when ignited the water forced out of the combustion chamber generates 51 N of thrust, launching the robot as high as 21 meters up. You can see the drone in action in [this video](https://youtu.be/aJU8EL61NgA).

6) This Adorable Baby T-Rex AI Learned To Dribble.
<br>[YouTube](https://youtu.be/-ryF7237gNo)<br>
INFO: This video from [Two Minute Papers](https://www.youtube.com/channel/UCbfYPyITQ-7l4upoX8nvctg) shows using AI to compose complex motions from the sum of elementary movements. Even though this paper demonstrates the solution for 3D animations, I can see how it could be utilized on robots with complex kinematic chains. Big thanks to [Artur](https://github.com/ArturSkowronski) for the tip about this video!

7) Publication of the Week - ShapeBots: Shape-changing Swarm Robots (2019).
<br>[arXiv](https://arxiv.org/abs/1909.03372)<br>
INFO: Each ShapeBot is equipped with 2.5 cm thin reel-based linear actuator that can extend to 20 cm (~7.9 in) both horizontally and vertically The work presented in the paper is the result of collaboration between the University of Colorado Boulder and the University of Tokyo. The robots are relatively simple with ESP8266 microcontroller used as the brains of the robot and BOM  summing up to 20-25 USD. I found the [ShapeBots simulator](https://ryosuzuki.github.io/shapebots-simulator/) to be very satisfying to experiment with and nicely showing the concept of these robots being used in a swarm setting. You can find the video showcasing the bots in action on [YouTube](https://www.youtube.com/watch?v=cwPaof0kKdM).

### Careers

1) [Parkopedia](https://parkopedia.workable.com/jobs/1119744) (London, UK) - Robotics Software Engineer.
<br>
INFO: Parkopedia was founded with the mission of being able to answer any parking question, anywhere in the world. In the Autonomous Driving team we’re creating Highly Autonomous Driving (HAD) indoor parking maps and testing those maps on our autonomous car to ensure that they are suitable for localisation and navigation.

2) [Apex.AI](https://hire.withgoogle.com/public/jobs/apexai/view/P_AAAAAAEAAGtKiUXTR4sbge) (Palo Alto, CA, USA) - Senior Field Application Engineer.
<br>
INFO: We envision a world of seamless and safe autonomous mobility. Pursuing this vision, we have built a team of the best engineers in their field working together focussed on enabling our customers to take automated mobility applications to production.

### Announcements

1) The Space Robotics Challenge Phase 2.
<br>[Nine Sights](https://ninesights.ninesigma.com/servlet/hype/IMT?userAction=Browse&documentId=d4414ecdb345e2190f661e20df641dee&templateName=&documentTableId=3422744979561065985)<br>
INFO: As NASA moves forward with plans to support human exploration of the solar system, a critical need arises to supply basic materials such as oxygen (O2) and water (H2O), food, propellants, and other materials (radiation shielding, clothing, etc.). As mankind ventures farther from Earth and for greater periods of time, it becomes imperative to develop technologies and mission architectures that utilize local resources, such as those found in lunar regolith, to provide supplies needed for human exploration. The objective of SRC Phase 2 is to find solutions to allow a heterogeneous, multi-robot team to autonomously complete tasks envisioned for a lunar in-situ resource utilization (ISRU) mission. This challenge will require competitors to develop software that allows a virtual team of robotic systems (i.e. virtual robotic team) to operate autonomously to successfully achieve these tasks. The application deadline is the 20th of December this year.
