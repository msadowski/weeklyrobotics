---
title: "Weekly Robotics #3"
description: "#3! Tiny 3D printed electric motor, trajectory optimization for walking robots, research on water-air communications, autonomous cars frustrating drivers with left turns and more!"
tags: [Robotics, DIY, Books, MIT, AutonomousCars, Software, ROS, ROS2, NASA, Curiosity]
date: 2018-09-02
---

1) DIY 3D-printed Electric Motor.
<br>[https://spectrum.ieee.org/geek-life/hands-on/how-to-print-an-electric-motor](https://spectrum.ieee.org/geek-life/hands-on/how-to-print-an-electric-motor){:target="_blank"}<br>
INFO: This project showcases a 3D printed brushless motor in which the motor coils are deposited on a PCB (Printed Circuit Board). With the current design the static torque was measured to be 0.9 gram-centimeters - not enough to include those motors in a tiny quadrotor just yet but we are very keen to see where the author takes this project in the future.

2) Humble Book Bundle - Machine Learning.
<br>[https://www.humblebundle.com/books/machine-learning-books](https://www.humblebundle.com/books/machine-learning-books){:target="_blank"}<br>
INFO: Humble Bundle teamed up with O'Reilly for the Machine Learning bundle. You can grab up to 15 books and support Code for America. Before checkout you can select how you want your money to be distributed between HumbleBundle, O'Reilly and Code for America. The bundle ends on 10.09.2018.

3) Johnny-Five - Program Robots in Javascript.
<br>[http://johnny-five.io/](http://johnny-five.io/){:target="_blank"}<br>
INFO: Johnny-Five is a Robotics and IoT platform working with Arduino compatible boards. It seems perfect for people who want to start their adventure with Arduino and have web development background. In the [Examples](http://johnny-five.io/examples/){:target="_blank"} you can find anything from blinking LED to handling joysticks, servos, motor shields, IMUs etc. Most of the examples have a very clear images showing the wiring between Arduino and hardware, which should also help if you are a beginner.

4) MIT researchers take a step forwards in water-air communications.
<br>[http://news.mit.edu/2018/wireless-communication-through-water-air-0822](http://news.mit.edu/2018/wireless-communication-through-water-air-0822){:target="_blank"}<br>
INFO: MIT researches propose a system where a sonar submerged in water directs the signal to the surface, causing tiny vibrations that represent transmitted bits. Above the surface a highly sensitive receiver reads the disturbances and decodes the signal. The emitter sends sonar waves at different frequencies (e.g. 100Hz for 0 and 200Hz for 1), causing tiny ripples in water. The receiver is a high-frequency radar that processes signals in the millimeter wave spectrum of wireless transmission, between 30 and 300 gigahertz. 

5) Waymo's left turns frustrate drivers.
<br>[https://ideas.4brad.com/waymos-left-turns-frustrate-other-drivers](https://ideas.4brad.com/waymos-left-turns-frustrate-other-drivers){:target="_blank"}<br>
INFO: According to author's sources some people are getting frustrated with driving patterns of autonomous Waymo vans. Author mentions that the reason cars are timid is not caused by the technology (Waymo cars are equipped high resolution LiDAR sensor that can have 200+ meters) but by the teams avoiding risks at early stages. 

6) Learn about Curiosity.
<br>[https://marsmobile.jpl.nasa.gov/msl/multimedia/interactives/learncuriosity/index-2.html](https://marsmobile.jpl.nasa.gov/msl/multimedia/interactives/learncuriosity/index-2.html){:target="_blank"}<br>
INFO: Did you know that NASA's Curiosity has roughly the size of a car (10x9x7 feet or 3x2.7x2.2 meters with a mass of 1,982 pounds or 899 kg). This interactive website allows for looking at the rover from different perspectives and provide information on the rover subsystems.

7) towr - Trajectory Optimizer for Walking Robots.
<br>[http://wiki.ros.org/towr](http://wiki.ros.org/towr){:target="_blank"}<br>
INFO: towr is a ROS package for trajectory optimization for legged robots. The library includes an Rviz (ROS visualization software) plugin that allows for creating robot representation and visualizing gait (see section two in the repository documentation for the short presentation). If you want to build your own AT-AT you can probably start here.