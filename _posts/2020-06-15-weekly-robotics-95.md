---
title: "Weekly Robotics"
description: "This week in WR: a novel approach for robot hands, free depth camera computer vision workshop, an update on UBR-1 restoration, open source multi legged robot controller, hoverbike crash and more!"
date: 2020-06-15
tags: [Robotics, Careers, ROS, ROS2, RobotArms, QuadrupedRobots, Drones, AutonomousCars, Sensors]
idx: 95
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> I knew that there would be heaps of cool robotics projects, news etc. coming right around the time ICRA wraps up but I didn't expect so many! As I'm putting this issue together I need to choose from 42 links. Now I'm wondering if this number is a coincidence. The most clicked last week was [Fresh Consulting report on why robotics companies fail](https://www.freshconsulting.com/wp-content/uploads/2020/06/Why-Robotics-Fail_Fresh-Consulting.pdf) with 15.2% opens.

1) We Can Do Better Than Human-Like Hands for Robots.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/we-can-do-better-than-humanlike-hands-for-robots)<br>
INFO: Researchers at Stanford University have developed a robotic hand that instead of mimicking anthropomorphic fingers is using 3 actuated rollers that allow for various methods of object manipulation. The second iteration of this work is using balls instead of rollers. In the article you can see 2 videos showing these two concepts.

2) UBR-1 Restoration Update.
<br>
INFO: Since the [last week's issue](https://weeklyrobotics.com/weekly-robotics-94) Michael Ferguson has published two blog posts with updates on the restoration of his robot. In the post [UBR-1 on ROS2](http://www.robotandchisel.com/2020/06/08/ubr1-on-ros2/) Michael describes how he ported his launch files and configuration to ROS2 and how he was able to run RVIZ with it. In the [follow up post](http://www.robotandchisel.com/2020/06/11/ubr1-on-ros2/) we can learn about porting controllers to ROS2.

3) OpenSHC: A Versatile Multilegged Robot Controller.
<br>[GitHub](https://github.com/csiro-robotics/syropod_highlevel_controller)<br>
INFO: "Syropod High-level Controller (SHC) is a versatile controller capable of generating body poses and gaits for quasi-static multilegged robots. This ROS package implemented in C++ can be easily deployed on legged robots with different sensor, leg and joint configurations. SHC is designed to generate foot tip trajectories for a given gait sequence, step clearance, step frequency and input body velocity". The library is open source with a CSIRO Open Source Software Licence (a variation of MIT/BSD). You can see a video showing some functionality of this library [on YouTube](https://youtu.be/-E7-2UMP5XU).

4) Continuum Robot Examples.
<br>[GitHub](https://github.com/JohnDTill/ContinuumRobotExamples)<br>
INFO: "Continuum robots have elastic links which are capable of large-scale continuous deformations. This repo has example scripts to simulate continuum robots of various design paradigms. Each example is accompanied by a short write-up in PDF format". This work has been open sourced by John Daniel Till. The repository also contains his [PhD disseretation](https://github.com/JohnDTill/ContinuumRobotExamples/blob/master/Misc/On%20the%20Statics%2C%20Dynamics%2C%20and%20Stability%20of%20Continuum%20Robots-%20Model%20Formulations%20and%20Efficient%20Computational%20Schemes.pdf).

5) Hoverbike Crash in Dubai!
<br>[YouTube](https://youtu.be/sBiYM8gqQ3Y)<br>
INFO: Here is a video I've very strong feelings about. Firstly why would put a unprotected spinning blades so close to a human and second of all why would a barometer failure cause the aircraft to start tilting, secondly saying "all safety systems worked well" in a crash like this indicates to me that there might not be too many safety systems implemented on these platforms. Luckily no one was injured this time!

6) CARLA Talks 2020.
<br>[CARLA](http://carla.org/2020/06/09/talks_2020/)<br>
INFO: The team behind CARLA, an open source simulator for autonomous driving research, had published a range of videos and slides showcasing some of their developments.

7) ROS Study Group- Beginner
<br>[discourse.ros.org](https://discourse.ros.org/t/ros-study-group-beginner/)<br>
INFO: Some folks at ROS discourse are joining forces to learn ROS together. I thought some of the readers could be interested in joining.

### Job Seekers

[In the issue #83](https://weeklyrobotics.com/weekly-robotics-83) I've started this section to try to help out those looking for work in the times of pandemic. If you are currently looking for work then feel free to [send me](mailto:mat@weeklyrobotics.com) your details in the same format as you can see in the entries below.

**Name**: Varadraj Bhat<br>
**Location**: Davis, CA, USA. Willing to relocate across USA<br>
**Skills**: Python, C,Embedded C, Ladder Logic, MATLAB/Simulink,ROS,RVIZ, Gazebo, PLC, Microcontrollers- INTEL 8051, INTEL 8086, ATMega328, TICC3200, MSP432 , Fusion360,Arduino IDE, Energia, CC studio, Studio 5000,500-Rockwell Automation, Repetier Host<br>
**Profile**: Robotics and Controls Engineer, Presently working on strawberry packing automation using the Baxter research robotic arm. Experienced in ROS, PLC, microcontroller. Looking for opportunities in Robotics, Controls and Autonomous systems<br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/varadraj-bhat/) <br>
**Email**: vbhat@ucdavis.edu<br>

### Careers

1) Dusty Robotics (Mountain View, CA, US) - [Sr Robotics Software Engineer / VP of Engineering](https://www.dustyrobotics.com/careers).
<br>
INFO: Dusty Robotics is an early-stage venture-backed startup developing robotic automation for the construction industry.

2) Dronistics (Lausanne, Switzerland) - [Full-Stack Developer](http://dronistics.epfl.ch/jobs.html).
<br>
INFO: At Dronistics you will have the unique opportunity to work with exciting technologies to develop the next generation of transportation drones. Working at Dronistics will provide you with hands-on experience in fields such as software development, UX Design, mechanical design, prototyping and field tests.

3) Saga Robotics (Lincoln, UK) - [Various Positions](https://www.indeedjobs.com/saga-robotics-ltd).
<br>
INFO: Saga Robotics are developing robotic solutions for soft fruit production, and are involved in several exciting projects world wide, including Norway, UK, and USA. The company works closely with universities as well as industry leaders in robotics and fruit production to create autonomous robots for farmers.

### Announcements

1) Computer Vision on Depth Cameras: Spatial AI.
<br>[Eventbrite](https://www.eventbrite.com/e/computer-vision-on-depth-cameras-spatial-ai-tickets-105895538406)<br>
INFO: AlwaysAI is organizing a free workshop on computer vision with depth cameras. The event will take place online on July 1st. Time to dust off these Realsense cameras!
