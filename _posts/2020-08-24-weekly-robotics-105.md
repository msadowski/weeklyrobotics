---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: open source robotic fingers, a state machine library for ROS, robots in SONY's PS4 assembly, Open Problems in Robotics and more!"
date: 2020-08-24
tags: [Robotics, Careers, Drones, SoftRobots, MicroRobots, Manipulators, IndustrialRobots, ROS]
idx: 105
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [TriFinger](https://sites.google.com/view/trifinger)*

> Yesterday I started a [patreon page](https://www.patreon.com/WeeklyRobotics) for Weekly Robotics. The reason for it is I want to take this project to the next level, but I won't be able to dedicate enough time for it without significantly affecting my day job. Your support will be highly appreciated! One thing I want to stress is that this newsletter is never going to get paywalled, so even if you can't support it you will keep access to all the issues. Thanks a lot for enjoying this project!!!

> The most clicked last week was [Project Wilson](https://projectwilson2020.wixsite.com/mysite) with 10.2% opens. The second one was the video showing [EGO-Planner](https://youtu.be/UKoaGW7t7Dk). As promised in the previous issue, here is the link to the [preprint](https://arxiv.org/abs/2008.08835) of the paper describing this planner. You can find the project repository on [GitHub](https://github.com/ZJU-FAST-Lab/ego-planner).

{:.post-entry-title}
#### TriFinger: An Open-Source Robot for Learning Dexterity

{:.post-source}
[TriFinger](https://sites.google.com/view/trifinger)

Remember [Solo](https://open-dynamic-robot-initiative.github.io/), an open source quadruped robot, from [issue #97](https://weeklyrobotics.com/weekly-robotics-97)? Turns out that with minimum modifications the quadruped leg can be made into a robotic finger. Multiply this by three and your TriFinger is ready for object manipulation. Each of the 3 finger modules weighs 930g. The Python and C++ interfaces allow control at up to 1kHz. You can find the instructions on building the modules in the [project repository](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/mechanics/tri_finger_edu_v1/README.md). If you like what you are seeing then check out the [paper describing the project](https://arxiv.org/abs/2008.03596).

----

{:.post-entry-title}
#### SMACC

{:.post-source}
[GitHub](https://github.com/reelrbtx/SMACC/)

"SMACC is an event-driven, asynchronous, behavioral state machine library for real-time ROS (Robotic Operating System) applications written in C++, designed to allow programmers to build robot control applications for multicomponent robots, in an intuitive and systematic manner". For project videos and a follow-up discussion check out [this ROS Discourse announcement](https://discourse.ros.org/t/introducing-the-smacc-state-machine-library) and [this post on MoveIt integration](https://discourse.ros.org/t/introducing-the-smacc-movegroupinterface-client-a-new-way-to-program-with-moveit). The project has now been added to the [Awesome-Weekly-Robotics list](https://github.com/msadowski/awesome-weekly-robotics).


----

{:.post-entry-title}
#### Playstation Backstage

{:.post-source}
[Nikkei Asian Review](https://vdata.nikkei.com/en/newsgraphics/sony-playstation/)

This article full of amazing high-res photos shows some behind the scenes of how Playstation 4 automatic assembly lines look like. My biggest surprise: the robots manipulate cables, including flat ribbon cables(!) and I get an impression they don't have any issues fitting the cables in the connectors. How difficult is that on an industrial scale?!

----

{:.post-entry-title}
####  Open Problems in Robotics

{:.post-source}
[Locklin on science](https://scottlocklin.wordpress.com/2020/07/29/open-problems-in-robotics/)

A very nice and concise write up on open problems in Robotics. If you are reading this newsletter chances are you are well aware of all of these issues, or maybe you are actively solving some of them. [The compilation of robots falling down](https://youtu.be/g0TaYhjpOfo) at DARPA Robotics Challenge made my day!

----

{:.post-entry-title}
#### A Collaborative Robotic Approach to Autonomous Pallet Jack Transportation and Positioning

{:.post-source}
[YouTube ( Human Robot Interfaces and physical Interaction)](https://youtu.be/HzruNzmwaHo)

Having an omnidirectional mobile robot pull a pallet jack sounds like a tough problem (pay attention to the wheel skid in the video). MOCA is a robot platform developed by researchers at IIT for pallet positioning. For more details about the implementation, you can check out [this open IEEE paper](https://ieeexplore.ieee.org/document/9153757).

----

{:.post-entry-title}
#### Deep Drone Acrobatics (RSS 2020)

{:.post-source}
[YouTube](https://youtu.be/2N_wKXQ6MXA)

Davide Scaramuzza's team is at it again, this time teaching a multirotors aggressive acrobatics in simulation and transferring the policies to a real drone and executing them using onboard sensors only.

----

{:.post-entry-title}
#### Watch a Tiny Robot Powered by Alcohol

{:.post-source}
[Science Mag](https://www.sciencemag.org/news/2020/08/watch-tiny-robot-powered-alcohol)

Scientists had developed an 88mg robot beetle burning methanol to cause the robot's legs to shorten, driving the robot movement. 95 milligrams of fuel could power the robot for up to two hours. For more details about this research check out [this paper](https://robotics.sciencemag.org/content/5/45/eaba0015).

<br>
<div class="sponsor-snippet-wrapper">
    <div class="sponsor-snippet container-fluid">
        <div class="row">
            <div class="col-3 d-none d-sm-block"></div>
                <div class="col-sm-12 col-md-6 nopadding">
                    <h3 id="spoonsored">Sponsored</h3>

                <p class="sponsor-blurb">Huge thanks to all of the Weekly Robotics <a href="https://weeklyrobotics.com/supporters">supporters</a> helping this project through <a href="https://www.patreon.com/WeeklyRobotics">Patreon</a> and the following business partners:</p>

                <div class="row">
                    <div class="col"><a href="http://msadowski.ch/"><img src="img/sponsors/m_consulting.png" alt="M. Sadowski Consulting"></a></div>
                </div>
            </div>
        </div>
    </div>
</div>

### Robotics Workshops

Would you like to share your workplace with the Weekly Robotics community? If yes then this is the place! Feel free to send me your submission [via e-mail](mailto:mat@weeklyrobotics.com) with pictures and a short description.

---

Leading by example here is [my](https://www.linkedin.com/in/mateuszsadowski/) working place for the times of Pandemic:

> Here is the office I've been sharing with my partner. From the left, you can see [Blue Owl FPV](https://www.youtube.com/channel/UCjr3hpadMQEaC9ksaxxVGYw) desk with all the racing multirotors and a soldering station. In between our desks, you will see some ammo boxes - perfect for storing LiPo batteries after [removing the seals](https://youtu.be/CnNId0mDnBo). The 3D printer in the right side of the image is AnyCubic I3 Mega, and just next to it - a fire extinguisher (because as you know - safety first).

<div class="wr-row">
    <img src="/img/workshops/105/1.jpg" alt="Mat's desk" style="width:100%">
</div>

### Job Seekers

[In the issue #83](https://weeklyrobotics.com/weekly-robotics-83) I've started this section to try to help out those looking for work in the times of pandemic. If you are currently looking for work then feel free to [send me](mailto:mat@weeklyrobotics.com) your details in the same format as you can see in the entries below.

**Name**: Muhammad Rehan<br>
**Location**: Orlando, FL, USA. Willing to relocate<br>
**Skills**: C/C++, Python, MATLAB, ROS, Ubuntu<br>
**Profile**: I am actively looking for Robotics Engineer position. I received PhD in Engineering Physics from Embry Riddle Aeronautical University USA (with major in robotics, systems & control). I have more than twelve years of industrial experience. My research interests include learning based control, multi-robot systems path planning and SLAM (Simultaneous Localization and Mapping)<br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/muhammad-rehan-phd-7676ab5a/) <br>
**Email**: engr.mrehan@gmail.com<br>

----

**Name**: Seth King<br>
**Location**: Central Virginia,  USA (Remote primary focus)<br>
**Skills**:  C, C++(11,14), Python, , Linux, Yocto, ROS, ROS2<br>
**Profile**: Embedded software engineer with 15 plus years of experience in Unix/Linux OS. I love building robots so much that during my Master's(CS 2018) I searched the organization for a professor to guide me through a special project. I found a professor overseas at a satellite campus and we spent the whole summer building an outdoor rover.  I enjoy working on robots and enjoy working with people who work on robots<br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/nerdking/), [GitHub](https://github.com/Neuromancer2701), [Side Project](https://openrover.com/#open)<br>
**Email**: king.seth@gmail.com<br>

----

### Careers

{:.post-entry-title}
#### Robosynthesis (Twyford, UK)

{:.post-source}
[Electronics Engineer](https://www.robosynthesis.com/post/electronics-engineers-jobs-in-robotics-come-join-us)

Robosynthesis​ is a ​modular​ industrial ​robotics platform​ that’s reconfigurable in-the-field to perform a wide range of missions using a variety of sensors and tools, different physical configurations, and various terrain-optimised traction systems. Our platforms have been used at ​CERN​ in the ​LHC​, at the ​National Physical Laboratory​, inside gas pressure vessels, and even in chicken sheds(!).

----

### Announcements

Did you miss any of the events announced in [Weekly Robotics #103](https://weeklyrobotics.com/weekly-robotics-103)? If yes then you can find the recordings from AWS Cloud Robotics Summit 2020 on [YouTube](https://www.youtube.com/playlist?list=PL5bUlblGfe0LLnVO0PLxkqIE5953uC9GT). When it comes to NuttX workshop YouTube has the recordings for [day 1](https://youtu.be/t49wq_ovT50) and [day 2](https://youtu.be/CIpa3_70PCY) - check out the pinned comment for presentation timestamps. Huge thanks to [Alan Carvalho de Assis](https://www.linkedin.com/in/acassis/) for keeping me up to date on NuttX events!
