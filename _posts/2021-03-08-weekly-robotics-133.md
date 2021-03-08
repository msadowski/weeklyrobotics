---
title: "Weekly Robotics"
description: "This week in WR: Looking back at WR community meeting #2, static analysis of ROS projects, robots setting a working pace, deploying soft robots in Mariana Trench and more"
date: 2021-03-08
tags: [Robotics, ROS, MobileRobots, Sensors, Drones]
idx: 133
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Loon](https://loon.com/)*

> On Thursday last week we've held a Weekly Robotics Community meeting dedicated to Robocars. During the event we had Ignat and Adrian shared their experience working on two different Formula Student teams and Josh told us all about Autoware and the latest [Autoware.Auto 1.0.0 release](https://discourse.ros.org/t/autoware-auto-1-0-0-is-here/19085). Huge thanks to all the presenters! If you missed the event but you would still like to check out the presentation then thanks to [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/) you can find it [on YouTube](https://youtu.be/nNWgXSi-lds). The presentation slot for the next meetup on the 18th of March is still up for grabs, so if you have something cool to showcase then please [get in touch](mailto:mat@weeklyrobotics.com)! The most clicked link last week was [Michael DeKort's piece on Agile ruining Engineering](https://imispgh.medium.com/silicon-valley-and-agile-are-ruining-engineering-196099378028) with 18.0% opens.

{:.post-entry-title}
#### How Google's Hot Air Balloon Surprised Its Creators

{:.post-source}
[BBC](https://www.bbc.com/future/article/20210222-how-googles-hot-air-balloon-surprised-its-creators)

A nice piece from BBC on AI surprising its creators, starting with the Project Loon executing trajectories unexpected by engineers that, as it turned out, resulted in significant time savings. The article goes on to mention some other examples of AI gaming the rules and featuring our [favourite spreadhseet](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml) (you can also find it in the [Awesome-WR list](https://github.com/msadowski/awesome-weekly-robotics)).

----

{:.post-entry-title}
#### HAROS

{:.post-source}
[GitHub](https://github.com/git-afsantos/haros)

"HAROS is a framework for quality assurance of ROS-based code, mostly based on static analysis". The [usage docs](https://github.com/git-afsantos/haros/blob/master/docs/USAGE.md) seem quite user friendly. I'll be looking forward to checking it out in some of my projects in the future.

----

{:.post-entry-title}
#### Why I was wrong to be optimistic about robots

{:.post-source}
[Financial Times(https://www.ft.com/content/087fce16-3924-4348-8390-235b435c53b2)

An interesting opinion piece by Sarah O'Connor about how human-robot collaboration can put a strain on the human part of the duo by 'upping' the work pace and potentially leading to strain related injuries in some cases.

----

{:.post-entry-title}
#### Assignment 1: Kalman Filter

{:.post-source}
[GitHub](https://github.com/denniskb/hy475/tree/master/assign1_kalman)

This repository contains a short intro to the Kalman filter, together with a link to an interactive robot simulator that you will use to implement your solution to the filter. This assignment is a part of [HY475](https://www.csd.uoc.gr/~hy475/) Robotic Navigation course at the Univeristy of Crete. I wish I still had some ECTS points to earn!

----

{:.post-entry-title}
#### Researchers build a swimming robot that works in the Mariana Trench

{:.post-source}
[Ars Technica](https://arstechnica.com/science/2021/03/researchers-build-a-swimming-robot-that-works-in-the-mariana-trench/)

Researchers have built a swimming soft robot with potential use for deep-sea exploration. The robot was successfully deployed at the depth of 3,224m, experiencing about 324 bars of pressure. The robot's fins are actuated with an on-board AC voltage of 8kV at 1Hz. At 10 km depth the robot was not released for a free-swim but it proved that it can overcome the pressure and still move its fins. If you would like to see all tests of this robot then check out [this video from Nature](https://youtu.be/shr6sJy_29E).

----

{:.post-entry-title}
#### Drones vs hungry moths: Dutch use hi-tech to protect crops

{:.post-source}
[The Associated Press](https://apnews.com/article/world-news-netherlands-3fb76e95fefbe0f9a160f330f3c4a075)

Big thanks to Edward for sharing this link on [WR Patrons Slack](https://www.patreon.com/WeeklyRobotics). The idea of flying a drone into insects to instantly 'pulverize it' sounds like an interesting alternative to using chemicals. Before jumping on-board I would have some questions on the technical feasibility of a palm-sized drones being able to survey big areas while being able to track a single type of insect and plan a colliding trajectory with it. I will be monitoring [PATS Drones](https://pats-drones.com/) development and looking forward to real-life implementations.

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
                <h4 class="post-entry-title">The Prepared</h4>
                <span class="sponsor-source">
                    <a href="https://theprepared.org/newsletter">theprepared.org</a>
                </span>
                <p class="sponsor-blurb">The Prepared is one of my own favorite newsletters, covering manufacturing, engineering, and infrastructure. In <a href="https://mailchi.mp/theprepared/the-prepared-xkejz25dve">this week's issue</a>, there's a rundown of two interesting metal 3D printing startups - both of which use some pretty unique tech. <a href="https://theprepared.org/newsletter">Subscribe here - it's great</a>!</p>
            </div>
        </div>
    </div>
</div>
----

### Announcements

{:.post-entry-title}
#### WR Community Meeting #3

{:.post-source}
[Eventbrite](https://www.eventbrite.co.uk/e/weekly-robotics-community-meeting-3-speaker-tbd-tickets-144981865663)

The presentation slot for this meetup is still up for grabs, so if you have something cool to showcase then please [get in touch](mailto:mat@weeklyrobotics.com)!

----

{:.post-entry-title}
#### Apply now for the 2021 Reddit Robotics Showcase and share your robotics with the world!

{:.post-source}
[/r/robotics](https://www.reddit.com/r/robotics/comments/laceed/apply_now_for_the_2021_reddit_robotics_showcase/)

Until 30th of April you can apply to present your robots to the /r/robotics community. Looking forward to seeing all the featured robots!

----
