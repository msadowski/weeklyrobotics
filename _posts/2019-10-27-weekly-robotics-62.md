---
title: "Weekly Robotics"
description: "This week in Weekly Robotics: introducing a SLAM library of the week, interesting robot joints, robot hand and an architecture of force feedback systems"
date: 2019-10-27
tags: [Robotics, Careers]
idx: 62
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

1) ROSCon 2019.
<br>[roscon.ros.org](https://roscon.ros.org/2019/)<br>
INFO: ROSCon is happening next week from October 31st to November 1st. [The talks lineup](https://roscon.ros.org/2019/#day-1-october-31st) is quite exciting and I'll definitely be following it. Usually there is a livestream of the talks, check out the conference page for updates.

2) LaMa - A Localization and Mapping Library.
<br>[GitHub](https://github.com/iris-ua/iris_lama)<br>
INFO: Feels like this newsletter will need a "SLAM Solution of the week section" if I keep learning about SLAM libraries at the current rate! Regarding this library there was an interesting discussion about it on [ROS Discourse](https://discourse.ros.org/t/announcing-lama-an-alternative-localization-and-mapping-package/10916) where the author of the library presented it to the community. The thing that caught my attention the most is how little resources this library uses. The GitHub repository description mentions that Raspberry Pi 3 Model B+ is the minimum viable computer to run it.

3) Humanoid Robot Has Joints That Inspire.
<br>[Hackaday](https://hackaday.com/2019/10/20/humanoid-robot-has-joints-that-inspire/)<br>
INFO: This article presents the LIMS2-AMBIDEX humanoid robot upper body developed by Researchers from IRIM Lab at Korea University of Technology and Education. The robot is driven using brushless motors and pulleys and I indeed found the wrist mechanism inspiring! In the comment a Hackaday user anil inverse provided a link to a [GitHub repository](https://github.com/adamlukomski/parallelwrist) that contains an stl model of the wrist mechanism that you can 3D print.

4) Anki Patent Portfolio Is Now for Sale.
<br>[The Robot Report](https://www.therobotreport.com/anki-consumer-robotics-patent-portfolio-sale/)<br>
INFO: Anki was a consumer robot manufacturer that close down earlier this year (as featured in [Weekly Robotics #37](https://weeklyrobotics.com/weekly-robotics-37)). As reported in the article the patent portfolio of the company is [now for sale](https://www.hilcostreambank.com/acquisition-opportunities/anki). I'm still bummed about Anki closing down I had high hopes for it and wanted to experiment with it using [vector_ros](https://github.com/betab0t/vector_ros) at one point.

5) Robot Teaches Kids Hand Washing Skills in Rural India.
<br>[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/robot-teaches-kids-hand-washing-skills-in-rural-india)<br>
INFO: Usually the robots I feature in this newsletter are a bit more sophisticated than the current version of Pepe shown in the article, however I believe it can have quite a positive impact. The experiment with this robot took only 3 days but throughout this time the hand washing rate of students increased by 40%.

6) Robert Williams (Robot Fatality).
<br>[Wikipedia](https://en.wikipedia.org/wiki/Robert_Williams_(robot_fatality))<br>
INFO: Let's take a dark turn. This Wikipedia page describes the death of Robert Willimas, who died in 1979 in one of the Ford plants and is the first known human to be killed by a robot. According to Wikipedia the second person to be killed by a robot was [Kenji Urada](https://en.wikipedia.org/wiki/Kenji_Urada) who at the time worked at Kawasaki Heavy Industries.

7) Publication of the Week - Mantis: A Scalable, Lightweight and Accessible Architecture to Build Multiform Force Feedback Systems (2019).
<br>[anneroudaut.fr](http://anneroudaut.fr/Mantis/MantisPaper.pdf)<br>
INFO: This paper by Researchers from the University of Bristol presents Mantis, a system architecture for creating force feedback systems. I've learned multiple things from this paper - especially on motor selection, impedance vs admittance control and transmission systems. You can find a video of Mantis systems [on YouTube](https://youtu.be/h1m_QuHe6Rg).

### Sponsored

1) Webots Now Available from the Snap Store.
<br>[snapcraft](https://snapcraft.io/webots)<br>
INFO: Webots R2019b revision was just released on the snap store so that you can install it safely and easily on your favorite Linux distribution. That is probably the easiest way to install Webots since all the dependencies are included, including the C/C++/Java compilers, python 3, etc. Also snap packages are safe as they run in a protected sand-box on your Linux computer and hence cannot harm it, can be uninstalled easily and can handle different versions of the software.

### Careers

1) [NVIDIA](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Software-Engineer---Robotics_JR1925220) (Santa Clara, CA, US) - Senior Software Engineer - Robotics.
<br>
INFO: The team around Project Isaac is building a robotics platform for developing the next generation of intelligent robots. Isaac is binding together high-fidelity visual and physical simulation, a high-quality developing platform, hundreds of optimized algorithms to tackle hard problems in computer vision and artificial intelligence, and a small and powerful computational platform to form the brain of intelligent machines.

2) [Space Application Serivces](https://www.spaceapplications.com/career/robotics-software-engineer-sensor-fusion-simulation/) (Brussels, Belgium) - Robotics Software Engineer - Sensor Fusion & Simulation.
<br>
INFO: Space Applications Services is a company based in the Brussels area (BE) that provides products and services for the space sector in many areas from Avionics, Robotics, Human Exploration, Science and Earth Observation.

3) [GIM Robotics](http://gimltd.fi/careers.html) (Espoo, Finland) - Robotics Engineer.
<br>
INFO: GIM provides full-stack automation and intelligent sensor systems for logistics, mobility and maintenance. Focus on sensor fusion software for autonomous navigation in large outdoor areas.
