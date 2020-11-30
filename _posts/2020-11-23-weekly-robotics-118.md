---
title: "Weekly Robotics"
description: "WR 118: Robot simulation in Unity, 3D printing enclosures, a documentary about flying windmills, licence plates for robots and more!"
date: 2020-11-23
tags: [Robotics, Drones, Simulation, 3DPrinting]
idx: 118
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Unity](https://unity.com/)*

> Today's issue is short and to the point. Towards the end of the issue, I will digress from robotics quite a bit to talk about geoscience. The most clicked link last week was [the multirotor with a tensegrity shell](https://hackaday.com/2020/11/05/quadcopter-with-tensegrity-shell-takes-a-beating-and-gets-back-up/) with 13.1% opens.

{:.post-entry-title}
#### Robotics Simulation in Unity Is as Easy as 1, 2, 3!

{:.post-source}
[Unity](https://blogs.unity3d.com/2020/11/19/robotics-simulation-in-unity-is-as-easy-as-1-2-3/)

Unity is capitalizing on ROS, with a new set of tools for importing URDFs and communicating with ROS based systems. The demonstration in the article is a pick-and-place application, you can find the tutorial on it on [GitHub](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/README.md#part-3-naive-pick--place)

----

{:.post-entry-title}
#### Enclosure design for 3D printing: A step-by-step guide

{:.post-source}
[3D Hubs](https://www.3dhubs.com/knowledge-base/enclosure-design-3d-printing-step-step-guide/)

If you find yourself 3D printing some enclosures every now and then then you might find this article by John Wall helpful.

----

{:.post-entry-title}
#### Why We Need a Robot Registry

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/robotics/humanoids/why-we-need-a-robot-registry?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+IeeeSpectrum+(IEEE+Spectrum))

A thought-provoking piece by Stacey Higginbotham, in which she makes a point on putting a 'licence plates' on the robot you might find in public spaces.

----

{:.post-entry-title}
#### ROS World Talks Are Posted!

{:.post-source}
[ROS Discourse](https://discourse.ros.org/t/ros-world-talks-are-posted/17436)

ROS World 2020 sessions have been published! You will find the links to all the videos in this blog post by Katherine Scott.

----

{:.post-entry-title}
#### Elios 2 Helps Researchers Inspect Reactor Five at Chernobyl

{:.post-source}
[YouTube (Flyability)](https://youtu.be/yyZZSyCmBqY)

Flyability took part in some Research at Chernobyl, resulting in the above video. If you like the idea of using Robotics in irradiated places then you might like [this coverage](https://www.popularmechanics.com/technology/robots/a34480039/spot-robot-dog-chernobyl-radiation/) of Researchers deploying Spot in Chernobyl.

----

{:.post-entry-title}
#### Pulling Power from the Sky: The Story of Makani [Feature Film]

{:.post-source}
[YouTube (X, the moonshot factory)](https://youtu.be/qd_hEja6bzE)

[Makani](https://x.company/projects/makani/) was a moonshot project by X, aiming to harness wind power using kites/drones, that was shut down this year. I've only started watching this documentary about Makami project, but I already know that I can fully recommend it. If you enjoy seeing an applied iterative process in Robotics with some drones occasionally crashing then this film is definitely for you.

----

{:.post-entry-title}
#### Publication of the Week - HOPPY: An open-source and low-cost kit for dynamic robotics education (2020)

{:.post-source}
[arXiv](https://arxiv.org/abs/2010.14580)

[Hoppy](https://github.com/RoboDesignLab/HOPPY-Project/) is an open source kit for robot education that dynamically hops around a rotating gantry, developed by researches from the University of Illinois. From the paper, it looks like you can teach students lots of concepts using just this kind of robot.

----

{:.post-entry-title}
#### Robotics, Python and Geoscience

Last week I was heavily looking into using USVs for mapping water body depth. When it comes to requirements I wanted to use Python to quickly visualise some of the data. In my quest, I came across two interesting libraries: [pyproj](https://pypi.org/project/pyproj/) for geographic projections and [verde](https://www.fatiando.org/verde/latest/), a package for processing and gridding spatial data. A very useful set of tutorials that really helped me wrap my head around many aspects of geoscience with Python was the [xlines repository](https://github.com/agile-geoscience/xlines) by Agile Geoscience. I’ve also learned that if you are not 100% sure what you are doing [Jupyter Notebook](https://jupyter.org/) will speed up your development 10x. Thanks to this exercise I can appreciate the amount of work that goes into [projects like these](https://www.mbari.org/at-sea/vehicles/autonomous-underwater-vehicles/seafloor-mapping-auv).

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
