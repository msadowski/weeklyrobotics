---
title: "Weekly Robotics #36"
description: "In this issue of Weekly Robotics Newsletter we explore the hot topics of LiDARs, 3 different mobile robots and soft robotics. Enjoy!"
date: 2019-04-28
tags: [Robotics, Careers, LiDAR, AutonomousCars, Space, SoftRobots, MobileRobot, ROS]
---

1) Laying the Ground for Robotic Strategies in Environmental Protection.
<br>[Wyss Institute](https://wyss.harvard.edu/laying-the-ground-for-robotic-strategies-in-environmental-protection/)<br>
INFO: Researchers at the Wyss Institute have developed Romu, a robot designed to drive interlocking sheet piles into the ground to help stabilize soil. The robot is using linear actuators and a vibratory hammer to press the sheets into the ground.

2) Snake-inspired Robot Uses Kirigami for Swifter Slithering.
<br>[The Robot Report](https://www.therobotreport.com/snake-inspired-robot-uses-kirigami-for-swifter-slithering/)<br>
INFO: Kirigami is a papercraft that uses cuts to change the properties of the material. By carefully choosing cuts in a shell the Scientists can 'program' the skin to deform in a desired sequence.

3) NASA's Robonaut to Return to Space Station With Legs Attached.
<br>[IEEE](https://spectrum.ieee.org/automaton/robotics/space-robots/nasas-robonaut-to-return-to-iss-with-legs-attached)<br>
INFO: [Robonaut](https://robonaut.jsc.nasa.gov/R2/) is currently being prepared to go back to ISS, this time with legs attached, that are key to the Robonaut Project research objectives. The above article contains an interview with Julia Badger who is the Robonaut Project Manager, we highly recommend going through it! If you happen to use ROS and Gazebo then you might be able to run the Robonaut 2 simulation by following [this wiki](https://gitlab.com/nasa-jsc-robotics/robonaut2/wikis/R2%20Gazebo%20Simulation).

4) Paris Firefighters Used This Remote-Controlled Robot to Extinguish the Notre Dame Blaze.
<br>[IEEE](https://spectrum.ieee.org/automaton/robotics/industrial-robots/colossus-the-firefighting-robot-that-helped-save-notre-dame)<br>
INFO: In the [previous issue of Weekly Robotics](https://weeklyrobotics.com/weekly-robotics-35) we've mentioned the robots used during the Notre Dame fire. This articles from IEEE provides more details about the Colossus, a 500 kg (1100 lbs) firefighting robot. We were quite surprised to learn that the robot is capable of moving 1,000 kg (2200 lbs) of payload.

5) ROS Package for Anki Vector Home Robot.
<br>[GitHub](https://github.com/betab0t/vector_ros)<br>
INFO: Omri Ben-Bassat has created an unofficial ROS package for [Anki Vector](https://www.anki.com/en-us/vector), a small wheeled home robot. The package is open source and is a wrapper around Vector SDK. It provides interfaces for the camera, velocity commands, animations, saying text etc.

6) Velodyne Lidar Partners with Nikon to Mass-produce Cheaper Lidar Sensors.
<br>[Velodyne](https://velodynelidar.com/newsroom/velodyne-lidar-nikon-announce-manufacturing-agreement-for-mass-production-of-velodyne-lidar-sensors/)<br>
INFO: "Sendai Nikon Corporation, a Nikon subsidiary, will manufacture lidar sensors for Velodyne with plans to start mass production in the second half of 2019". Hopefully the ramp up in production will result in cheaper multi-axis LiDARs on the market.

7) Publication of the week - Pseudo-LiDAR from Visual Depth Estimation:Bridging the Gap in 3D Object Detection for Autonomous Driving (2019).
<br>[arXiv](https://arxiv.org/abs/1812.07179)<br>
INFO: We found the above paper cited in several articles [[1](https://www.therobotreport.com/researchers-back-teslas-non-lidar-approach-to-self-driving-cars/)], [2](https://gizmodo.com/elon-musk-was-right-cheap-cameras-could-replace-lidar-1834266742)] that surfaced after Elon Musk made a statement about LiDARs being a fool's errand during Tesla autonomy days earlier this week. We've decided to see ourselves what the paper says and if stereo cameras will beat LiDARs any time soon. The paper has been written by Cornell University Researchers. In the paper they propose an alternative method for representation of 3D information obtained from stereo cameras so that it resembles LiDAR data (pseudo-LiDAR) and therefore LiDAR based object detection algorithms can be applied to it. The experiment setup is based on the [KITTI benchmark](http://www.cvlibs.net/datasets/kitti/) and there are two algorithms that Researchers evaluate: F-POINTNET-v1 and AVOD-FPN. Looking at the results table the chosen approach is a significant improvement over other camera based methods however at high [Intersection over Union](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/) there is still a high gap between stereo based method described and Lidar + monocular camera based method. In case of Bird Eye View representation with AVOD algorithms and the IoU of 0.7 the researchers obtained a result of 74.9 (89.4 for LiDAR + mono camera) in Easy category and 49.0 (79.3 for LiDAR + mono camera) in Hard category.

### Sponsored

1) Humble Book Bundle: Electronics + 3D Printing by Make.
<br>[Humble Bundle](https://www.humblebundle.com/books/electronics-3d-printing-make-books?partner=weeklyrobotics)<br>
INFO: This Humble Book bundle features 24 books from Make that are worth $401. In the bundle you will find books related to 3D printing, electronics, programming and even drones. If you purchase the bundle using the above affiliate link you can choose to support Weekly Robotics.

### Careers

1) [Moley](https://moleyrobotics.bamboohr.com/jobs/) (London, UK) - Various Positions.
<br>
INFO: Moley has created the world's first robotic kitchen. Featuring an advanced, fully functional robot integrated into a beautifully designed, professional kitchen, it cooks with the skill and flair of a master chef. The prototype was premiered to widespread acclaim at Hanover Messe, the international robotics show.

2) [Sonnet.ai](http://sonnet.ai/job01/) (Seoul / Daegu, South Korea) - Senior Software Engineer, Autonomous Driving.
<br>
INFO: Sonnet.ai is a tech startup bringing artificial intelligence to autonomous vehicles and precision medicine. We founded sonnet.ai because we believe that artificial intelligence technology has the potential to save lives and transform our societies, and we think this is the right team to do it.

3) [Barrios Technology](https://careers-barrios.icims.com/jobs/1460/software-developer/job?mobile=false&width=1020&height=500&bga=true&needsRedirect=false&jan1offset=60&jun1offset=120) (Houston, TX, US) - Software Developer.
<br>
INFO: Barrios Technology Ltd. is a woman-owned and operated small business headquartered in Houston, Texas. We provide a full spectrum of engineering, operations and related technology services in support of the aerospace community and have successfully supported NASA for 38 years.
