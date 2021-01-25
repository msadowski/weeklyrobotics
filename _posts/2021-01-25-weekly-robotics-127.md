---
title: "Weekly Robotics"
description: "This week in Weekly Robotics newsletter: Project Loon closing down, rotor failure recovery for multirotors, cuspidal robots and more!"
date: 2021-01-25
tags: [Robotics, RobotArms, MobileRobots, ROS, Machining]
idx: 127
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Project Loon](https://blog.x.company/loons-final-flight-e9d699123a96)*

> Another Monday, another issue of the newsletter! You will notice that in this edition a Job Seekers and Careers section are in again. The deal is simple - you send me your profile or a robotics-related job post and I publish it in the newsletter (no agencies, please!). As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). Thanks! The most clicked link last week was [the paper on SwarmRail](https://elib.dlr.de/133813/1/ICRA_2020_Swarmrail_Final.pdf) with 13.6% opens.

{:.post-entry-title}
#### Loon’s Final Flight

{:.post-source}
[X](https://blog.x.company/loons-final-flight-e9d699123a96)

Loon, one of X moonshot projects aiming to beam internet from stratospheric balloons is shutting down. It's definitely a bummer, especially given that the team was recently up to getting some [interesting results](https://medium.com/loon-for-all/drifting-efficiently-through-the-stratosphere-using-deep-reinforcement-learning-c38723ee2e90) in using Reinforced Learning for navigation, and some balloons staying in the stratosphere for as long as [312 days](https://youtu.be/e_QI5llQrF0).

----

{:.post-entry-title}
#### Autonomous Quadrotor Flight despite Rotor Failure with Onboard Vision Sensors: Frames vs Events

{:.post-source}
[YouTube (UZH Robotics and Perception Group)](https://youtu.be/Ww8u0KH7Ugs)

Neat work by RPG team from the University of Zurich. First of all, a quadrotor can recover from a rotor failure, what is more, the navigation and localization still work (all in GPS-denied environment). Every time I see a demonstrator featuring an event camera from RPG folks I'm amazed. I can't wait for the wider adoption of these sensors!

----

{:.post-entry-title}
#### Fast Visual Servoing with MoveIt

{:.post-source}
[PickNick](https://picknik.ai/visual%20servoing/moveit%20servo/2021/01/21/fast-visual-servoing-with-moveit.html)

This blog post can be a nice intro into Moveit Servo, with some hints for things like PID tuning.

----

{:.post-entry-title}
#### Anatomy of a CNC Router

{:.post-source}
[mattferraro.dev](https://mattferraro.dev/posts/cnc-router)

Here is an interesting encyclopedia style article by Matt Ferraro. Matt did a very good research job here if you are thinking of building your own CNC router this blog post might be a great starter!

----

{:.post-entry-title}
#### Why you should know about cuspidal robots

{:.post-source}
[medium](https://achille0.medium.com/why-has-no-one-heard-of-cuspidal-robots-fa2fa60ffe9b)

Are you like me and never heard of cuspidal robot arms? This blog post by Achille Verheye is a great introduction to the topic. After reading this article I'm curious why a question whether the robot is cuspidal is not one of the first ones we ask when looking into a robot arm? If you want to research this topic further then you are in luck because Achille wrote a [second post](https://achille0.medium.com/under-the-radar-cuspidal-robots-7091eca01271) on the topic that is more in-depth! If you want to do even more research than [this paper](https://arxiv.org/abs/1610.04080) is where I would start.

----

{:.post-entry-title}
#### Parent robot (BIG STAR) collaborating with a child robot (RSTAR)

{:.post-source}
[YouTube (zarrouk lab)](https://youtu.be/utkj6xpMYK0)

Here is an interesting mobile robot platform from Bio-inspired and Medical Robotics Lab at the Ben Gurion University of the Negev. Not only can it lower itself down by 'folding' wheels but it also has a ramp to carry a smaller clone of itself.

----

{:.post-entry-title}
#### Publication of the Week - SLOAM: Semantic Lidar Odometry and Mapping for Forest Inventory (2019)

{:.post-source}
[arXiv](https://arxiv.org/abs/1912.12726)

Mapping environments surrounded by leaves, thorns, and vines are quite challenging, and even LiDAR methods can fail at this task. The article describes a way to use semantic segmentation to estimate three diameters and map forests. The author uses a fully convolutional neural network (FCN) to perform the segmentation to feed the data to update odometry and generate a map. To train the FCN the authors created a virtual reality tool to label the point cloud data and make the process less time-consuming. Finally, the method can be very useful to evaluate preserved forests and generate deforestation metrics.

{:.post-entry-title}
### Weekly Robotics 2 Years Ago

{:.post-source}
[Issue 22](https://weeklyrobotics.com/weekly-robotics-22)

Around 2 years ago we were looking into EPFLs Bio-Robotics lab project aiming to recreate gait of a [fossilized 300 million year old animal](https://actu.epfl.ch/news/a-robot-recreates-the-walk-of-a-300-million-year-o/). This project was among many that I've discussed with Professor Auke Ijspeert in the first and only [Weekly Robotics podcast episode](https://youtu.be/tFn7KcW_RRg).

[Passerine Aircraft jumping-flying robot](https://spectrum.ieee.org/automaton/robotics/drones/delivery-drones-use-birdinspired-legs-to-jump-into-the-air) seemed like an interesting project at a time. Unfortunately, it looks like the project website is down and the last entry on the [company's Facebook page](https://www.facebook.com/PasserineAircraft/) is from March 2019.

----

### Job Seekers

[In the issue #83](https://weeklyrobotics.com/weekly-robotics-83) I've started this section to try to help out those looking for work in the times of pandemic. If you are currently looking for work then feel free to [send me](mailto:mat@weeklyrobotics.com) your details in the same format as you can see in the entries below.

**Name**: Diego Avila<br>
**Location**: Milan, Italy. Willing to relocate within Europe<br>
**Skills**: Javascript, Java, Python, C++, Linux, ROS<br>
**Profile**: I’m a Software Engineer, recently graduated as MSc. in Computer Science & Engineering, from Argentina. I have a strong interest in autonomous robotics and computer vision, as well as in machine learning. I’m very eager to contribute, I learn quickly so wherever my skill set could be of use, I’d be happy to help!<br>
**Social Profiles**: [LinkedIn](https://www.linkedin.com/in/adiego73/), [GitHub](https://github.com/adiego73)<br>
**Email**: adiego73@gmail.com<br>

---

### Careers

[SINTEF Digital](https://candidate.hr-manager.net/ApplicationInit.aspx?cid=1131&ProjectId=144663&DepartmentId=18961&MediaId=5) (Oslo, Norway) - Research Scientist / Senior Scientist with the Machine Vision group

SINTEF is one of Europe’s largest independent research organisations. The Machine Vision group currently consists of 13 research scientists and we develop novel technologies based upon research within video, 2D, and 3D analysis and machine learning. Our projects are primarily oriented towards industrial applications and our researchers both initiate and carry out projects in close cooperation with our customers.  As part of our team you will contribute to development of new solutions within autonomy, robot vision, drone applications as well as quality control and industrial automation.  Our projects cover market segments including aquaculture, inspection, recycling, surveillance, manufacturing and space industry. Many of our customers are startups, requiring innovative solutions. Application deadline is Feb 1st!
