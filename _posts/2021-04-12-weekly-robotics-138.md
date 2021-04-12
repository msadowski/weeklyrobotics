---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: lots of DIY robotic arms, Ingenuity flight delay, magnetoquasistatic 3D localization, 'shedding' wheels of planetary rovers to keep mission running and more!"
date: 2021-04-12
tags: [Robotics, Space, Meetups, Drones, IndustrialRobots, Control, DIY, OpenSource]
idx: 138
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> Please join me, as I comb through a backlog of over 200 links to deliver some interesting news to you. From this issue onward any information about the future (there is a meetup this Thursday!) and past meetups will be posted at the bottom of the newsletter. As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). The most clicked link last week was [the sherp style 4 wheel drive rover](https://youtu.be/63go-gQNn5o) with 12.4% opens.

{:.post-entry-title}
#### Army of robots pushes the limits of astrophysics

{:.post-source}
[EPFL](https://actu.epfl.ch/news/army-of-robots-pushes-the-limits-of-astrophysics/)

Via article: One thousand newly-minted microrobots created in EPFL labs will soon be deployed at two large-scale telescopes in Chile and the United States. These high-precision instruments, capable of positioning optical fibers to within a micron, will vastly increase the quantity of astrophysics data that can be gathered – and expand our understanding of the Universe.

----

{:.post-entry-title}
#### Mars Helicopter Flight Delayed to No Earlier than April 14

{:.post-source}
[NASA](https://mars.nasa.gov/technology/helicopter/status/291/mars-helicopter-flight-delayed-to-no-earlier-than-april-14/)

While we are touching on space Ingenuity did not fly yet :(. Better safe than sorry! While we wait you can check out [this article and an interview](https://spectrum.ieee.org/automaton/robotics/space-robots/ingenuity-how-to-fly-a-helicopter-on-mars) with Håvard Grip, Ingenuity's chief pilot. I highly recommend the interview part, as it explains how useful simulation was in the design process.

----

{:.post-entry-title}
#### Making chainsaw robot, carving logs

{:.post-source}
[YouTube (Stuff Made Here)](https://youtu.be/ix68oRfI5Gw)

A very interesting video about using an industrial robot arm equipped with a chainsaw to cut shapes in styrofoam (hopefully wood too!). When I saw this video I immediately thought of [this research](https://youtu.be/lLKI0HWV3dc) - utilizing ABB YuMi dual-arm robot for hot-wire cutting.

----

{:.post-entry-title}
#### Building a 7 Axis Robot from Scratch

{:.post-source}
[YouTube (Jeremy Fielding)](https://youtu.be/HMSLPefUVeE)

While we are touching upon Industrial robot arms in a DIY space you can't miss this build by Jeremy Fielding that was published earlier this month. It looks like Jeremy is going to teach us a lot about making robot arms soon! Looking forward to the follow-up videos!

----

{:.post-entry-title}
#### POINTER: Seeing Through Walls to Help Locate Firefighters

{:.post-source}
[NASA](https://www.nasa.gov/feature/jpl/pointer-seeing-through-walls-to-help-locate-firefighters)

NASA is developing a new 3D localization system utilizing magnetoquasistatic fields for localization. The biggest advantage? The signals can penetrate all kinds of materials used in buildings, while still providing several inches of accuracy. The current version of the system has a range of 230 feet (70 meters) but according to the article, the system will support higher distances in the future. I'm wondering if we will ever see this kind of system making it to the robotics domain. Interestingly, Disney Research also [looked into this technology](https://la.disneyresearch.com/publication/magnetoquasistatic-tracking-of-an-american-football-a-goal-line-measurement/) and published this [video demostrator](https://www.youtube.com/watch?v=tnYuH2L0Q4E).

----

{:.post-entry-title}
#### Robot Arm Achieves Amazing Accuracy With Just Servos

{:.post-source}
[Hackaday](https://hackaday.com/2021/03/19/robot-arm-achieves-amazing-accuracy-with-just-servos/)

How precise can hobby-grade servos be? Turns out crazy precise! This is a very interesting demonstrator by Adam Bäckström.

----

{:.post-entry-title}
#### Publication of the Week - Rimmed Wheel Performance on the Mars ScienceLaboratory Scarecrow Rover (2019)(PDF)

{:.post-source}
[JPL](https://www-robotics.jpl.nasa.gov/publications/Arturo_Rankin/Rimmed_Wheel_Performance_on_the_Mars_Science_Laboratory_Scarecrow_Rover.pdf)

The Mars Science Laboratory (MSL) Curiosity rover experienced an unexpectedly high rate of damage on the rover wheels. This damage could lead to other types of loss that could put the mission at risk. This paper describes all the methods used to provide a very interesting solution to this problem. To reduce the effects of the broken wheel's grousers, the rover could be remotely commanded to shed 1/3 of the wheel’s outer ring by hitting it in an immovable rock. To test the validity of this proposal, the team tested the Scarecrow rover at the JLP Mars Yard in different terrains and slopes to evaluate slippage, heading error, motor current, and many more metrics. It is interesting to see that even robust robots like the rover, sometimes need out-of-the-box solutions.

----

{:.post-entry-title}
#### WR Community Meeting #6 - RoboCup@Home with team TechUnited

{:.post-source}
[Eventbrite](https://www.eventbrite.com/e/150152238387/)

RoboCup is one of the largest robotics competitions world-wide. The competition's various leagues focus on robots playing soccer, helping in disaster situations, in factories and at home. In RoboCup@Home, both custom-built and commercial service robots perform a multitude of service tasks. In 2019, team TechUnited Eindhoven won a first prize with their robot HERO. Loy van Beek will present what RoboCup is all about and how team TechUnited won their first prize.

----

{:.post-entry-title}
#### Previous Meeting #5 - Webots

{:.post-source}
[YouTube (WeeklyRobotics)](https://youtu.be/UQ08JT05o5k)

Last week Darko made a very good presentation about Webots. Some highlights I found particularly interesting are: Webots supports [GitHub actions](https://github.com/cyberbotics/webots-animation-action), and it can nicely work with your continuous integration. [Robot Benchmark](https://robotbenchmark.net/) is a library of online simulated environment created by Cyberbotics. It allows you to program the simulated robots on the web, and will allow for virtual competitions. In my opinion, this could be a really valuable learning tool.

If you would like to present your robotics-related projects or ideas in one of the meetings or know someone interested, please [let me know](mailto:mat@weeklyrobotics.com)!
