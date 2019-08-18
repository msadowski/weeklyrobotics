---
title: "Weekly Robotics #51"
description: "In this issue of Weekly Robotics newsletter we look into radiation vs. software, robots repairing infrastructure, spring-loaded drone and more!"
date: 2019-08-11
tags: [Robotics, Drones, IndustrialInspection, Manufacturing, ROS, AutonomousBoats, Space, Software]
---
![HeaderImage](/img/headers/51.jpg "Header image")

> Being on holidays I don't read as many articles as I normally would, still I found some time to read "[All the best engineering advice I stole from non-technical people](https://medium.com/@bellmar/all-the-best-engineering-advice-i-stole-from-non-technical-people-eb7f90ca2f5f)" by Marianne Bellotti and found it to be very insightful and a very good read. Next week's issue of WR will be the last of my holiday edition, after which you can expect to see some improvements to this project.

1) Robots Can Play Key Roles in Repairing our Infrastructure.
<br>[The Robot Report](https://www.therobotreport.com/robots-can-play-key-roles-in-repairing-our-infrastructure/)<br>
INFO: This Robot Report article from June is a great introduction on using robots for pipe inspection and maintenance.

2) How to Design For CNC Milling.
<br>[adambender.info](https://www.adambender.info/post/design-for-cnc-milling)<br>
INFO: In this post Adam Bender gives quite useful advice on 3D part design for CNC milling. It's interesting how a badly designed part can almost double the price of an element.

3) Spring-Loaded Drone Collapses Mid-Flight to Zip Through Windows.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/drones/spring-loaded-drone-collapses-midflight-to-zip-through-windows)<br>
INFO: UC Berkeley researchers created a spring loaded drone. The arms of this robot are spring loaded causing them to fold whenever the motor-propeller combination is not producing any thrust. If you are into drones then the video included in the article is quite worth a watch.

4) ROSCon 2019 Program is Out.
<br>[ros.org](https://roscon.ros.org/2019/#program)<br>
INFO: The program for ROSCon 2019 that will take place from 31st of October to 1st of November is out! Unsurprisingly, there is a lot of focus on ROS2 related presentations and I'm expecting to learn a ton! As soon as there is some information about livestream published I'll let you know!

5) Underwater Drones Nearly Triple Data From the Ocean Floor.
<br>[Bloomberg](https://www.bloomberg.com/news/articles/2019-06-07/underwater-drones-nearly-triple-data-from-the-ocean-floor)<br>
INFO: From this Bloomberg article we can learn about [Ocean Infinity](https://oceaninfinity.com/), their seabed mapping business and successful shipwreck discoveries. All powered by [Kongsberg Maritime AS](https://www.kongsberg.com/maritime/) submarines costing anywhere from $5-$10M.

6) Using a 'Cave Rover,' NASA Learns to Search for Life Underground.
<br>[NASA](https://www.nasa.gov/feature/ames/braille)<br>
INFO: BRAILLE (Biologic and Resource Analog Investigations in Low Light Environments) is a NASA's project looking into detecting life on the walls of volcanic caves from afar. For this purpose NASA engineers are using the [CaveR rover](https://nasa-braille.org/cave-r/) equipped with DSLR cameras and Velodyne LiDAR to perform its tasks.

7) Publication of the Week - Expecting the Unexpected - Radiation Hardened Software (PDF).
<br>[NASA](https://ti.arc.nasa.gov/m/pub-archive/1075h/1075%20(Mehlitz).pdf)<br>
INFO: This week let's learn about Single Event Upsets (SEUs) or bit-flips. Bit-flips can occur when a cosmic ray or other source of radiation hits a memory die and causes a single bit to change state from 0 to 1 or vice versa. The reason I thought it would be interesting to cover this topic was [this article](https://www.theregister.co.uk/2019/08/02/737_max_cosmic_bit_flipping_test/) from The Register that tells us about an issue in Boeing 737 Max architecture where bit-flips can cause pilots to lose control of the aircraft. From the linked paper we can learn about the conventional and software based approaches for handling software in places where radiation is a concern. The core of the paper is about The Radiation Hardened Software Project (RHS), a software library that is resilient against probabilistic errors and handles error detection, recovery and reconfiguration (I quite like the idea of using checkpoints in software). If you like podcasts then [Radiolab](https://www.wnycstudios.org/story/bit-flip) has an excellent episode on bit-flips that focuses on voting machines and cars.

### Announcements

1) The FPV Drone Racing VIO Competition.
<br>[GitHub](https://github.com/uzh-rpg/IROS2019-FPV-VIO-Competition)<br>
INFO: University of Zurich Robot Perception Group is organizing an FPV Drone Racing Visual Inertial Odometry competition. The participants will work with [UZH-FPV Drone Racing Dataset](http://rpg.ifi.uzh.ch/uzh-fpv.html) (you might know it from the [awesome weekly robotics list](https://github.com/msadowski/awesome-weekly-robotics)) with the goal of estimating the drone position as well as possible. The author of the best solution will win $1,000 and a chance to present their approach at the IROS 2019 Workshop "Challenges in Vision-based Drone Navigation". The deadline to submit estimated trajectories is 1st of October 2019.
