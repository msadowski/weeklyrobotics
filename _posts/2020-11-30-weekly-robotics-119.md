---
title: "Weekly Robotics"
description: "Weekly Robotics 119: Wireless charging of lunar robotics, AI incident database, a new SLAM library, Spot in nuclear decommissioning, Cybathlon highlights and more!"
date: 2020-11-30
tags: [Robotics, Space, Bionics, SLAM, DIY, OpenSource]
idx: 119
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Astrobotic](https://www.astrobotic.com/)*

> Welcome to yet another issue of Weekly Robotics. I finally had time to finish the [Makani documentary](https://youtu.be/qd_hEja6bzE), and my verdict is: it's amazing! I've liked it so much I've added a documentaries section to the [awesome-weekly-robotics](https://github.com/msadowski/awesome-weekly-robotics). Do you know of any other documentaries I should include there? [Let me know!](mailto:mat@weeklyrobotics.com). This week we have a guest contribution to the publication fo the week by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). Thanks! The most clicked link last week was [the robotics simulation in Unity](https://blogs.unity3d.com/2020/11/19/robotics-simulation-in-unity-is-as-easy-as-1-2-3/) with 12.0% opens.

{:.post-entry-title}
#### NASA Initiative Developing Wireless Charging for Lunar Robots

{:.post-source}
[The Robot Report](https://www.therobotreport.com/nasa-initiative-developing-wireless-charging-lunar-robots/)

In 2001 NASA will be testing small lunar rovers (roughly the size of the shoe box) on the Moon's surface. If you would like to get more technical details on this project then you can check out the [Cuberover Payload User Guide](https://www.astrobotic.com/cuberover-payload-user-guide).

----

{:.post-entry-title}
#### gradslam

{:.post-source}
[gradslam.github.io](https://gradslam.github.io/)

gradslam is an open-source framework providing differentiable building blocks for simultaneous localization and mapping (SLAM) systems. We enable the usage of dense SLAM subsystems from the comfort of PyTorch.

----

{:.post-entry-title}
#### AI Incident Database

{:.post-source}
[incidentdatabase.ai](https://incidentdatabase.ai/summaries/incidents)

A neat database of AI incidents ranging from AI discriminating group of people to [robots releasing bear spray](https://eu.app.com/story/money/business/main-street/2018/12/05/bear-spray-incident-nj-amazon-warehouse-shines-light-safety-record/2215515002/) and self driving cars crashing into things.

----

{:.post-entry-title}
#### Boston Dynamics' Spot Is Helping Chernobyl Move Towards Safe Decommissioning

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/boston-dynamics-spot-chernobyl)

I've linked to the video of Spot in Chernobyl in the last week's issue but seeing the information in this article I thought it would be worth expanding on the topic. According to the article, the best thing about using legged robots in such environments is that their locomotion doesn’t disturb the radioactive dust on the floor as much a wheeled robot or a drone would.

Another interesting information contained in the article is on how little testing has been done on robots failing under radiation, an example provided is a KUKA LBR800 robot arm that "stopped operating after a large radiation dose of 164.55(±1.09) Gy to its end effector, and the component causing the failure was an optical encoder". For reference 1-2 Gy dose to a whole body for a human causes radiation sickness and possible death, while 8Gy "is usually just straight-up death". If you would like to know more about Spot in Chernobyl then check out [this RACE webinar](https://youtu.be/CyK5hYoeoDI) by Guy Burroughes.

----

{:.post-entry-title}
#### DIY Camera Motion Rig Is Mostly 3D Printed

{:.post-source}
[Hackaday](https://hackaday.com/2020/11/24/diy-camera-motion-rig-is-mostly-3d-printed/)

Here is a 6-axis camera motion rig by Do It Whenever? that you can control using GCODE. Could it be an open alternative to the [Bolt cinematic robot](https://www.mrmoco.com/motion-control/bolt/#bolt-videos) that was featured in the [Weekly Robotics #25](https://weeklyrobotics.com/weekly-robotics-25)?

----

{:.post-entry-title}
#### Highlights of the CYBATHLON 2020 Global Edition

{:.post-source}
[YouTube (Cybathlon)](https://youtu.be/owMz11C1-mc)

Cybathlon 2020, a competition in which people with physical disabilites compete by solving everyday tasks using assistive technologies, too place earlies this month. The video above is a highlight of the competition but you can find full streams and some extra videos on the [Cybathlon channel](https://www.youtube.com/channel/UCqGx-eUykZLDKjjrwRhfilQ/videos).

----

{:.post-entry-title}
#### Publication of the Week - Real-Time Multi-SLAM System for Agent Localization and 3D Mapping in Dynamic Scenarios (2020)(PDF)

{:.post-source}
[hal.inria.fr](https://hal.inria.fr/hal-02913098/document)

In fire scenarios, the major challenge is the different complex scenarios such as dark environments, smoked rooms, high temperatures, and lots of light sources. Considered a hard task for humans and even more for robots. This paper proposes a way to use different sensors (Camera, LiDAR, IMU and GPS) to compensate for each environment challenge and help firefighters gather more information about the building, such as structural weak points, heat sources, and many other that can increase the chances of saving lives.

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
