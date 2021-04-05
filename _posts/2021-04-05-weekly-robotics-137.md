---
title: "Weekly Robotics"
description: "This week in WR: Ingenuity test coming up later this week, sheet metal forming with industrial robots, cornhole winning robot, shape-shifting quadruped and more!"
date: 2021-04-05
tags: [Robotics, Quadrupeds, Research, IndustrialRobots, SLAM, Space, Rovers, Drones, Sensors]
idx: 137
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: NASA/JPL*

> You know this feeling when you have a newsletter called "Weekly Robotics" and as a part of it, you start having these community meetings called "Weekly Robotics Community Meetings" that you organize bi-weekly? Well, I know this feeling. Or I did know this feeling because as of this week Weekly Robotics meetups are a weekly thing! The time is the same as previously (7 PM CEST) every Thursday. This week I'm excited for Darko's presentation about Webots, a feature-rich robotics simulator. As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). The most clicked link last week was [the Robotics 101 course](https://github.com/michiganrobotics/rob101) with 18.5% opens.

----
<div class="sponsor-snippet-wrapper">
    <div class="sponsor-snippet container-fluid">
        <div class="row">
            <div class="col-3 d-none d-sm-block"></div>
                <div class="col-sm-12 col-md-6 nopadding">
                    <h3 id="spoonsored">Sponsored</h3>
                <h4 class="post-entry-title">Plug&Play RTK with Septentrio mosaic-X5 dev kit</h4>
                <span class="sponsor-source">
                    <a href="https://msadowski.github.io/rtk-plug-n-play-with-septentrio/">msadowski.github.io</a>
                </span>
                <p class="sponsor-blurb">Recently I had a chance to do some ROS integration of <a href="https://www.septentrio.com/en">Septentrio's</a> mosaic-X5 development kit running two modules in an RTK setup and getting some really good results. If you are looking into integrating some GNSS modules on your robots the post might have some useful hints on how to approach this.</p>
            </div>
        </div>
    </div>
</div>
----

{:.post-entry-title}
#### NASA's Mars helicopter Ingenuity touches down on the Red Planet

{:.post-source}
[space.com](https://www.space.com/mars-helicopter-ingenuity-touches-down-martian-surface)

Ingenuity was safely deployed by Perseverance and should be ready for flight on the 11th of April. I hope to update you on how the first flight went in the next issue of this newsletter! There is a relevant [xkcd](https://xkcd.com/2444/) for the flight event.

----

{:.post-entry-title}
#### The shaping of things to come

{:.post-source}
[Nissan](https://global.nissannews.com/en/releases/release-6376ec37a1b56f1d78027f204b026c13-191126-00-e)

Nissan is rethinking sheet-metal forming but instead of investing in dies, they use two industrial robot arms with specially designed tooltips that work on the piece from both sides of the sheet. The idea is to use this approach for low volume production of parts that might have been discontinued. I highly recommend watching the featured video in 4k and closed captions enabled. This is some pretty solid engineering!

----

{:.post-entry-title}
#### Cheat At Cornhole With A Bazillion-Dollar Robot

{:.post-source}
[Hackaday](https://hackaday.com/2021/04/04/cheat-at-cornhole-with-a-bazillion-dollar-robot/)

Since we are already looking at Kuka's industrial arms - check out this article and video of a robot that solves winning a cornhole game. The first thing I liked about the video is that the robot is not only developed to play a game, it was used for the manufacturing of the cornhole itself. I appreciate the authors creating a [public repo](https://github.com/davesarmoury/Cornhole/blob/master/Cornhole.py) for the project 161 lines of Python the code is quite easy to go through.

----

{:.post-entry-title}
#### voxgraph

{:.post-source}
[GitHub](https://github.com/ethz-asl/voxgraph)

"Voxgraph is a globally consistent volumetric mapping framework. It represents the world as a collection of Signed Distance Function submaps, which it aligns through pose graph optimization". I highly recommend checking out the [video](https://youtu.be/N9p1_Fkxxro) or the [preprint](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/385682/Voxgraph-ETHpreprintversion.pdf) on this framework. I have to say the results look really good!

----

{:.post-entry-title}
#### Homemade Sherp Style 4 Wheel Drive Robot Chassis

{:.post-source}
[YouTube (Engineering After Hours)](https://youtu.be/63go-gQNn5o)

Engineering After Hours had built an RC controlled skid steer mobile robot that really can take a beating and seems relatively waterproofed. I think it would make an interesting development platform for mobile robots, especially if it can be made low cost.

----

{:.post-entry-title}
#### This Shape-Shifting Robot Can Rearrange Its Body to Walk in New Environments

{:.post-source}
[Singularity Hub](https://singularityhub.com/2021/03/25/this-shape-shifting-robot-can-rearrange-its-body-to-walk-in-new-environments/)

DyRET is a quadruped robot with each of the four legs having two telescopic sections, that allow it to change leg length and adapt to the environment it's in.

----

{:.post-entry-title}
#### BrMechanic's robotic hand

{:.post-source}
[/r/robotics](https://www.reddit.com/r/robotics/comments/mjdny6/hello_everybody_this_is_the_first_demo_of_a/)

Reddit's user BrMechanic had shared the robotic hand he has been working on that has a haptic interface and works very well, especially given that the author had used hobby-grade components.

----

{:.post-entry-title}
#### Publication of the Week - The Marathon 2: A Navigation System (2020)

{:.post-source}
[papercept.net](https://ras.papercept.net/proceedings/IROS20/0704.pdf)

One of the most important packages of ROS had a huge upgrade when it comes to ROS2. Navigation2 features modern highly modular methods that took into account security and performance aspects that lacked in ROS. This paper describes all the new features of Navigation2 that apply to a large variety of robot types such as holonomic and non-holonomic including ackermann and legged robots. All of the work is open-source and contains a rich set of instructions and support for future work by the community.

----

### Announcements

{:.post-entry-title}
#### Weekly Robotics Community Meeting #5 - Webots with Darko Lukić

{:.post-source}
[Eventbrite](https://www.eventbrite.co.uk/e/weekly-robotics-community-meeting-5-webots-with-darko-lukic-tickets-149507417711)

In the presentation, we will give an introduction to the [Webots](https://cyberbotics.com/) open-source robot simulator. We will focus on Webots advantages, tips, and useful resources. In addition, we will present the current state of the web integration and the ROS 2 interface.
