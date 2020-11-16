---
title: "Weekly Robotics"
description: "WR 117: a bionic tail, open-source quadruped update, machine-learned models for autonomous cars, a multirotor with tensegrity shell and more!"
date: 2020-11-16
tags: [Robotics, Bionics, quadrupeds, autonomouscars, drones, space]
idx: 117
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Embodied Media Project](http://embodiedmedia.org/project/arque/)*

> On Thursday last week ROS World 2020 took place. I've really enjoyed the presentations. A small boast: my presentation on Weekly Robotics was featured in the[Lightning Talks](https://vimeo.com/478574166) at around 2:00. If you enjoy lightning talks then you should also check out [RoboTrainer](https://twitter.com/OpenRoboticsOrg/status/1321527779234443265) by Denis, one of our readers. Similarly to last week, the publication of the week in this issue was prepared by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). Huge thanks! The most clicked link last week was [the building with robot legs](https://hackaday.com/2020/11/04/building-walks-with-robot-legs/) with 12.7% opens.

{:.post-entry-title}
#### Arque Is an Artificial Tail for Enhancing Humans

{:.post-source}
[The New Stack](https://thenewstack.io/arque-is-an-artificial-tail-for-enhancing-humans/)

Last month I had a random thought: "would it be possible to create a bionic tail that could aid balancing in humans". With quite a bit of research, I came across Arque - a pneumatically driven, seahorse inspired,  tail that can help you find the balance, or it can be used for haptic feedback in VR games. You can find a short paper describing this work on [ResearchGate](https://www.researchgate.net/publication/334689139_Arque_artificial_biomimicry-inspired_tail_for_extending_innate_body_functions). The paper links to an interesting project from 2012: [shippo](http://neurowear.com/projects_detail/shippo.html) - a robotic tail wagging based on user mood. Unfortunately, the project's [kickstarter](https://www.kickstarter.com/projects/shota/tailly-the-tail-that-wags-when-you-get-excited) didn't secure enough funding - probably because it was too ahead of its times.

----

{:.post-entry-title}
#### mjbots November 2020 Update

{:.post-source}
[jpieper.com](https://jpieper.com/2020/11/09/mjbots-november-2020-update/)

I've been following Josh Pieper's work ever since I've featured Quad A0 in the [issue #59](https://weeklyrobotics.com/weekly-robotics-59). This blog post features a summary of what Josh has been up to. I have to say I'm really intrigued by the Moteus Controllers and might test them in a near future.

----

{:.post-entry-title}
#### Autoware Model Zoo

{:.post-source}
[GitHub](https://github.com/autowarefoundation/modelzoo)

[Autoware](https://www.autoware.org/) had released a collection of machine-learned models for use in autonomous driving applications. Right now the repo has perception models: camera_obstacle_detection and lidar_obstacle_detection.

----

{:.post-entry-title}
#### HMI - Aquanaut 2020 - Galveston Bay

{:.post-source}
[YouTube (Houston Mechatronics, Inc)](https://youtu.be/k2JjIKBAfv0)

Remember [the Aquanaut](https://spectrum.ieee.org/robotics/humanoids/meet-aquanaut-the-underwater-transformer) from [WR #50](https://weeklyrobotics.com/weekly-robotics-50)? From the video, it looks like it is quite capable. Cool stuff!

----

{:.post-entry-title}
#### Quadcopter With Tensegrity Shell Takes A Beating And Gets Back Up

{:.post-source}
[Hackaday](https://hackaday.com/2020/11/05/quadcopter-with-tensegrity-shell-takes-a-beating-and-gets-back-up/)

Using an icosahedron tensegrity structure as a safety cage for multirotor sounds like an innovative idea, especially if it can crash into obstacles at 6.5m/s and it is able to '[turtle mode](https://brushlesswhoop.com/flip-over-after-crash/)' its way upright after falling. You can find this project's research paper on [ArXiv](https://arxiv.org/abs/2003.03417).

----

{:.post-entry-title}
#### Preparing to Land Perseverance

{:.post-source}
[YouTube (NASA JPL)](https://youtu.be/v7iUb_wDHxk)

"To prepare the Perseverance rover for its date with Mars, NASA’s Mars 2020 mission team conducted a wide array of tests to help ensure a successful entry, descent and landing at the Red Planet. From parachute verification in the world’s largest wind tunnel, to hazard avoidance practice in Death Valley, California, to wheel drop testing at NASA’s Jet Propulsion Laboratory and much more, every system was put through its paces to get ready for the big day."

----

{:.post-entry-title}
#### Publication of the Week - Unsupervised Domain Adaptation for Transferring Plant Classification Systems to New Field Environments, Crops, and Robots (2020)

{:.post-source}
[ResearchGate](https://www.researchgate.net/publication/344100796_Unsupervised_Domain_Adaptation_for_Transferring_Plant_Classification_Systems_to_New_Field_Environments_Crops_and_Robots)

Identifying crops and weeds in different terrains using different robots is a real-world challenge that requires a lot of tunning and data labelling. This paper proposes a solution to transfer the "visual style" of previous labelled images to completely new terrain images to maintain the accuracy of the classifier, hence reducing considerably retraining work. This can be considered a huge step towards fully autonomous robots in agriculture.

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
