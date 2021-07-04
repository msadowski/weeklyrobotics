---
title: "Weekly Robotics"
description: "This week in WR: a roadmap for learning SLAM, an open source farming rover, legged robots for low gravity applications, 3D SLAM package and more!"
date: 2021-07-05
tags: [Robotics, Research, Learning, SLAM, Sensors, ROS, AutonomousRobots]
idx: 150
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> A [Q2 2021 newsletter update](https://www.patreon.com/posts/53155007) is out for the newsletter patrons! If you would like to support this project and join our Slack channel that would be amazing! If you would rather not, not an issue, you are still going to get the same newsletter as always. As a spoiler to the Q2 update: our year to date subscription growth is 21.77%. The most clicked link last week was [the open-source farm robot](https://farm.bot/) with 20.9% opens. As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/).

----
<div class="sponsor-snippet-wrapper">
    <div class="sponsor-snippet container-fluid">
        <div class="row">
            <div class="col-3 d-none d-sm-block"></div>
                <div class="col-sm-12 col-md-6 nopadding">
                    <h3 id="spoonsored">Sponsored</h3>

                <h4 class="post-entry-title">Making a 3D mapping prototype with ROS</h4>
                <span class="sponsor-source">
                    <a href="https://msadowski.github.io/3d-mapping-with-ros/">msadowski.github.io</a>
                </span>
                <p class="sponsor-blurb">In the past 3 months I've been working on integrating a LiDAR, RTK GNSS and an IMU to create a proof of concept 3D mapping device. The above post sums up my experience and lessons learned while making this prototype, all using open source ROS packages.</p>

            </div>
        </div>
    </div>
</div>
----

{:.post-entry-title}
#### Visual SLAM Roadmap

{:.post-source}
[GitHub](https://github.com/changh95/visual-slam-roadmap)

Hyunggi Chang had put together a set of diagrams listing the skills one would likely need to become a visual SLAM developer. This might be of interest to anyone looking to specialize in this area.

----

{:.post-entry-title}
#### RBR50 Robotics Innovation Awards

{:.post-source}
[Robotics Business Review](https://www.roboticsbusinessreview.com/rbr-50-2020-innovations/)

"Each year since 2012, Robotics Business Review has produced the RBR50 Robotics Innovation Awards, which recognize and celebrate forward thinking companies and the original, impactful solutions they have created. Widely recognized throughout the world as a leading indicator of robotics innovation leadership, the RBR50 Robotics Innovation Awards are also a critical measure of robotics sector growth".

----

{:.post-entry-title}
#### A closer look at Acorn, our open source precision farming rover

{:.post-source}
[TwistedFields](https://community.twistedfields.com/t/a-closer-look-at-acorn-our-open-source-precision-farming-rover/108)

Acorn is an open-source rover being developed by the TwistedFields community. The current version of the robot uses eight 100 watts solar panels. Each of the wheel assemblies has built-in steering. For each of the wheels, an [ODrive](https://odriverobotics.com/) motor controller is used for control of the steering and wheel motion. I'll be looking forward to seeing this project grow.

----

{:.post-entry-title}
#### Legged Robots Do Surprisingly Well in Low Gravity

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/space-robots/legged-robots-surprisingly-well-low-gravity)

Here comes a SpaceBok update! We've covered this system back in [issue #47](https://weeklyrobotics.com/weekly-robotics-47), from the videos and images it looks like the system went through some redesign. After 2 years, I still like the idea of using a wheeled mobile robot being used to simulate low gravity. If you would like to learn more about this work, check out [this publication](https://arxiv.org/abs/2106.09357).

----

{:.post-entry-title}
#### Pre-release testing on ROS2?

{:.post-source}
[ROS Discourse](https://discourse.ros.org/t/pre-release-testing-on-ros2/21126)

Tyler Weaver had prepared a short video ROS2 pre-release testing.

----

{:.post-entry-title}
#### Austin Cyclists Split On Sharing Bike Lanes With Pizza Delivery Robots

{:.post-source}
[Houston Public Media](https://www.houstonpublicmedia.org/articles/news/transportation/2021/06/24/401460/austin-cyclists-split-on-sharing-bike-lanes-with-pizza-delivery-robots/)

This article raises a few very good questions on what part of the road could be utilized by small delivery vehicles. In Austin, the robots are allowed to be deployed on bike lanes, making some bikers unhappy, while others see it as a chance for improving the infrastructure for everyone.

----

{:.post-entry-title}
#### HDL Graph SLAM

{:.post-source}
[GitHub](https://github.com/koide3/hdl_graph_slam)

"hdl_graph_slam is an open source ROS package for real-time 6DOF SLAM using a 3D LIDAR. It is based on 3D Graph SLAM with NDT scan matching-based odometry estimation and loop detection. It also supports several graph constraints, such as GPS, IMU acceleration (gravity vector), IMU orientation (magnetic sensor), and floor plane (detected in a point cloud). We have tested this package with Velodyne (HDL32e, VLP16) and RoboSense (16 channels) sensors in indoor and outdoor environments".
As Adrian pointed on WR Slack, two papers evaluated this SLAM implementation: [A comparison of LiDAR-based SLAM systems for Control of Unmanned Aerial Vehicles](https://arxiv.org/pdf/2011.02306.pdf) and [Interactive 3D Graph SLAM for Map Correction](https://unit.aist.go.jp/hcmrc/mr-rt/papers/published/interactive_slam_RA-L2020.pdf) with various results.
