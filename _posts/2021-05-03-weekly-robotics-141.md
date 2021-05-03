---
title: "Weekly Robotics"
description: "This week in Weekly Robotics Newsletter: DeepRacer goes open-source, farming robots killing weeds with lasers, robots winding interesting structures, R/C proximity flying fixed-wing and more!"
date: 2021-05-03
tags: [Robotics, drones, space, electronics, open-source, agriculturalRobots]
idx: 141
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> Lately I've been, again, thinking about the 80/20 rule and how it applies to hardware. More specifically I've started playing with the idea of using a precise positioning system with a LiDAR to create a hand-held mapping system ([LinkedIn teaser for the curious](https://www.linkedin.com/posts/mateuszsadowski_robotics-ros-sensors-activity-6794720261234049025-Uj1C)). Since I don't have plans to productise it in any way (at least not yet), it's quite straightforward - put some hardware together, glue it with software (thanks ROS!), run some simple test and I'm done - in 20% of the time I will achieve the 80% ready 'thing'. The remaining 20% would take the longest, and I would consider it more 'productization phase' - creating a solid casing, adding a battery and a BMS, optimizing the timing of all sensors, figuring data formats, storage, single board computers... All of this work is not particularly hard, but it requires some serious grind. Do you have any thoughts on 80/20 in Robotics that you would like to share? Send me an [e-mail](mailto:mat@weeklyrobotics.com)! As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). Last week’s most clicked link was [IEEE article about the state of Machine Learning in 15 graphs](https://spectrum.ieee.org/tech-talk/artificial-intelligence/machine-learning/the-state-of-ai-in-15-graphs) with 11.8% opens.

{:.post-entry-title}
#### AWS DeepRacer Goes Open-Source

{:.post-source}
[GitHub](https://github.com/aws-deepracer)

Amazon's AWS [DeepRacer](https://aws.amazon.com/deepracer/), a small 1/18th scale race car's software has been made open source.

----

{:.post-entry-title}
#### Farming Robot Kills 100,000 Weeds per Hour With Lasers

{:.post-source}
[freethink](https://www.freethink.com/articles/farming-robot)

[Carbon Robotics](https://carbonrobotics.com/) is building a rover that will use laser to destroy weeds. I've been watching the space of agricultural robots killing weeds without chemicals, starting with [Tertill](https://tertill.com/), through [RBTX](https://rbtx.com/en/use-cases/ponchon-sas-autonomous-robot-laser-weed-agriculture-delta-robot) and [Weedbot](https://weedbot.eu/), and possibly many others. This space really seems promising, I can't wait to see more and more products like these being applied in the industry. Shout out to Myroslav for making me aware of the Carbon Robotics solution!

----

{:.post-entry-title}
#### ITECH M.Sc. 2019: Spatial Winding

{:.post-source}
[University of Stuttgart](https://www.icd.uni-stuttgart.de/teaching/master-theses/itech-m.sc.-2019-spatial-winding)

Check out this master thesis by Rebeca Duque Estrada and Fabian Kannenberg who created a system for creating structures from fibres. The system is using a massive robot arm with a custom end-effector and a 2-axis gantry that can move the released end effector at the bottom of the structure for the robot to grasp it back. I don't know if my explanation is very clear, so here is a [video](https://vimeo.com/507950769) showcasing the project.

----

{:.post-entry-title}
#### Mining robot stranded on Pacific Ocean floor in deep-sea mining trial

{:.post-source}
[Reuters](https://www.reuters.com/business/environment/mining-robot-stranded-pacific-ocean-floor-deep-sea-mining-trial-2021-04-28/)

Losing an attachment to a 25-tonne deep-sea mining robot at a depth of 4 km (2.5 mi) does sound suboptimal. Fortunately, Global Sea Mineral Resources (GSR), had managed to recover the prototype according to [this article](https://www.offshore-energy.biz/gsr-reconnects-deep-seabed-mining-robot-patania-ii/).

----

{:.post-entry-title}
#### R/C Ground Effect Vehicle with LiDAR Altitude Control

{:.post-source}
[YouTube (rctestflight)](https://youtu.be/nvMUYdr5_g8)

A neat video (love the custom soundtrack!) showing some development of an R/C aircraft capable of some proximity flying. I'm not sure if it's possible this aircraft is actually utilizing ground effect, but the results are still pretty nice.

----

{:.post-entry-title}
#### The Radio We Could Send to Hell

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/semiconductors/materials/the-radio-we-could-send-to-hell)

There is something exciting about the idea of sending a robot to an environment with an average temperature of 464 °C, with an acidic atmosphere and atmospheric pressure at the surface is 90 higher than the one we experience on Earth. Future missions to Venus can use Silicon-carbide circuits that can withstand the high temperatures for a prolonged amount of time. This article is a very good read on the topic, I highly recommend it, even if you are not planning to send anything to Venus any time soon.

----

{:.post-entry-title}
#### Publication of the Week - RoboStack - Using the Robot Operating System alongside the Conda and Jupyter Data Science Ecosystems (2021)

{:.post-source}
[arXiv](https://arxiv.org/abs/2104.12910)

If you always thought about integrating ROS and its packages with all the visualization and easy-to-use tools from Jupyter Notebook, then this article is a must-read for you. The authors describe RoboStack, a Conda channel that combines all the features of Conda package manager with the tools from JupyterLab to easily visualize and debug ROS topics, nodes, and even simulations. This integration allows you to install multiple ROS versions using a single line of command and run them simultaneously on one machine. It is also possible to make use of JupyterLab-ROS to display multiple widgets that are very powerful for debug purposes.

----

{:.post-entry-title}
#### WR Community Meeting #9 - Coffee with Nav2

{:.post-source}
[Eventbrite](https://www.eventbrite.com/e/153117748307)

This week, we will hold an informal chat with Steve Macenski, maintainer of [Nav2](https://navigation.ros.org/). If you have questions about this stack or have some ideas about features you would find useful, then this event will be a great opportunity to get input from Steve. As usual, we will hold the event on Thursday, at 7PM CEST. For the past meetup videos check out [our playlist](https://www.youtube.com/playlist?list=PL4NxwwJKGEA-LDNgkp1UPVwhu34xvhd7w) - the latest presentation from James Turnshek on how [Formant](https://formant.io/) manages fleets of robots will be uploaded later today.
