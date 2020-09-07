---
title: "Weekly Robotics"
description: "This week in WR newsletter: an open source Mars rover, tuning wheel odometry for mobile robots, a new open source quadrotor simulator and more!"
date: 2020-09-07
tags: [Robotics, Careers]
idx: 107
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [ESA (ExoMy)](https://esa-prl.github.io/ExoMy/)*

> These past few days I am mostly focused on moving to another country therefore this issue might appear a bit more lightweight than you are used to. I'm expecting a full WR recovery in 2 weeks! The most clicked last week was [the article from National Geographic on robot revolution](https://www.nationalgeographic.com/magazine/2020/09/the-robot-revolution-has-arrived-feature/) with 12.8% opens.

{:.post-entry-title}
#### ExoMy

{:.post-source}
[ESA](https://esa-prl.github.io/ExoMy/)

ExoMy is a 3D printed open source rover developed by ESA. The rover should cost approximately 250-500 Euro to build. The [software](https://github.com/esa-prl/ExoMy_Software) seems to be running ROS. The [hardware repository](https://github.com/esa-prl/ExoMy) contains all build instructions and a [BOM](https://github.com/esa-prl/ExoMy/wiki/Purchasing-Instructions). I think this Rover is a nice alternative to the $2500 NASA's [Open Source Rover](https://opensourcerover.jpl.nasa.gov).

----

{:.post-entry-title}
#### Deploying on Mars: Rock Solid Odometry for Wheeled Robots

{:.post-source}
[Freedom Robotics](https://www.freedomrobotics.ai/blog/tuning-odometry-for-wheeled-robots)

While we are on the topic of Mars: In this blog post Achille Verheye does a good summary of tuning wheel odometry for mobile robots. Mostly ROS is covered but as long as your mobile robot uses EKF then you should learn something useful.

----

{:.post-entry-title}
#### Autonomous Off-Road Food Delivery With Pixhawk

{:.post-source}
[Hackaday](https://hackaday.com/2020/09/04/autonomous-off-road-food-delivery-with-pixhawk/)

Do you want to run a robotics based delivery service? You might consider modifying an R/C car with Pixhawk running Px4 / ArduPilot - just be aware of the ramps on the robot's path!

----

{:.post-entry-title}
#### Self-Driving Cars with ROS and Autoware

{:.post-source}
[Autoware](https://www.autoware.org/awf-course)

The course on ROS2 and autonomous cars from Autoware is now complete! All 14 lectures are available on the website above.

----

{:.post-entry-title}
#### Flightmare

{:.post-source}
[UZH-RPG](https://uzh-rpg.github.io/flightmare/)

Researchers from Robotics and Perception Group have developed an open source quadrotor simulator. "Flightmare is composed of two main components: a configurable rendering engine built on Unity and a flexible physics engine for dynamics simulation. Those two components are totally decoupled and can run independently from each other. Flightmare comes with several desirable features: (i) a large multi-modal sensor suite, including an interface to extract the 3D point-cloud of the scene; (ii) an API for reinforcement learning which can simulate hundreds of quadrotors in parallel; and (iii) an integration with a virtual-reality headset for interaction with the simulated environment. Flightmare can be used for various applications, including path-planning, reinforcement learning, visual-inertial odometry, deep learning, human-robot interaction, etc."

----

{:.post-entry-title}
#### An Up-Close Look At The First Martian Helicopter

{:.post-source}
[Hackaday](https://hackaday.com/2020/09/02/an-up-close-look-at-the-first-martian-helicopter/)

Ingenuity makes a comeback to the newsletter. This is probably the most detailed write up about the Martian helicopter that I've came across. I had no idea the motors were hand-wired with copper wires with rectangular cross-section.

----

{:.post-entry-title}
#### GSoC and Intern Projects for Summer 2020

{:.post-source}
[ROS Discourse](https://discourse.ros.org/t/gsoc-and-intern-projects-for-summer-2020/16237)

Would you like to know what Google Summer of Code interns were up to this year while working on Ignition Gazebo. Some of the projects look very interesting! You should also check out the comments in the thread where some of the interns from Open Robotics described their projects as well.

<br>
<div class="sponsor-snippet-wrapper">
    <div class="sponsor-snippet container-fluid">
        <div class="row">
            <div class="col-3 d-none d-sm-block"></div>
                <div class="col-sm-12 col-md-6 nopadding">
                    <h3 id="spoonsored">Sponsored</h3>

                <p class="sponsor-blurb">Huge thanks to all of the Weekly Robotics <a href="https://weeklyrobotics.com/supporters">supporters</a> helping this project through <a href="https://www.patreon.com/WeeklyRobotics">Patreon</a> and the following business partners:</p>

                <div class="row">
                    <div class="col"><a href="http://msadowski.ch/"><img src="img/sponsors/m_consulting.png" alt="M. Sadowski Consulting"></a></div>
                </div>

            </div>
        </div>
    </div>
</div>

----

### Careers

{:.post-entry-title}
#### Knightscope (Mountain View, CA, US)

{:.post-source}
[Senior Robotics Engineer](https://knightscope.bamboohr.com/jobs/view.php?id=8)

Knightscope is developing technology that will predict and prevent crime. Our Crime Fighting Autonomous Data Machines - a large-scale deployment of autonomous technology, sensors, robotics and predictive analytics - will gather real-time on-site data and combine it with existing large data sets as well as relevant social network feeds, allowing for a breakthrough ability to map the future in a given environment.
