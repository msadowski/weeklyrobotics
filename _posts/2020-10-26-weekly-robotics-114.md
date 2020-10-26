---
title: "Weekly Robotics"
description: "Last WR issue of October 2020: a robot swimming through grains, coverage planning in ROS, an interesting RC car robot build, a memristor-based balancing robot and more!"
date: 2020-10-26
tags: [Robotics, MobileRobots, AgriculturalRobots, ROS, Navigation, OpenSource, Hardware, Programming]
idx: 114
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Crover](https://www.crover.tech/)*

> Welcome to the last issue of October 2020! Last week I dug through some ROS packages for coverage planning, hence in the second feature, you will see a summary of what's out there. The most clicked link last week was [Robotics Backend ROS2 tutorials](https://roboticsbackend.com/category/ros2/) with 20.3% opens.

{:.post-entry-title}
#### Grain-Monitoring Robot Helps Prevent Food Waste

{:.post-source}
[ESA](https://www.esa.int/Space_in_Member_States/United_Kingdom/Grain-monitoring_robot_helps_prevent_food_waste)

While researching features for this issue I came across this blog post about the grain monitoring tethered robot and got very curious about how can a robot move through solid matter. Fortunately, the folks at Crover were very responsive and forwarded me [this video](https://vimeo.com/460609606) showing the robot going through some grains. Interesting stuff!

----

{:.post-entry-title}
#### Coverage Planning in ROS

I recently had a use case for a robot to cover the full mapped area (just like you would expect a Roomba to do) in ROS. In my quest, I've started checking out existing ROS packages to see what I could work with out of the box.

The first package I looked at was [boustrophedon_planner](https://github.com/Greenzie/boustrophedon_planner) from [Greenzie](https://www.greenzie.co/) since I knew it existed after I've featured it in [WR #50](https://www.sciencedirect.com/science/article/abs/pii/S092188901300167X). The package exposes an Action Server that you can use to send a Polygon message containing your outer boundary, and you will get a list of waypoints when the action server finishes.

Then I looked at [polygon_coverage_planning](https://github.com/ethz-asl/polygon_coverage_planning) from ETH ASL - the user interface in RVIZ is great, I had some issues working with it outside of RVIZ but in general, it should be a good option if you have some time to invest into fully checking out the workflow. The caveat: the readme file mentions that the memetic solver used in this package is free for non-commercial purposes only.

The last package I came across was [full_coverage_path_planner](https://github.com/nobleo/full_coverage_path_planner) by [Nobleo Technology](https://nobleo-technology.nl/) and supported by ROSIN. I didn't test this package (yet), as I was looking into generating straight paths through the area of interest, but it's good to know something like this exists, especially if you work with wheeled mobile robots.

----

{:.post-entry-title}
#### Jetson Nano Robot - Realsense, RPLidar, Joysticks

{:.post-source}
[Hackaday](https://hackaday.io/project/175387-jetson-nano-robot-realsense-rplidar-joysticks)

An interesting robot project - an RC car, with Jetson Nano running ROS2. From the project log, it seems like the author is right now working on implementing navigation/localization.

----

{:.post-entry-title}
#### Saildrone Fleet Completes First Arctic Mapping Mission

{:.post-source}
[Sail-World Cruising](https://www.sail-worldcruising.com/news/232433/Saildrone-completes-first-Arctic-mapping-mission?source=twitter)

A fleet of Saildrones made it from San Francisco to the Arctic to "identify the 20-meter and 50-meter isobaths (contour lines), delineating a virtual lane to be mapped for safe passage of commercial vessels and to demonstrate the ability to conduct remote bathymetric surveys using unmanned technology". The roundtrip for the vessels was 8k nautical miles. You can learn a bit more about the mission on [NOAA's website](https://www.nauticalcharts.noaa.gov/updates/autonomous-vessel-operations-in-the-arctic-lessons-learned-from-the-summer-2020-mapping-mission/).

----

{:.post-entry-title}
#### Brain-Inspired Robot Controller Uses Memristors for Fast, Efficient Movement

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/braininspired-robot-controller-uses-memristors-for-fast-efficient-movement)

This article describes the work done by the researchers at the University of Southern California and the Air Force Research Laboratory. By using [memristors](https://en.wikipedia.org/wiki/Memristor) the team had managed to develop a self-balancing two-wheel robot, reducing cycle time from 3034 microseconds to 6 (!). Developing an analog Kalman filter sounds like a big challenge, and I'll be looking forward to seeing what other advancements will spin out of this research.

----

{:.post-entry-title}
#### Researchers Building Robot with Wheels and Legs to Traverse Any Terrain

{:.post-source}
[The Robot Report](https://www.therobotreport.com/researchers-building-robot-wheels-and-legs/)

Texas A&M researchers are looking into military robots with wheels transforming into rotary legs so that the robots can climb stairs.

----

{:.post-entry-title}
#### Publication of the Week - So You Want to Build an Embedded Linux System? (2020)

{:.post-source}
[jaycarlson.net/](https://jaycarlson.net/embedded-linux/)

I've recently started reading this article on building an embedded Linux System. The article is quite long, to read it fully you should expect to commit about 2.5+ hours for it. Jay is very thorough when explaining why you should/shouldn't use a processor instead of a microcontroller. I think this post might be relevant for anyone looking into using embedded Linux in their projects. I bet you will also like Jay's attitude: "Continue working on your projects, but never be afraid to roll up your sleeves and commit to some quality practice time!".

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

                <hr>
                <h4 class="post-entry-title">Virtual Robotics Recruiting Event: November 13</h4>
                <span class="sponsor-source">
                    <a href="https://rebrand.ly/rmzwq">https://rebrand.ly/rmzwq</a>
                </span>
                <p class="sponsor-blurb"><a href="https://oneamericaworks.org/">One America Works</a> connects high-growth technology companies with the talent they need to grow in cities across America. We are hosting a free, virtual <a href="https://rebrand.ly/rmzwq">Robotics Recruiting Event</a> on November 13, featuring some of the fastest-growing robotics companies like Locomation, industry leaders like Honeywell, and research leaders like NREC. Attendees will interview one-on-one with up to 15 different companies for both internships and full-time roles. Register online or contact <a href="mailto:paige@oneamericaworks.org">paige@oneamericaworks.org</a>.</p>
            </div>
        </div>
    </div>
</div>
----

### Job Seekers

[In the issue #83](https://weeklyrobotics.com/weekly-robotics-83) I've started this section to try to help out those looking for work in the times of pandemic. If you are currently looking for work then feel free to [send me](mailto:mat@weeklyrobotics.com) your details in the same format as you can see in the entries below.

**Name**: Daniel Tobon Collazos (Colombian Citizenship)<br>
**Location**: Tralee, Ireland (until december 1st) --> Cali, Colombia (december 1st>)<br>
**Skills**: C/C++, computer vision, structure from motion, 3D mapping, point cloud processing, python, cmake, ROS, linux, system software, embedded software, robotics, OpenCV, image processing<br>
**Profile**: I am a mechatronics engineer with an emphasis on application development in robotics perception systems  — computer vision techniques, image processing, depth processing, path planning with ROS, CAD modelling, embedded systems and robotics. Now I’m interested in 3D mapping and localization projects, intelligent systems, perception, navigation, mobile robots, drones, autonomous vehicles, machine learning. At the moment, I am looking for a job in the US for the next year 2021. If nothing happens, I will be open to other locations<br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/danieltobonco43/), [Portfolio](http://danieltobon43.github.io/)<br>
**Email**: daniel.tobon@uao.edu.co<br>
