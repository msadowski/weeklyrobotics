---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: sensing things with lasers, the third thumb project, kirigami-inspired gripper and more!"
date: 2021-05-24
tags: [Robotics, Quadrupeds, Bipedal, Research, DIY, Bionics]
idx: 144
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> Unfortunately, this week we won't have the WR meetup either, but the next week look hopeful! More details coming in a week! As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). The most clicked link last week was [the album showing robots everywhere](https://www.theatlantic.com/photo/2021/05/photos-robots-are-everywhere/618823/) with 18.8% opens!

{:.post-entry-title}
#### With A Big Enough Laser, The World Is Your Sensor

{:.post-source}
[Hackaday](https://hackaday.com/2021/05/21/with-a-big-enough-laser-the-world-is-your-sensor/)

Here is an interesting idea from the team behind Vibrosight++ - use laser aimed at reflective markers to monitor vibration and estimate city 'behaviours' (e.g. traffic passing on a bridge, fan working).

----

{:.post-entry-title}
#### 2021 Hackaday Prize: Rethink, Refresh, And Rebuild

{:.post-source}
[Hackaday](https://hackaday.com/2021/05/18/2021-hackaday-prize-rethink-refresh-and-rebuild/)

While we are visiting Hackaday - the 2021 Hackaday Prize is on! Every year I enjoy going through the submissions as some of them make for fantastic content for this newsletter. If you are reading this newsletter chances are you will find the "Redefine Robots" track interesting! If you submit your project, let me know, and I'll be more than happy to share your design with the community.

----

{:.post-entry-title}
#### Third Thumb Project

{:.post-source}
[daniclodedesign.com](https://www.daniclodedesign.com/thethirdthumb)

Researchers at [Plasticity Lab](https://plasticity-lab.com/) have been studying people using a 'third thumb' - a mechanical thumb controlled by toes. Interestingly humans were very quick to adapt to using it as can be seen in the video. If you would like to learn more about the study then I found [the paper](https://www.biorxiv.org/content/10.1101/2020.06.16.151944v1) for you.

----

{:.post-entry-title}
#### This Robot's Soft Gripper Was Inspired By Japanese Kirigami

{:.post-source}
[YouTube (Boston University)](https://youtu.be/UerxNyu147g)

While we are on the topic of things that can be used to grip other things - here is a kirigami inspired gripper that supposedly is very gentle with the things it's picking up.

----

{:.post-entry-title}
#### Discovering candidate for reflex network of walking cats: Understanding animals with robots

{:.post-source}
[YouTube (Control and Robotics)](https://youtu.be/-iLHRhvDccA)

I'm all in for using robots instead of animals for neurological research, and it looks like this quadruped from Osaka University could help. The design can "reproduce the neuro-muscular dynamics", allowing to create reflexive walking behaviours. For more details about this project, you can check out [this paper](https://www.frontiersin.org/articles/10.3389/fnbot.2021.636864/full).

----

{:.post-entry-title}
#### Agility Robotics' Cassie Is Now Astonishingly Good at Stairs

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/humanoids/agility-robotics-cassie-stairs)

When Evan says this robot is "probably better at stairs than you are" - I agree in this context. If you blindfold me and set me off in the random direction saying I'll encounter stairs at some point I wouldn't be as sure-footed as Cassie is in these experiments. The article linked goes into detail about this work, but if you want more then [here is the paper](https://arxiv.org/pdf/2105.08328.pdf). Big thanks to Darko for linking this in our WR Slack channel!

----

{:.post-entry-title}
#### Publication of the Week - SLAM Toolbox: SLAM for the dynamic world (2021)

{:.post-source}
[JOSS](https://joss.theoj.org/papers/10.21105/joss.02783)

Last week's publication, we talked about a Collaborative Visual SLAM Framework for Service Robots used mainly for large buildings that require multiple robots. To use SLAM in such extensive areas, this paper presents the SLAM Toolbox ROS package. This Toolbox came to replace GMapping and has lots of new functionalities that can be a game changer in many applications. Among its features, the package can map spaces using mobile Intel CPUs on areas over  100,000 ft^2 (~9,000 m^2), using multi-threaded processing with 3 major operation modes with modern graph-optimization techniques. This is already being used in robots, such as Simbe Robotics’ Tally, ROBOTIS’ Turtlebot3, and many more.
