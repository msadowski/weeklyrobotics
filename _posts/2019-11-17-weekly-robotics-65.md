---
title: "Weekly Robotics"
description: "This week in the newsletter: old robots playing piano, 3D printers, weird looking robots, ROS for beginners, precision agriculture and more!"
date: 2019-11-17
tags: [Robotics, HumanoidRobots, MobileRobots, Manufacturing, SoftRobotics, QuadrupedRobots, AgriculureRobots]
idx: 65
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> This weekend I’m attending [Zoohackathon](http://www.zoohackathon.com/Geneva) thinking how we can use technology to improve anti-poaching efforts. As we’ve learned in [Weekly Robotics #30](https://weeklyrobotics.com/weekly-robotics-30) just using drones does not necessarily solve the problem. Do you have experience using Robotics in conservation efforts? I'd love to [hear from you](mailto:contact@msadowski.ch).

1) WABOT-2.
<br>[YouTube](https://youtu.be/ZHMQuo_DsNU)<br>
INFO: Reddit user LiesGround submitted the picture of Wabot-2 on [/r/robotics](https://www.reddit.com/r/robotics/comments/dumqe7/q_what_happened_to_wabot2_is_there_more_footage/) asking if anyone has any visual materials of the robot. Maybe you can help? WABOT-2 is an anthropomorphic robot playing musical instruments developed by Researchers from Waseda University in the 1980s. The robot contained subsystems responsible for: limb control, vision, conversation, singing voice tracking and supervision. Unfortunately, I couldn't find any information about WABOT-2 that was in English and was not a [paywalled research paper](https://www.sciencedirect.com/science/article/pii/0167849387900027) (if you however have an access to it it's quite informative but personally I wouldn't pay $30 for accessing it).

2) Core XY Explained.
<br>[Hackaday](https://hackaday.com/2019/11/12/core-xy-explained/)<br>
INFO: I didn't realize I was so far behind in the 3D printing tech. I found the video to be quite a good overview of various 3D printer types kinematics and the part I found particularly useful is the CoreXY kinematics explanation with all the advantages and disadvantages.

3) Wyss Institute Researchers Create a Fast Multimaterial 3D Printer.
<br>[3DPrint.com](https://3dprint.com/259784/wyss-institute-researchers-create-a-fast-multimaterial-3d-printer/)<br>
INFO: While we are on the topic of 3D printing; Wyss Institute for Biologically Inspired Engineering Researchers had developed a 3D printing method that allows switching the printing material at up to 50 times a second. This technique can be especially useful for rapid development of soft-robotics thanks to having materials with different stiffness. The linked article has a video that explains the concept behind this 3D printing method.

4) Harvard's UrchinBot Is One of the Weirdest Looking Robots We've Ever Seen.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/harvard-amphibious-urchinbot)<br>
INFO: I hold similar views to Evan Ackerman: in my case this is the weirdest looking robot I've seen as well.

5) Quadruped Robots Can Climb Ladders Now.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/quadruped-robots-can-climb-ladders-now)<br>
INFO: At IROS 2019 Researchers from Tokyo Metropolitan University and Okayama University had presented this quadruped robot that can climb vertical ladders. According to the article only 1 in 5 climbs was successful with the current hardware used, however the Researchers hope to improve their setup to reduce the amount of failures and to be able to climb any ladder without prior training. If you watch the video shown in the article pay attention to the time rate shown in the lower left corner; it looks like the task is quite consuming at the moment.

6) Your First Robot: A Beginner’s Guide to Ros and Ubuntu Core [1/5].
<br>[kyrofa.com](https://kyrofa.com/posts/your-first-robot-a-beginner-s-guide-to-ros-and-ubuntu-core-1-5)<br>
INFO: The linked article is the first in a blog post series on setting up an inexpensive (~$95) robot with Raspberry Pi and ROS. If you've never used ROS before this series might be a good practical start!

7) Publication of the Week - Building an Aerial-Ground Robotics System for Precision Farming (2019).
<br>[arXiv](https://arxiv.org/abs/1911.03098)<br>
INFO: The thing I like the most about [precision agriculture](https://en.wikipedia.org/wiki/Precision_agriculture) is that it can drastically reduce the use of chemicals when farming. This paper introduces the Flourish project that aims at creating a precision farming solution comprised of UAV (Unmanned Aerial Vehicle) for performing aerial surveys and an UGV (Unmanned Ground Vehicle) to perform interventions in the field. The UAV used in the project is a DJI Matrice 100 multirotor. The UGV is BoniRob Farming Robot created by Bosch (for more details about this platform you can check [this excellent IEEE Spectrum article](https://spectrum.ieee.org/automaton/robotics/industrial-robots/bosch-deepfield-robotics-weed-control)). For those of you interested in mobile robots I highly recommend reading the section on navigation and using crop rows to aid localization.
