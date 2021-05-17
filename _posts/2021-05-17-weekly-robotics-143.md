---
title: "Weekly Robotics"
description: "Weekly Robotics #143: robots doing things (including skiing), various 3D printed mechanical components taking a beating, a collab notebook for landing a SpaceX rocket, Waymo autonomous taxi getting confused and more!"
date: 2021-05-17
tags: [Robotics, AutonomousCars, MobileRobots, Space, ROS]
idx: 143
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> Let's start this week's issue slowly, by watching some quality pictures of robots doing things, and then let's keep up building momentum until [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/) introduces you to a collaborative visual SLAM, followed by a look at our latest meetup recording. This week there is no WR Meetup but we will return next week! The most clicked link last week was [The best projects from 10 years of Applied Science](https://youtu.be/rLkVFjRyoDU) with 15.8% opens.

----
<div class="sponsor-snippet-wrapper">
    <div class="sponsor-snippet container-fluid">
        <div class="row">
            <div class="col-3 d-none d-sm-block"></div>
                <div class="col-sm-12 col-md-6 nopadding">
                    <h3 id="spoonsored">Sponsored</h3>

                <h4 class="post-entry-title">Webinar - Bridging ROS and GNSS for robotics applications</h4>
                <span class="sponsor-source">
                    <a href="https://bit.ly/3teqJuh">Septentrio</a>
                </span>
                <p class="sponsor-blurb">On June 3rd I will be presenting in this free webinar by Septentrio, premiering my 3D mapping RTK based prototype and providing insights on GNSS integration in ROS. See you there!</p>
            </div>
        </div>
    </div>
</div>
----

{:.post-entry-title}
#### Robots Are Everywhere

{:.post-source}
[The Atlantic](https://www.theatlantic.com/photo/2021/05/photos-robots-are-everywhere/618823/)

A series of 30 photographs showing robots in various situations. As I mentioned in the intro browsing through these can be a good start to your week!

----

{:.post-entry-title}
#### 3D Print all the things with Hacakday

Hacakaday had quite a few interesting article/videos with some 3D printed designs by [Let's Print](https://www.youtube.com/channel/UCLn_0VPipeMkLqo5tW6FP0A) lately. The first one I came across is [this 3D printed chain](https://hackaday.com/2021/05/15/putting-3d-printed-chain-through-its-paces/). In the video, the author is using three types of materials to print his design and performs some impact tests on them. The next one is [testing 3D printed worm gears](https://hackaday.com/2021/05/12/testing-3d-printed-worm-gears/), again using three types of materials and stress testing them. Finally, there is [this stackable planetary gearbox](https://hackaday.com/2021/05/14/a-stackable-planetary-gearbox-you-can-print-at-home/), that can lift some seriously heavy things.

----

{:.post-entry-title}
#### How SpaceX lands Starship (sort of)

{:.post-source}
[thomas-godden.medium.com](https://thomas-godden.medium.com/how-spacex-lands-starship-sort-of-ee96cdde650b)

Thomas Godden has been looking into trajectory optimization and came up with this blog post, in which he shows how he applied it to 'land' a 2D Starship model with some nice simulations created in matplotlib. All the code developed by Thomas is accessible in [this notebook](https://colab.research.google.com/drive/18MVtu4reVJLBE1RXByQEmu0O9aLXlMHz?usp=sharing).

----

{:.post-entry-title}
#### How Ingenuity Knows Where It Is And Where It's Going

{:.post-source}
[PickNik](https://picknik.ai/slam/localization/state%20estimation/mars%20helicopter/2021/05/10/Ingenuity.html)

Here is a nice and short write up by John Stechschulte on how Ingenuity does state estimation. If you would like to learn more about the Ingenuity Software stack then a good starting point could be [this F' architecture document](https://github.com/nasa/fprime/blob/devel/docs/Architecture/FPrimeSoftwareArchitecture.pdf).

----

{:.post-entry-title}
#### Confused Waymo robotaxi shows challenges of scaling AVs

{:.post-source}
[The Robot Report](https://www.therobotreport.com/confused-waymo-robotaxi-shows-challenges-of-scaling-avs/)

[JJRicks Studios](https://www.youtube.com/channel/UCpUqV-RsACKUSw2oG3Ybqtg) happened to be in a Waymo car when it got quite confused about traffic cones on the road. The full video of the ride is featured in the article, with the car being stuck occurring around the 11 minute mark. I find it quite funny how the car tries to run away from the Waymo assistance.

----

{:.post-entry-title}
#### Publication of the Week - A Collaborative Visual SLAM Framework for Service Robots (2021)

{:.post-source}
[arXiv](https://arxiv.org/abs/2102.03228)

Lately, an increasing number of service robots are being used for many tasks in hospitals, malls, hotels, restaurants, and many other places that might require multiple robots to operate under the same building. This paper proposes a framework so each robot can register to a prior existing map to perform mapping and localization tasks. Not only that, but each one of the robots can update the map using visual feature-based algorithms from monocular, stereo, and RGB-D cameras. All of this is done in real-time given the proposed efficient communication pipeline used.

----

### Announcements

{:.post-entry-title}
#### Previous Meeting #10 - Perception for autonomous cars with Roland Meertens

{:.post-source}
[YouTube (WeeklyRobotics)](https://youtu.be/X23bYTQr3Gg)

Last Roland gave a very interesting presentation on perception and autonomous cars. There were lots of interesting insights on safety in the industry and a captivating brainstorm mid talk. Loved it!
