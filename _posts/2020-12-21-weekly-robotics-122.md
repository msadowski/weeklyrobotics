---
title: "Weekly Robotics"
description: "This week in your robotics newsletter of choice: wheeled-legged robots, a DIY desktop windtunnel, a modular robot navigation framework, solar-based skin for robot arms, a course on robotic manipulation and more!"
date: 2020-12-21
tags: [Robotics, MobileRobots, LeggedRobots, Quadrupeds, DIY, Navigation, Localization, Space, ROS, SoftRobots]
idx: 122
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [FZI](https://www.fzi.de/en/research/fzi-house-of-living-labs/)*

> Something I enjoy before Christmas (except from the certain song by Wham), are the Robotic themed Christmas videos. The one I liked the most this year was shared by Ignat on the WR Slack: [FZI Living Lab Christmas Robotics 2020](https://youtu.be/rzUcpFGHQqE). The 6-legged Robot featured in the video certainly looks interesting - I will do some digging and provide you with some quality information about it in one of the future issues. Literally 30 minutes before publication of this newsletter issue, Kenneth shared [this one](https://youtu.be/lCS7L4SdVsc), made the folks from his lab, that I also enjoyed! I wish [Ascento](https://www.ascento.ethz.ch/) was brining me presents every year too! Last week, I've asked your opinion on analyzing the features published 2 years ago. Since everyone that had taken the survey was either liked the idea or was indifferent we will give it a shot! The most clicked link last week was [the report on Boston Dynamics acquistion](https://spectrum.ieee.org/automaton/robotics/humanoids/hyundai-buys-boston-dynamics) with 13.8% opens.

{:.post-entry-title}
#### Wheels Are Better Than Feet for Legged Robots

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/wheels-are-better-than-feet-for-legged-robots)

Here is a short article on equipping legged robots with wheels - making the robot capable of executing hybrid gaits. The interesting bit of information is that the robot can change the gait just based on the feel of the terrain, creating a good compromise between energy efficiency and the ability to go through obstacles. The first mention of equipping quadrupeds with wheels I came across was back in 2019 when I featured [this paper](https://arxiv.org/abs/1809.03557) in the [issue #33](https://weeklyrobotics.com/weekly-robotics-33) - it's the same team as described in the article, working with the previous version of ANYmal.

----

{:.post-entry-title}
#### Desktop Windtunnel

{:.post-source}
[YouTube (Mark Waller)](https://youtu.be/Sx5BQjKvElk)

A really cool DIY wind tunnel build, using drinking straws to provide laminar flow into the tunnel. The smoke is generated using an e-cigarette connected to an aquarium pump. The project looks very simple, yet it provides great results for this scale. If you end up inspired by this, let me know and I will be more than happy to feature your work in the newsletter!

----

{:.post-entry-title}
#### A Puppet and a Robot Walk into a Moonshot Factory

{:.post-source}
[X](https://blog.x.company/a-puppet-and-a-robot-walk-into-a-moonshot-factory-561c383a96f2)

What can you translate experience from puppeteer into robotics? You can learn that in this article by Benjie Holson, who started working as a puppeteer at the age of 5 and then became robotics engineer at X. One of the concepts that stood out for me in this article is how gaze is important for the robots to seem more capable and social.

----

{:.post-entry-title}
#### GeRoNa

{:.post-source}
[GitHub](https://github.com/cogsys-tuebingen/gerona)

"GeRoNa (Generic Robot Navigation) is a modular robot navigation framework, that bundles path planning and path following (including obstacle detection) and manages communication between the individual modules. It is designed to be easily extensible for new tasks and robot models". I have to say [the video](https://youtu.be/Ppdi7dQ7Vzw) showing the framework on various robot platforms looks quite promising.

----

{:.post-entry-title}
#### Solar-based Electronic Skin Generates Its Own Power

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/tech-talk/robotics/robotics-hardware/solarbased-electronic-skin-that-generates-its-own-power)

Here is an inspirational idea from [BEST](https://www.gla.ac.uk/research/az/best/) (Bendable Electronics and Sensing Technologies) group at the University of Glasgow: create an electronic skin for the robot with solar cells that not only power the skin itself, but that can be used for proximity sensing when an approaching object covers the light source.

----

{:.post-entry-title}
#### ROS 2 Galactic Default Middleware Announced

{:.post-source}
[ROS Discourse](https://discourse.ros.org/t/ros-2-galactic-default-middleware-announced/18064)

The default middleware of ROS 2 has been announced. Spoiler: it's [Cyclone DDS](https://github.com/eclipse-cyclonedds/cyclonedds). I found [the report](https://osrf.github.io/TSC-RMW-Reports/) mentioned in the article very interesting, as it allowed me to get an idea what to expect from the two DDS implementation considered in terms of CPU and memory footprint, latency, and behaviour on lossy networks.

----

{:.post-entry-title}
#### Publication of the Week - Robotic Manipulation (2020)

{:.post-source}
[manipulation.csail.mit.edu](http://manipulation.csail.mit.edu/index.html)

This is a series of lecture notes by Russ Tedrake from an MIT 6.881 - Robotic Manipulation course. The course makes extensive use of [Drake](https://drake.mit.edu/), a toolbox for model-based design and verification for robotics. Lots of the materials are in the form of an interactive python notebook, allowing you to run them online. Some of the subsections of the notes, especially towards the end of the book, are missing, however, it's understandable since the course might still be in progress.

----
<div class="sponsor-snippet-wrapper">
    <div class="sponsor-snippet container-fluid">
        <div class="row">
            <div class="col-3 d-none d-sm-block"></div>
                <div class="col-sm-12 col-md-6 nopadding">
                    <h3 id="spoonsored">Sponsored</h3>

                <p class="sponsor-blurb">Huge thanks to all of the Weekly Robotics <a href="https://weeklyrobotics.com/supporters">supporters</a> helping this project through <a href="https://www.patreon.com/WeeklyRobotics">Patreon</a> and the following business partners:</p>

                <div class="row">
                    <div class="col"><a href="http://msadowski.ch/"><img src="img/sponsors/m_consulting.png" alt="M. Sadowski Consulting"></a></div>
                    <!-- <div class="col"><a href="#"><img src="img/Member_Logo.png" alt="Sponsor Logo"></a></div>
                    <div class="col"><a href="#"><img src="img/Member_Logo.png" alt="Sponsor Logo"></a></div>
                    <div class="col"><a href="#"><img src="img/Member_Logo.png" alt="Sponsor Logo"></a></div> -->
                </div>

                <!-- <hr>
                <h4 class="post-entry-title">TODO TITLE</h4>
                <span class="sponsor-source">
                    <a href="TODO LINK">TODO LINK TEXT</a>
                </span>
                <p class="sponsor-blurb">TODO: Description</p> -->
            </div>
        </div>
    </div>
</div>
----

{:.post-entry-title}
### Weekly Robotics 2 Years Ago

{:.post-source}
[Issue 18](https://weeklyrobotics.com/weekly-robotics-18)

Here are the highlights on what we were learning about 2 years ago:

[Metamaterials that changed shape under magnetic field](https://spectrum.ieee.org/tech-talk/robotics/robotics-hardware/new-class-of-metamaterials-changes-physical-properties-in-seconds). The concept of 4D materials (that change shape over time) sounds very cool. Unfortunately, I wasn't able to find any information on follow up research from the Lawrence Livermore National Laboratory. Sculpteo has a nice [overview of 4D printing research](https://www.sculpteo.com/en/3d-learning-hub/best-articles-about-3d-printing/4d-printing-technology/) that you might enjoy.

[CCM-SLAM](https://v4rl.ethz.ch/research/datasets-code/code--ccm-slam.html) is a centralized SLAM implementation by Researchers from ETH. In the video demonstrator, they showed 3 multirotors SLAMming together. The [project repository](https://github.com/VIS4ROB-lab/ccm_slam) is still active every now and then, and the [latest paper](https://www.research-collection.ethz.ch/handle/20.500.11850/313259) describing this solution was published in June 2019.

[ROS 2 Crystal release](https://discourse.ros.org/t/ros-2-crystal-clemmys-released/7137) took place right around this time 2 years ago. It reached an end of life one year later.

[NASA's Robotic Refueling Mission 3](https://www.nasa.gov/mission_pages/station/research/news/rrm3/) was super interesting. The project aimed at demonstrating a transfer of cryogenic fuel in orbit and test various robotic tools and vision systems for robotic refuelling. In April 2019 the cryogenic coolers [malfunctioned](https://www.nasa.gov/feature/goddard/2019/robotic-refueling-mission-3-update-april-12-2019) cutting the cryogenic transfer experiments short, however, a number of robotic experiments were still performed, with the [second set of operations](https://www.nasa.gov/feature/goddard/2020/nasa-s-refueling-mission-completes-second-set-of-robotic-tool-operations-in-space) taking place in October this year.
