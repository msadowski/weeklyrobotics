---
title: "Weekly Robotics"
description: "This week in WR: Stretch - a NEW robot from Boston Dynamics, Open-source drone gesture control, micro-ROS on Raspberry Pi Pico, free robotics algebra course and more!"
date: 2021-03-29
tags: [Robotics, DIY, OpenSource, Research, Drones, MobileRobots, Meetups]
idx: 136
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [CBS News](https://www.cbsnews.com/news/boston-dynamics-robots-humans-animals-60-minutes-2021-03-28/)*

> This week we are having a Weekly Robotics meetup! This time I will do an AMA on working as an independent robotics consultant, so get your questions ready! You will find more information about the event in the last entry in this newsletter. As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). Last week’s most clicked link was [the electrical engineering study plan](https://i-kh.net/2021/03/20/electrical-engineering-study-plan/) with 22.9% opens.

{:.post-entry-title}
#### Boston Dynamics: Inside the workshop where robots of the future are being built

{:.post-source}
[CBS News](https://www.cbsnews.com/news/boston-dynamics-robots-humans-animals-60-minutes-2021-03-28/)

Here is a short coverage of Boston Dynamics from CBS 60 minutes. Biggest reveal? Stretch, a new robot by BD that looks like a heavy AGV with a hefty arm attached to it and a reported battery life of 16 hours. You can see it around the 11:30 timestamp of the video. Cool stuff!

----

{:.post-entry-title}
#### Gesture controlled drone - DIY Motion Controller

{:.post-source}
[YouTube (Paweł Spychalski)](https://youtu.be/1e1Dzy56vOk)

Paweł Spychalski had created a one-handed controller for UAVs that conceptually looks very similar to a controller done by [MotionPilot](https://motionpilot.ch/) and recently [DJI](https://dronedj.com/2021/03/10/djis-motion-controller-for-its-fpv-drone-is-intuitive-to-a-point/). In Paweł's design, he uses an ESP32 with MPU6050 IMU, sending control data directly to a trainer port on his OpenTx radio. You will find the project repository on [GitHub](https://github.com/DzikuVx/DiyMotionController).

----

{:.post-entry-title}
#### Getting started with micro-ROS on the Raspberry Pi Pico

{:.post-source}
[Ubuntu](https://ubuntu.com/blog/getting-started-with-micro-ros-on-raspberry-pi-pico)

Like the idea of using ROS2 on microcontrollers? Then you should check out [micro-ROS](https://micro.ros.org/) project. This tutorial can be a good first introduction.

----

{:.post-entry-title}
#### Shadow Teleoperation System Plays Jenga

{:.post-source}
[YouTube (The Shadow Robot Company)](https://youtu.be/7K9brH27jvM)

A neat presentation from Shadow showing a human teleoperating two UR robot arms playing Jenga. I was surprised how accurately can this system track hand movements and how small the latency seems to be.

----

{:.post-entry-title}
#### Robotics 101: Computational Linear Algebra

{:.post-source}
[GitHub](https://github.com/michiganrobotics/rob101)

"Computational Linear Algebra is a pilot first-semester, first-year undergraduate course that shows how mathematics and computation are unified for reasoning about data and making discoveries about the world". In the repository, you will find links to the free textbook, videos and lectures.

----

{:.post-entry-title}
#### Functgraph: Personal Factory Automation With a 3D Printer

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/industrial-robots/functgraph-personal-factory-automation-with-a-3d-printer)

Researchers from Meiji University had modified a 3D printer to act as a mini-factory, being able to design various functional systems such as T-shirt folding and even sandwich making.

----

{:.post-entry-title}
#### Publication of the Week - Development of A Passive Skid for Multicopter Landing on Rough Terrain (2021) (PDF)

{:.post-source}
[Papercept](https://ras.papercept.net/proceedings/IROS20/0479.pdf)

With the advent of multiple drone utilities such as express shipping and delivery, safety inspections, search and rescue operations and many more that sometimes require landing on rough terrain. This paper proposes a device that features one passive joint with two points of contact and a third contact connected to an arm with two servos joints. One of the benefits of this system is to maintain the drone plane levelled regardless of the terrain angle. I wish I had one of those in my drone when I was first trying to fly it.

----

### Announcements

{:.post-entry-title}
#### WR Community Meeting #4 - AMA with Mat

{:.post-source}
[Eventbrite](https://www.eventbrite.co.uk/e/weekly-robotics-community-meeting-4-robotics-consulting-ama-with-mat-tickets-148503621329)

Our next community meeting is up this week at 7 PM CEST! This time Mat will answer any questions you might have on going solo and working as a robotics consultant/freelancer. We will give AMA (Ask Me Anything) format a shot - if you have any questions related to this newsletter then I'll be more than happy to answer them as well. If you would like to present your robotics-related projects or ideas in one of the meetings or know someone interested, please [let me know](mailto:mat@weeklyrobotics.com)!
