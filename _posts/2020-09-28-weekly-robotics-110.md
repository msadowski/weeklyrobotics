---
title: "Weekly Robotics"
description: "This week in WR: ocean exploration live thanks to @EVNautilus, a home security drone critique, open source code for airborne wind turbine, computer vision recipes from @OpenAtMicrosoft, and more!"
date: 2020-09-28
tags: [Robotics, Careers]
idx: 110
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Ocean Exploration Trust](https://nautiluslive.org/tech/rov-hercules)*

> To give you a glimpse on what's going on in the Weekly Robotics Supporter's Slack, we've had discussions on [NVIDIA Isaac SDK](https://youtu.be/v_ulHMfDUco) and [Ring's flying camera](https://www.theverge.com/2020/9/24/21453709/ring-always-home-cam-indoor-drone-security-camera-price-specs-features-amazon). If you would like to join the conversation then [consider supporting the project](https://www.patreon.com/WeeklyRobotics). Your contribution will allow me to spend way more time working on this newsletter! The most clicked last week was [the ROS 2020 metrics report](https://discourse.ros.org/t/2020-ros-metrics-report/16394) with 15.9% opens.

{:.post-entry-title}
#### Nautilius Live

{:.post-source}
[Ocean Exploration Trust](https://nautiluslive.org/live/quad)

Did you know that you can follow an ocean exploration mission from the comfort of your home? Dr Robert Ballard and the Corps of Exploration have been streaming their work live for quite some time now and you can see the livestream on it on the above page. Huge thanks to [Yousof](https://www.linkedin.com/in/ebneddin/) for letting me know about this project!

----

{:.post-entry-title}
#### Why You Should Be Very Skeptical of Ring's Indoor Security Drone

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/drones/ring-indoor-security-drone)

If you have read The Verge's article on Ring's drone then you might want to consider to read this one too, as it provides some cons to the idea of a surveillance robot running in your personal space.

----

{:.post-entry-title}
#### Computer Vision Recipies

{:.post-source}
[GitHub](https://github.com/microsoft/computervision-recipes/tree/master/scenarios)

Microsoft has an Open Source repository with some computer vision recipies in the form of Iron Python Notebooks. In the repo, you will find information on such topics as classification, detection, keypoints, segmentation and more.

----

{:.post-entry-title}
#### Life Sized Gundam in Testing mode

{:.post-source}
[Twitter](https://twitter.com/catsuka/status/1308068858541023232)

So, Yokohama's Gundam is now moving. It looks like the legs don't bear the weight of the robot, which is understandable but slightly disappointing.

----

{:.post-entry-title}
#### makani

{:.post-source}
[GitHub](https://github.com/google/makani)

"Makani was a project to develop a commercial-scale airborne wind turbine, culminating in a flight test of the Makani M600 off the coast of Norway. All Makani software has now been open-sourced. This repository contains the working Makani flight simulator, controller (autopilot), visualizer, and command center flight monitoring tools. Additionally, almost all avionics firmware is also included, albeit potentially not in a buildable state, due to the removal of some third-party proprietary code. We hope that this code will be inspirational and useful to the kite-based windpower and wider communities".

----

{:.post-entry-title}
#### Why Wasn't Uber Charged in a Fatal Self-Driving Car Crash?

{:.post-source}
[Wired](https://www.wired.com/story/why-not-uber-charged-fatal-self-driving-car-crash/)

The safety driver of the Uber car that killed a woman in 2018 has been charged with a crime, while Uber won't face any charges.

----

{:.post-entry-title}
#### Reforming 3D Prints With Salt And Heat

{:.post-source}
[Hackaday](https://hackaday.com/2020/09/23/reforming-3d-prints-with-salt-and-heat/)

I did not know that annealing of 3D prints can be a thing until I've read this article and watched the video. A very, neat method in which you tightly pack your print in salt and then bake it for some time so that the plastics can re-melt.

----

{:.post-entry-title}
#### Publication of the Week - RTAB-Map as an Open-Source Lidar and Visual SLAM Library for Large-Scale and Long-Term Online Operation (2018)

{:.post-source}
[introlab.3it.usherbrooke.ca](https://introlab.3it.usherbrooke.ca/mediawiki-introlab/images/7/7a/Labbe18JFR_preprint.pdf)

Until last week, every time I tried RTAB-Map I was starting with the [handheld demo](http://wiki.ros.org/rtabmap_ros/Tutorials/HandHeldMapping) and was deciding that it's probably not going to work well enough for my needs. Only after reading this paper, I realised how wrong I was. It turns out that if you are running RTAB-Map you can quite easily restrict the localization to 3-axes (X, Y, Yaw) - perfect for mobile robots, and also provide a LiDAR and odometry input. As you will also see in the attached paper it does quite well on some of the openly available datasets. It's time to get some VSLAM done!

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

### Careers

{:.post-entry-title}
#### Furhat Robotics (Stockholm, Sweden)

{:.post-source}
[Software Engineer - Java/Kotlin](https://emp.jobylon.com/jobs/16824-furhat-robotics-software-engineer-javakotlin-platform-core/)

Furhat Robotics is a Stockholm based startup building the world’s most advanced social robotics platform. We are a collective of doers and dreamers driven by one common goal: making the promise of social robots a reality.
