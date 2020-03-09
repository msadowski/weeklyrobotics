---
title: "Weekly Robotics"
description: "This week in Weekly Robotics: swarming robots avoiding collisions, more stories from SubT challenge, 3D projections library, testing realsense tracking accuracy and more!"
date: 2020-03-09
tags: [Robotics, Careers, AutonomousCars, SocialRobots, ROS, Software, MobileRobots, Space, OpenSource, Sensors, SLAM]
idx: 81
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> I'm looking to team up with companies creating hardware for robots (can be sensors, actuators, research platforms) for a grand Weekly Robotics project. If you know any company that could be interested I'd highly appreciate it if you could [let me know](mailto:mat@weeklyrobotics.com). The most clicked last week was [the /r/robotics link with a gif of tracked robot(?)](https://www.reddit.com/r/robotics/comments/fbrdme/m_wait_for_it_something_really_cool_happens_at/) with 18.7% opens.

1) RDBOX.
<br>[GitHub](https://github.com/rdbox-intec/rdbox)<br>
INFO: RDBOX is a standard IT infrastructure for ROS robots and IoT devices. If I understand it correctly this software should make it way easier for you to create a local network for robots and can even be used on robot swarms.

2) Swarming Robots Avoid Collisions, Traffic Jams.
<br>[YouTube (NorthwesternU)](https://youtu.be/XR86Zw5bemQ)<br>
INFO: Speaking of swarm robots: Researchers at Northwestern University have developed a system with 100 swarm robots (1024 in simulation) that can perform a collision-free reconfiguration.

3) Introducing: ARI ROS Simulator.
<br>[PAL Robotics](http://blog.pal-robotics.com/intoducing-ari-ros-simulation/)<br>
INFO: PAL Robotics have prepared a set of tutorial for simulating its ARI Social Robot with Gazebo/ROS. The tutorials on the [ROS wiki](http://wiki.ros.org/Robots/ARI/Tutorials) seem interesting - I would love to go through the implementation of some of them.

4) Late Nights, Cool Hacks, and More Stories From the DARPA SubT Urban Circuit.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/late-nights-cool-hacks-and-more-stories-from-the-darpa-subt-urban-circuit)<br>
INFO: SubT Urban Circuit wrapped up last week. The winner of this circuit was Team CoSTAR. The above IEEE Spectrum article describes the circuit, team preparation, last minute hacks and more. I'm looking forward to the Cave Circuit!

5) Klein.
<br>[jeremyong.com](https://www.jeremyong.com/klein/)<br>
INFO: This library is an implementation of 3D Projective Geometric Algebra. If you need to perform any geometric projections, distance calculations, translations and rotation of geometries then it might be useful for you. I've learned about this package thanks to [Davide Faconti on Twitter](https://twitter.com/facontidavide).

6) Testing the Realsense T265 Accuracy.
<br>[jaspereb.github.io](https://jaspereb.github.io/TestingRealsenseT265/)<br>
INFO: On [one occassion](https://msadowski.github.io/Realsense-T265-First-Impressions/) I've tested the Intel T265 tracking camera on a mobile robot, however I really lacked the ground truth information. In this blog post Jasper Brown shares the results of his experiments mounting the T265 on a UR5 robotic arm, which allowed him to have a ground truth. The results are indeed very good but as the author points out we have to remember that the robot performs a very smooth motion, which might not be a case for other platforms.

7) Publication of the Week - 2020 Autonomous Vehicle Technology Report (2020).
<br>[Wevolver](https://www.wevolver.com/article/2020.autonomous.vehicle.technology.report)<br>
INFO: Wevolver had published a very in-depth report on the state of autonomous cars that covers all of the aspects of autonomous cars I can think of and more. The use case of Roborace Robocar is also interesting with the autonomous car speed record at 282.42 km/h (175.49 mph).

### Announcements

1) ESA Startup Competition.
<br>[ESA](https://esa-2020-start-up-companies-competition.com/)<br>
INFO: "Collaboration between start-ups and the European Space Agency (ESA) can fast-track the development and introduction of breakthrough space technologies. That’s why ESA is calling for European start-ups to come forward and propose their game-changing space solutions to benefit from the know-how and support of ESA in their development". The winning startups will win a mentoring package worth between 25,000 to 100,000 Euro. You can register to the competition until 15th of April.
