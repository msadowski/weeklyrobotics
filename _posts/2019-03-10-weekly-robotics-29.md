---
title: "Weekly Robotics #29"
description: "In this issue we discover robotics project with Google Summer of Code, we get insights from using drones at sea, and observe helicopter flying made easy."
date: 2019-03-10
tags: [Robotics, Careers, OpenSource, Drones, Sensors, Programming, AutonomousCars, Aviation]
---

1) Google Summer of Code 2019.
<br>[Google](https://summerofcode.withgoogle.com/)<br>
INFO: "Google Summer of Code is a global program focused on bringing more student developers into open source software development". The Robotics and Space related projects students can contribute to this year are: [ArduPilot](https://summerofcode.withgoogle.com/organizations/5883027960365056/), [JdeRobot](https://summerofcode.withgoogle.com/organizations/6728816414687232/), [RoboComp](https://summerofcode.withgoogle.com/organizations/5371847267319808/), [Open Source Robotics Foundation](https://summerofcode.withgoogle.com/organizations/6099855632498688/), [JSK Robotics Laboratory](https://summerofcode.withgoogle.com/organizations/6626799532900352/), [Open Roberta](https://summerofcode.withgoogle.com/organizations/4856641372028928/), [OpenCV](https://summerofcode.withgoogle.com/organizations/5654472617885696/), [RTEMS Project](https://summerofcode.withgoogle.com/organizations/5907269225545728/), [Libre Space Foundation](https://summerofcode.withgoogle.com/organizations/6444860416983040/), [GNSS-SDR](https://summerofcode.withgoogle.com/organizations/5772865612283904/), [BRL-CAD](https://summerofcode.withgoogle.com/organizations/5998740693843968/). If we've missed any projects please send us [an e-mail](mailto:contact@weeklyrobotics.com) and we will update the list.

2) Drones At Sea: The Highs & Lows of a Parley SnotBot Expedition.
<br>[DroneLife](https://dronelife.com/2019/03/08/drones-ocean-alliance-parley-snotbot-expedition/)<br>
INFO: This article from DroneLife talks about Ocean Alliance usage of drones for whale monitoring in a SnotBot expedition. Even though the team faced numerous challenges they managed to achieve the expedition objective of capturing over 50 biological samples.

3) Optical Gyro Dwarfed by a Grain of Rice.
<br>[Elektor](https://www.elektormagazine.com/news/optical-gyro-dwarfed-by-a-grain-of-rice)<br>
INFO: Caltech engineers developed an optical gyroscope the size of a grain rice. From the article we've learned that the optical gyroscopes make us of Sagnac effect ([Wikipedia](https://en.wikipedia.org/wiki/Sagnac_effect), [Simple simulation on YouTube](https://www.youtube.com/watch?v=Fk0RvzaHq_Q]) and are usually the size of a golf ball.

4) Bare Metal STM32 Programming and a Quadcopters Awakening.
<br>[timakro.de](https://timakro.de/blog/bare-metal-stm32-programming/)<br>
INFO: In this blog post Tim Schumacher describes his experience in programming an STM32 chip onboard Crazypony mini, a 100$ mini quadrotor. Even though the author only shows how to control a single LED this article can be a good entry point for anyone looking into programming embedded autopilots.

5) Vehicle Path Planning.
<br>[Razor Code](http://razorcode.net/articles/vehicle-path-planning.html)<br>
INFO: This article on vehicle path planning by David Olsen talks a lot about heuristics of path planning and optimization. It also showcases an interesting vehicle model and approaches to path optimization.

6) I Flew a Helicopter, and then the Helicopter Flew Me.
<br>[The Verge](https://www.theverge.com/transportation/2019/3/5/18250996/sikorsky-autonomous-helicopter-flying-taxi-lockheed)<br>
INFO: Piloting a helicopter after 45 minutes of training on simulator? It is now possible with SARA (Sikorsky Autonomy Research Unit). The system is fit with a fly-by-wire system allowing the pilot to control the aircraft using two inceptors (a lever and a joystick). The system comes with an HMI (Human Machine Interface) in form of a screen with widgets, allowing the pilot to plan flight parameters that the aircraft will execute automatically.

7) Publication of the week - Autonomous  Drifting  using  Simulation-Aided  Reinforcement  Learning (2016).
<br>[WeeklyRobotics](https://weeklyrobotics.com/publications/autonomous_drifting/Cutler16_ICRA_final_submission.pdf)<br>
INFO: This paper by Mark Cutler and Jonathan P. How introduces a framework that  combines  simple and  complex  continuous  state-action  simulators  with  a  real-world robot to efficiently find good control policies, while minimizing the number of samples needed from the physical robot. While many Reinforcement Learning Researchers use expert demonstration to initialize the models, the authors of this paper chose an approach in which they generate initial policies from simple models. On the car Researchers track velocities in x and y direction (the information is provided by a motion capture system), turn rate and wheel speed. By applying the algorithm shown in this paper combined with prior simulated information the R/C car was able to drift as it can be seen in [this YouTube video](https://youtu.be/opsmd5yuBF0). You can download additional material to the paper [here](https://weeklyrobotics.com/publications/autonomous_drifting/Cutler16_ICRA_additional.pdf).


### Careers

1) [Saildrone](https://www.saildrone.com/careers) (Alameda, CA, US) - Various Positions.
<br>
INFO: Saildrone's mission is to create the highest resolution ocean data set in the world and use it to make global processes such as weather forecasting, carbon cycling, global fishing, and climate change more predictable, visible, and actionable. We've linked to their Unmanned Surface Vehicle and Arctic mission in [Weekly Robotics #28](https://weeklyrobotics.com/weekly-robotics-28).

2) [Remy Robotics](https://remy-robotics.breezy.hr/) (Barcelona, Spain / Moscow, Russia) - Various Positions.
<br>
INFO: Remy Robotics is using robotic technology to take the routine and inefficiency out of cooking, creating a ‘robot chef’ that can help cook any cuisine or any dish in the world.

3) [Samsung](https://samsungresearchamerica.applytojob.com/apply/nF5l2HnkrT/Robotics-Open-Source-Engineer-Staff-Engineer-Engineer?source=LINK) (Mountain View, CA, US) - Robotics Open Source Engineer.
<br>
INFO: Open Source Group (OSG) under Samsung Research is the corporate Open Source Program office for all open source activities in Samsung.

