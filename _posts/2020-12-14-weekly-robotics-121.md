---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: the best coverage of Boston Dynamics acquisition I found, an autonomous excavator, an interesting approach to human-robot collaboration, a free self-driving cars course and more!"
date: 2020-12-14
tags: [Robotics, AutonomousCars, DIY, Business, Research, MobileRobots, ConstructionRobots, Libraries, OpenSource]
idx: 121
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Boston Dynamics](https://www.bostondynamics.com/)*

> Last Wednesday I did a 'throwback Wednesday' on [Twitter](https://twitter.com/WeeklyRobotics/status/1336732366895804418), where I looked at Weekly Robotics newsletter issue published exactly 2 years ago. Would you find such an addition to the main newsletter interesting? You can voice your opinion in [this survey](https://forms.gle/4aWbiegnCw2w8exeA) that I designed to take less than 47 seconds. The most clicked link last week was the article [Eight Degrees of Difficulty for Autonomous Navigation](https://picknik.ai/ros/navigation/2020/12/04/navigation.html) with 19.6% opens.

{:.post-entry-title}
#### Hyundai Buys Boston Dynamics for Nearly $1 Billion. Now What?

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/humanoids/hyundai-buys-boston-dynamics)

This is the most well-written piece about Hyundai's about the acquisition.

----

{:.post-entry-title}
#### HEAP

{:.post-source}
[ETH](https://rsl.ethz.ch/robots-media/heap.html)

HEAP (hydraulic excavator for an autonomous purpose) is a robotized machine being developed by the Researchers at Robotics Systems Lab. The [video of Robotic Embankment Prototype](https://youtu.be/Wjq3Nf9rWrM) looks really good. The [follow-up video](https://youtu.be/IbMZTErlQNU) where the platform is teleoperated to clear rock slides is also interesting. For the latest publication about this project, you can check [this open access IROS 2020 paper](https://www.research-collection.ethz.ch/handle/20.500.11850/444474). Big thanks to [Julius](https://www.linkedin.com/in/juliussust/) for making me aware of this!

----

{:.post-entry-title}
#### Trajekt T1 Product Demo

{:.post-source}
[Vimeo](https://vimeo.com/454792845)

I have stolen this video from the ROS Discourse [ROS news of the week](https://discourse.ros.org/t/ros-news-for-the-week-of-11-30-2020/17750). It shows a baseball pitch replication robot. The machine looks pretty complex but the results are mind-blowing.

----

{:.post-entry-title}
#### Real Life Baby Yoda with AI

{:.post-source}
[YouTube (Manuel Ahumada)](https://youtu.be/PEj8jWapGt4)

Manuel recently got in touch with me to share his latest video showing his [OpenBot](https://www.openbot.org) based DIY mobile robot build. If you enjoy build video logs or you've never seen OpenBot than this video is for you.

----

{:.post-entry-title}
#### Perception-Based Region Selection for Human to Robot Collaboration

{:.post-source}
[ROS Industrial](https://rosindustrial.org/news/2020/12/10/perception-based-region-selection-for-human-to-robot-collaboration)

This is certainly one way to do a human-robot collaboration - a person can draw 'areas of interest' on the workpiece with the marker that robot can then automatically detect and attend to them (in case of the above article by sanding it). What is more amazing is that the ROS package developed for this research had been [open-sourced](https://github.com/swri-robotics/Region-Detection) with a BSD licence.

----

{:.post-entry-title}
#### Crocoddyl

{:.post-source}
[GitHub](https://github.com/loco-3d/crocoddyl)

Crocoddyl is an optimal control library for robot control under contact sequence. Its solver is based on various efficient Differential Dynamic Programming (DDP)-like algorithms.

----

{:.post-entry-title}
#### Best Week Ever for Robotaxis?

{:.post-source}
[The Robot Report](https://www.therobotreport.com/best-week-ever-for-robotaxis/)

From the article, it seems like we could make a whole issue of this newsletter about autonomous cars and we wouldn't run out of content. The above article describes an intensive week for autonomous cars with some acquisitions, regulatory approvals and new testing sites.

----

{:.post-entry-title}
#### Publication of the Week - Localization of Sound Sources in Robotics: A Review (2017)

{:.post-source}
[Science Direct](https://www.sciencedirect.com/science/article/pii/S0921889016304742)

[Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/): Localization is a huge topic for mobile robots. This article reviews a very particular and interesting way of localization using sound. The author explains all the steps towards SSL (sound source localization) pipeline and shows all the methods currently used in each one of them. This is a great reading for those who want to implement SSL in their robot.

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

### Announcements

{:.post-entry-title}
#### The Duckietown Massive Online Open Course

{:.post-source}
[Duckie Town](https://www.duckietown.org/mooc)

The Duckietown Foundation presents the first hardware based massive online open course (MOOC) in AI and robotics: “Self-driving cars with Duckietown”, free on edX. Learn autonomy hands-on by making real robots take their own decisions and accomplish broadly defined tasks. Step by step from the theory, to the implementation, to the deployment in simulation as well as on Duckiebots. The course will start in February 2021.

----

{:.post-entry-title}
####  Drone X Challenge 2020 - Phase III

{:.post-source}
[DXC](https://dronexchallenge2020.com/)

A US$1.5+ Million Global Challenge (US$1 Million Final Prize and US$500,000+ in R&D Grants) that is pushing the frontiers of R&D and innovation in drone technologies. DXC 2020 aims at accelerating the practical deployment of drones/UAVs in key applications focusing on transportation and delivery. DXC 2020 will support innovative commercial applications/solutions that tackle two major challenges: payload capacity and flight endurance. Companies that didn't participate in Phase I or II can apply directly to Phase III. The deadline for the application is 15th of January 2021.
