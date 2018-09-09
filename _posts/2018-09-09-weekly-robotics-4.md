---
title: "Weekly Robotics #4"
description: "Single rotor drone, satellite capture and deorbitting, animatronic dinosaurs welcoming hotel guests, vacuum cleaners doing Simultaneous Localization And Mapping (SLAM), Skydio introducing a developer platform, Real-time robotics communications in Linux and a comparison of open source robot simulators."
date: 2018-09-09
---

1) Ikarus Single Rotor Drone.
<br>[http://omeganaught.com/2018/08/ikarus-electric-rocket/](http://omeganaught.com/2018/08/ikarus-electric-rocket/){:target="_blank"}<br>
INFO: One of the most interesting drone projects we've seen lately. A single rotor drone Ikarus "rocket" is based on a 70$ ducted fan. The 30 minutes investment in watching the [following video](https://www.youtube.com/watch?v=RMeEh5OUaDs){:target="_blank"} will show you the decision process the author of this project has taken, the problems he experienced and lessons learned. What seems to be the core problem to solve in this type of aircraft is the gyroscopic effect compensation (very well explained at 08:00 in the video). In the linked page you will find part lists, CAD designs and autopilot setup.

2) ESA satellite deorbiting mission.
<br>[http://www.esa.int/Our_Activities/Space_Engineering_Technology/Clean_Space/e.Deorbit](http://www.esa.int/Our_Activities/Space_Engineering_Technology/Clean_Space/e.Deorbit){:target="_blank"}<br>
INFO: Space is full of junk that can delay launches or put spacecraft or astronauts at risk. ESA e-deorbit mission aims at creating a custom spacecraft to capture a retired ESA satellite and move it in such way that it burns down in the atmosphere. Currently two capture methods are considered: a net and a robotic arm (it seems that at early stages of the project a harpoon was also a consideration). 

3) Japanesee hotel staffed by dinosaurs.
<br>[https://phys.org/news/2018-08-robotel-japan-hotel-staffed-robot.html/](https://phys.org/news/2018-08-robotel-japan-hotel-staffed-robot.html){:target="_blank"}<br>
INFO: Henn na Hotel in Japan is said to be fully staffed by robots. The guests will experience animatronic dinosaurs and fish in the hotel lobby, as well as robotic vacuum and window cleaners. Inside the rooms the guests will find a dinosaur egg assistant, allowing them to control some aspects of the room (light, TV and so on). If you want to see the hotel in action there is a [video by Abroad In Japan](https://youtu.be/P9DBb-Eng20){:target="_blank"}.

4) Neato vacuum cleaners to introduce persistent maps.
<br>[https://spectrum.ieee.org/automaton/robotics/home-robots/neato-introduces-new-robot-vacuums-adds-zone-cleaning-to-d7](https://spectrum.ieee.org/automaton/robotics/home-robots/neato-introduces-new-robot-vacuums-adds-zone-cleaning-to-d7){:target="_blank"}<br>
INFO: The more devices performing SLAM and utilizing LiDAR the better (at least for those of us waiting impatiently for LiDAR sensor prices to go down). With this feature Neato users will be able to specify the areas the vacuum cleaner should focus on the most. 

5) Skydio to introduce a developer platform
<br>[https://www.suasnews.com/2018/09/skydio-continues-to-push-the-frontier-of-autonomous-flying-robots/](https://www.suasnews.com/2018/09/skydio-continues-to-push-the-frontier-of-autonomous-flying-robots/){:target="_blank"}<br>
INFO: Skydio, is a drone platform famous for its obstacle avoidance capabilities and tracking ([here](https://youtu.be/L8l4vTgd0Y0){:target="_blank"} you can see its performance in a warehouse full of obstacles). The developer platform will allow to create custom Skills(application specific behaviours), issue movement commands, query 3D map distances, obtain telemetry data etc. 

6) Real-time Linux communications for robotic applications 
<br>[https://medium.com/@vmayoral/real-time-linux-communications-2faabf31cf5e](https://medium.com/@vmayoral/real-time-linux-communications-2faabf31cf5e){:target="_blank"}<br>
INFO: Computer Science ahead! This article from Erle Robotics engineers analyzes using Real-time Preemption Patch for UDP communication in Linux. If you look at the table that compares the results in the article you can see that without a Real-time patch the latency varies a lot (in case of stress test it's between 262 to 46742 µs for no RT patch and 254 to 618 µs for RT Normal). Latency is especially important topic when working with safety certified systems - it's not fast results that are of interests but consistency and determinism. 

7) Paper of the week - Feature and performance comparison of the V-REP, Gazebo and ARGoS robot simulators.
<br>[http://lenkaspace.net/tutorials/robotics/robotSimulatorsComparison](http://lenkaspace.net/tutorials/robotics/robotSimulatorsComparison){:target="_blank"}<br>
INFO: This blog post (and a paper it links to) is a comparison of 3 open source robotics simulators: V-REP, Gazebo and ARGoS. 