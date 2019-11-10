---
title: "Weekly Robotics"
description: "This week in Weekly Robotics Newsletter: humanoid robots reflexes, quadruped rover, autonomous cars not living to the expectations and more!"
date: 2019-11-10
tags: [Robotics, Careers, AutonomousCars, RobotSwarms, HumanoidRobots, OpenSource, Space, ]
idx: 64
---
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> I've been thinking recently of how we perceive robotics systems and tend to compare them to our own abilities. Every time I see a robot performing a task I'm subconsciously thinking how I'd perform this task. In unconstrained environments I'd be probably faster in most of the tasks, assuming the weights involved are low enough for me to handle. What I'm thinking is that it might be OK for the robots to be slower than us in tasks like produce picking or pick and place, after all they can do it for a full day or we can just add more robots to the system. I have this image in my head of a small mobile robot casually strolling down a raspberry field and slowly picking up fruits, while humming some relaxing robot tune.

1) Self-Transforming Robot Blocks Jump, Spin, Flip, and Identify Each Other.
<br>[MIT](http://news.mit.edu/2019/self-transforming-robot-blocks-jump-spin-flip-identify-each-other-1030)<br>
INFO: M-Blocks are self assembling modular robots, using magnets to attach to one another. The momentum required to make a block jump is created by applying a break to a flywheel which rotates at 20,000 RPM. The potential future use case described in the article of building a temporary staircase of such robots in a fire scenario sounds like something straight out of science-fiction books - can't wait!

2) This MIT Robot Wants to Use Your Reflexes to Walk and Balance.
<br>[Spectrum IEEE](https://spectrum.ieee.org/automaton/robotics/humanoids/mit-little-hermes)<br>
INFO: MIT Researchers propose a teleoperation system that is capable of dynamically synchronizing the motion of the robot with the motion of the operator. I like how small is the delay between the movement of the human and the corresponding reaction of the robot.

3) Pymanoid.
<br>[GitHub](https://github.com/stephane-caron/pymanoid)<br>
INFO: While we are at bipedal robots this repository contains an open source (GPL v.3.0 licenced) humanoid prototyping environment based on [OpenRAVE](http://openrave.org/docs/latest_stable/). If you would like to test this library then I recommend looking at [this tutorial](https://scaron.info/teaching/prototyping-a-walking-pattern-generator.html) as it sounds like a good way to get started.

4) UK's 1st Moon Rover to Launch in 2021.
<br>[space.com](https://www.space.com/uk-first-moon-rover-spacebit-launch-2021.html)<br>
INFO: This rover developed by [Spacebit](https://spacebit.com/) is a quadruped destined to moon in 2021. The body of the robot is built using standardized cubesat parts. The plan for this robot is to only walk at least 10 meters (33 feet). I would be very curious to see a power budget for a robot like this in a lunar environment.

5) Technique Helps Robots Find the Front Door.
<br>[MIT](http://news.mit.edu/2019/technique-helps-robots-find-front-door-1104)<br>
INFO: MIT engineers are using semantic techniques to teach a robot to navigate to front door or a garage. According to the article this approach is 189% faster than the classical navigation algorithms. In the video shown in the article we can see the algorithm in action in a simulated environment.

6) Perler Printer Pushes Pixel-Art Like No Sprite Artist Could.
<br>[Hackaday](https://hackaday.com/2019/10/23/perler-printer-pushes-pixel-art-like-no-sprite-artist-could/)<br>
INFO: This article contains one of the most satisfying video I've seen to date while working on this newsletter. This project is a 'Perler Beads printer' - a delta robot laying down beads to turn pixel art into physical objects.

7) Apple Co-Founder: 'I've Really Given Up' on Level 5.
<br>[Automotive News](https://europe.autonews.com/automakers/apple-co-founder-ive-really-given-level-5)<br>
INFO: Steve Wozniak is reportedly having doubts about humanity reaching Level 5 automation (for an overview of the automation levels you can check [this Wikipedia article](https://en.wikipedia.org/wiki/Self-driving_car#Levels_of_driving_automation)) in autonomous cars in his lifetime. In the article Wozniak is quoted saying "What we've done is we've misled the public into thinking this car is going to be like a human brain to be able to really figure out new things and say, 'Here's something I hadn't seen before, but I know what's going on here, and here's how I should handle it", a perfect opening for our Publication of the Week.

8) Publication of the Week - NTSB Report on Deadly Uber Crash (2019)(PDF).
<br>[NTSB](https://dms.ntsb.gov/public/62500-62999/62978/629713.pdf)<br>
INFO: NTSB (National Transportation Safety Board) released a report about the deadly crash involving Uber Autonomous car and a woman walking a bicycle that occured in March last year. The report is quite technical and if you work with autonomous systems then I can recommend reading it. Below are some quotes from the report:

> if  the  perception system  changes  the  classification  of  a  detected  object,  the  tracking history of that object is no longer considered when generating new trajectories. For such newly reclassified object, the predicted path is dependent on its classification, the object’s goal;

> When the system detects an emergency situation, it initiates action suppression. This is a one-second period during which the ADS suppresses planned braking while the (1) system verifies the nature of the detected hazard and calculates an alternative path, or (2) vehicle operator takes control  of  the  vehicle.

> Although  the  ADS  sensed  the  pedestrian  nearly  6  seconds  before  the  impact,  the  system  never classified  her  as  a  pedestrian—or  predicted  correctly  her  goal  as  a  jaywalking  pedestrian  or  a  cyclist—because she was crossing the N. Mill Avenue at a location without a crosswalk;  the system design did not include a consideration for jaywalking pedestrians.  Instead, the system had initially classified  her  as  an  other  object  which  are  not  assigned  goals.  As  the  ADS  changed  the  classification of the pedestrian several times—alternating between vehicle, bicycle, and an other—the system was unable to correctly predict the path of the detected object.

### Careers

1) Intermodalics (Leuven, Belgium) - [Various Positions](https://www.intermodalics.eu/join-us).
<br>
INFO: Intermodalics is a robotics software development firm, working for businesses world-wide, from our offices in Leuven, Belgium. We assist our customers in their product development journey, from technology exploration to product launch and beyond.

2) TerraClear (Bellevue, WA / Grangeville, ID, US) - [Robotics Systems Engineer / AI and Machine Vision Software Research Engineer](https://www.terraclear.com/company).
<br>
INFO: We are integrating advanced technologies such as aerial sensing, machine vision, high-accuracy GPS, and advanced robotics into our end-to-end rock picking solution.

3) Saga Robotics Ltd (Lincoln / Maidstone, UK) - [Various Positions](https://www.indeedjobs.com/saga-robotics-ltd/_hl/en_GB).
<br>
INFO: Saga Robotics are developing robotic solutions for soft fruit production, and are involved in several exciting projects world wide, including Norway, UK, and USA. The company works closely with universities as well as industry leaders in robotics and fruit production to create autonomous robots for farmers.
