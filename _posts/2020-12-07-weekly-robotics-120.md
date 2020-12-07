---
title: "Weekly Robotics"
description: "This week in WR: evolutionary robot design, an open-source optimization toolset for robotics, ball manipulating quadruped, difficulties in robot navigation and more!"
date: 2020-12-07
tags: [Robotics, Space, ROS, OpenSource, Software, DIY, Quadrupeds, Control]
idx: 120
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [MIT](https://news.mit.edu/2020/computer-aided-robot-design-1130)*

> Did you know that newsletter's Patreon supporters get a [monthly pick](https://www.patreon.com/posts/monthly-robotics-44481777) with highlights of the projects featured in the WR in a given month. Your support, even if it's one coffee equivalent per month, would really help me take this project to the next level. The most clicked link last week was [grad SLAM](https://gradslam.github.io/) with 19.0% opens.

{:.post-entry-title}
#### Computer-Aided Creativity in Robot Design

{:.post-source}
[MIT](https://news.mit.edu/2020/computer-aided-robot-design-1130)

RoboGrammar is a tool designed by MIT researchers that iteratively creates robot designs using graph grammar to traverse various types of terrains. You can find a paper describing this project in detail [here](https://people.csail.mit.edu/jiex/papers/robogrammar/paper.pdf).

----

{:.post-entry-title}
#### How To Start a Robot Revolution

{:.post-source}
[Red Hat](https://www.redhat.com/en/open-source-stories/robots/breaking-the-wheel)

Last week all episodes of Red Hat documentary on ROS was released. A perfect addition to the documentary on Makani that I added to [awesome-wr](https://github.com/msadowski/awesome-weekly-robotics) the other day.

----

{:.post-entry-title}
#### EXOTica

{:.post-source}
[GitHub](https://github.com/ipab-slmc/exotica)

The EXOTica library is a general Optimisation Toolset for Robotics platforms, written in C++ with bindings for Python. Its motivation is to provide a more streamlined process for developing algorithms for tasks such as Inverse Kinematics, Trajectory Optimisation, and Optimal Control.

----

{:.post-entry-title}
#### Hayabusa-2: Capsule with Asteroid Samples in 'Perfect' Shape

{:.post-source}
[BBC](https://www.bbc.com/news/science-environment-55201662)

Hayabusa-2 successfully delivered rock samples from the asteroid it reached on June 2018. As a quick refresher: Hayabusa-2 carried [two hopping rovers](http://www.hayabusa2.jaxa.jp/en/topics/20180919e/) that landed on the Asteroid in September 2018. As a mission extension, the spacecraft will now target rendezvous with [1998 KY26](https://en.wikipedia.org/wiki/1998_KY26) in 2031.

----

{:.post-entry-title}
#### 2020 Al Extrusion Erector Set

{:.post-source}
[Hackaday](https://hackaday.io/project/12480-2020-al-extrusion-erector-set)

A Collection of 3D printable parts for building machines and other mechanical creations from 2020 Aluminum Extrusions. These parts are meant to be used with 2020 Aluminum extrusion cut to length for the application. They are designed with M4 screws for M4 sized T-nuts, the holes all have 2mm countersink and are meant for hex socket cap head screws.

----

{:.post-entry-title}
#### Eight Degrees of Difficulty for Autonomous Navigation

{:.post-source}
[PickNik](https://picknik.ai/ros/navigation/2020/12/04/navigation.html)

A well-written piece by David Lu!! explaining the biggest issues you will likely come across when working on autonomous navigation. "However, most mobile robots need to avoid the obstacles around them, if for no other reason than roboticists hate getting their shins bumped all the time" - I can confirm this is very true.

----

{:.post-entry-title}
#### Publication of the Week - Circus ANYmal: A Quadruped Learning Dexterous Manipulation with Its Limbs (2020)

{:.post-source}
[arXiv](https://arxiv.org/abs/2011.08811)

Since the previous article featured an [ANYmal quadruped](https://www.anybotics.com/anymal-legged-robot/) it is high time to feature this paper (big thanks to [Julius](https://www.linkedin.com/in/juliussust/) for pointing it out to me). In this research, the quadruped is placed on its back and an exercise ball with mocap markers is placed on its legs. The robot is then tasked with rotating the ball at a desired angular velocity. The team had used deep reinforcement learning to train the robot in simulation. The video showing the ball manipulation can be found on [YouTube](https://youtu.be/lmWSw_Hl9l8). Are we going to see robotics circuses in the near future?

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
