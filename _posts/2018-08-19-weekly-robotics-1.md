---
title: "Weekly Robotics #1"
description: Weekly Robotics is born. This week we cover two space related robot project, a humanoid stuntman, a record-breaking UAV flight. On top of that we cover a IR dataset for ADAS and a great resource on Kalman Filter.
tags: [Robotics, FLIR, NASA, Airbus, Zephyr, Disney, ESA]
date: 2018-08-19
---

1) FLIR, the manufacturer of thermal imaging cameras, offers a free dataset for ADAS (autonomous driver-assistance systems) convolutional neural networks training. The web page below contains a form that you can fill to request the dataset.
<br>[https://www.flir.com/oem/adas/adas-dataset-form/](https://www.flir.com/oem/adas/adas-dataset-form/){:target="_blank"}<br>
INFO: The dataset contains over 14k images (60% of data captured during the day and 40% during night). Over 10k of captured frames are annotated.

2) NASA Jet Propulsion Laboratory published an open source mars rover project on github.
<br>[https://github.com/nasa-jpl/open-source-rover](https://github.com/nasa-jpl/open-source-rover){:target="_blank"}<br>
INFO: The project is based almost entirely on consumer off the shelf (COTS) parts. The total cost of all the parts is under 2500 USD. The team estimates a minimum of 200 man hours is needed to complete the project. It's worth to point out high quality of documentation in the project (for example [Ackermann steering](https://github.com/nasa-jpl/open-source-rover/blob/master/Software/Software%20Controls.pdf){:target="_blank"} is presented in a very straightforward way).

3) Airbus Zephyr High Altitude (high altitude pseudo satellite fixed wing aircraft) completed it's maiden flight by staying in the air for 25 days 23 hours and 57 minutes.
<br>[https://www.airbus.com/newsroom/press-releases/en/2018/08/Airbus-Zephyr-Solar-High-Altitude-Pseudo-Satellite-flies-for-longer-than-any-other-aircraft.html](https://www.airbus.com/newsroom/press-releases/en/2018/08/Airbus-Zephyr-Solar-High-Altitude-Pseudo-Satellite-flies-for-longer-than-any-other-aircraft.html){:target="_blank"}<br>
INFO: Zephyr is an electric-solar plane with a wingspan of 25 meters (82 feet) and weight of only 75 kg (165 pounds). The plane operates in stratosphere with an average altitude of 21 km (70,000 feet). [Here](https://www.youtube.com/watch?v=0IZW7llqReM){:target="_blank"} you can see the Zephyr launch.

4) Disney created a robotic stuntman.
<br>[https://www.engineering.com/DesignerEdge/DesignerEdgeArticles/ArticleID/17247/Disney-Brings-Robotic-Stunt-Double-to-Life.aspx](https://www.engineering.com/DesignerEdge/DesignerEdgeArticles/ArticleID/17247/Disney-Brings-Robotic-Stunt-Double-to-Life.aspx){:target="_blank"}<br>
INFO: [Here](https://www.disneyresearch.com/publication/stickman/){:target="_blank"} you can find a paper with stickman - what seems to be the first iteration of this project. The robot uses IMU and a rangefinder for state estimation mid flight and air actuated piston to change it's moment of inertia.

5) University of Texas has patented a smart skin, aimed at giving collaborative robots more sensitive tactile feeling than humans.
<br>[https://phys.org/news/2018-08-hairy-robot.html](https://phys.org/news/2018-08-hairy-robot.html){:target="_blank"}<br>
INFO: The sensors are made from zinc oxide [nanorods](https://en.wikipedia.org/wiki/Nanorod){:target="_blank"}, 0.2 micron in diameter and supposedly do not need any external voltage for operation.

6) A great explanation of how Kalman Filter works.
<br>[https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/](https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/){:target="_blank"}<br>
INFO: The article relies heavily on visualizations, making it more digestible.

7) ESA astronaut Alexander Gerst commanded a humanoid robot "Rollin' Justin" live from ISS (International Space Station). The robot was located in Germany.
<br>[https://youtu.be/TCXGNPgrDhw?t=1h10m28s](https://youtu.be/TCXGNPgrDhw?t=1h10m28s){:target="_blank"}<br>
INFO: [Rollin' Justin](https://www.dlr.de/rm/en/desktopdefault.aspx/tabid-11427/#gallery/29202){:target="_blank"} is a DLR (German Space Center) 200 kg (441 pounds), 1.91 m (6.27 feet) humanoid robot with 51 degrees of freedom. The experiment needs a level of autonomy from the robot. The communication delay is around 800ms therefore the robot needs to operate semi-autonomously. This technology could in the future allow astronauts to be on mars satellites and teleoperating robots that assemble habitats. The robot was using [April Tags](https://april.eecs.umich.edu/software/apriltag/){:target="_blank"} as means of localization. Couple of times during the experiment robot position estimation was off as it can be observed here: [1](https://youtu.be/TCXGNPgrDhw?t=1h16m41s){:target="_blank"}, [2](https://youtu.be/TCXGNPgrDhw?t=2h12m35s){:target="_blank"}. To recover from those issues the robot needs to look at one of many April Tags.

8) Weekly Robotics survey.
<br>[https://goo.gl/forms/ODd8vy54Tp2IBNq63](https://goo.gl/forms/ODd8vy54Tp2IBNq63){:target="_blank"}<br>
INFO: Thank you for joining us for the first issue of robotics weekly! Your feedback is very valuable to us and we would appreciate if you could fill this 3 minute survey on your expectations from us. Thank you!


