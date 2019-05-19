---
title: "Weekly Robotics #39"
description: "This week in Weekly Robotics Newsletter we revisit Astrobee, look at machine learning course, visit mines with an underwater robot and more!"
date: 2019-05-19
tags: [Robotics, Careers, Space, ROS, IndustrialRobots, AI, DeepLearning, Drones, Sensors, MobileRobots]
---
![HeaderImage](/img/headers/39.jpg "Header image")

1) Stanford Engineers Design a Robotic Gripper for Cleaning Up Space Debris (2017).
<br>[YouTube](https://youtu.be/6hHv4li2JbY)<br>
INFO: This YouTube video shows a gecko inspired gripper created by Stanford researchers that in the future could be used for object manipulation in space and cleaning space debris.

2)A Machine Learning Course with Python.
<br>[GitHub](https://github.com/machinelearningmindset/machine-learning-course/blob/master/README.rst)<br>
INFO: The link above is a short course on Machine Learning by [Machine Learning Mindset](https://machinelearningmindset.com/). The course contains both tutorial text and Python source code.

3) The Rise of ROS.
<br>[AP News](https://www.apnews.com/Business%20Wire/091710e2474c41d19d6eb9ac1a4008f2)<br>
INFO: According to [ABI Research](https://www.abiresearch.com) nearly 55% of total commercial robots shipped in 2024, over 915,000 units, will have at least one ROS package installed.

4) Event Camera Helps Drone Dodge Thrown Objects.
<br>[IEEE](https://spectrum.ieee.org/automaton/robotics/drones/event-camera-helps-drone-dodge-thrown-objects)<br>
INFO: Researchers from [Robotics and Perception Group](http://rpg.ifi.uzh.ch/) presented dynamic obstacle avoidance on a drone allowing it to dodge a ball thrown at it at 10m/s. The drone showcased in the article uses an event camera for localization and obstacle detection and in some experiments a motion capture system is used for getting ground truth information for both a drone and the ball.

5) This Two-Wheeled RC Car Is Rather Quick.
<br>[Hackaday](https://hackaday.com/2019/05/16/this-two-wheeled-rc-car-is-rather-quick/)<br>
INFO: Compared to Bobble-Bot that we covered in the [previous issue](https://weeklyrobotics.com/weekly-robotics-38) this self-balancing platform is a simpler build when it comes to software but we still found it quite interesting and entertaining to watch. The platform is based on the [oDrive motor controller](https://odriverobotics.com/), a Teensy 3.6 micro computer and MPU6050 IMU. According to the captions in the attached video the platform is capable of driving at 40 MPH (64 Km/h).

6) Underground Robots: How Robotics Is Changing the Mining Industry.
<br>[EOS](https://eos.org/features/underground-robots-how-robotics-is-changing-the-mining-industry)<br>
INFO: This article shows couple of use cases how robotics can be used in the mining industry for searching for rare metals and free humans from needing to be exposed to danger in mines. Part of the article focuses on the [UX-1 robot](https://www.unexmin.eu/the-project/the-ux-1-robot/#tab-id-1) developed as a part of the [UNEXMiN project](https://www.unexmin.eu/the-project/project-overview-2/). UX-1 is an underwater robot with expected weight of 112 kg (247 lbs) and 0.6 m (2 ft) diameter and capable of operating at a maximum depth of 500 m.

7) Publication of the Week - Astrobee Robot Software: Enabling Mobile Autonomy on the ISS (PDF) (2018).
<br>[NASA](https://www.nasa.gov/sites/default/files/atoms/files/fluckiger2018astrobee.pdf)<br>
INFO: We mentioned Astrobee back in [Weekly Robotics #35](https://weeklyrobotics.com/weekly-robotics-35). The above paper presents the software architecture of Astrobee. Each Astrobee runs on 3 interconnected ARM processors communicating over ethernet and interfacing with 7 microcontrollers, 6 cameras, propulsion system etc. The system is composed of about 46 ROS [nodelets](http://wiki.ros.org/nodelet). The low and medium level processors run Ubuntu 16.04, while the high level one runs Android (Nougat 7.1) that is used for guest science applications developed by research partners. The system <b>does not</b> require real-time kernel extensions due to the control loop running at low speed of 62.5Hz. The system has 3 sources of localization depending on the localization mode: 120° camera, AR markers for docking or depth camera for perching. Apart from the publication we found [this talk](https://vimeo.com/292690863) by Andrew Symington to be a good summary of the software stack.

### Sponsored

1) Humble Book Bundle: Artificial Intelligence & Deep Learning by Packt.
<br>[HumbleBundle](https://www.humblebundle.com/books/artificial-intelligence-deep-learning-books?partner=weeklyrobotics)<br>
INFO: Pay what you want for those 25 books on AI & Deep Learning. By using the above link you can choose to support WeeklyRobotics and help us grow.

### Careers

1) [Aeolus Robotics](https://aeolusbot.com/careers/) (Various Countries and Remote) - Various Positions.
<br>
INFO: Founded to bring the first generation of multi-purpose robot assistants into service across the globe, Aeolus Robotics is a global company with offices in Taiwan, Poland, Austria and the USA. Integrating world-class, world-wide AI and Robot Systems genius with Taiwanese manufacturing aptitude, we are breaking new ground in general-purpose commercial-consumer robotics with capabilities in unstructured “human” spaces.

2) [Magazino](https://www.magazino.eu/apply-now/robot-qa-engineer-m-f-x/?lang=en) (Munich, Germany) - Robot QA Engineer.
<br>
INFO: Magazino develops and builds intelligent, mobile robots for intralogistics.

3) [Cobalt Robotics](https://jobs.lever.co/cobaltrobotics/1e3a394f-407f-4ec0-af1e-220401fd8b15) (San Mateo, CA, US) - Robotics Software Engineer.
<br>
INFO: Cobalt builds autonomous security robots that keep buildings safe by combining the reliability of machines and the friendly face of human-in-the-loop “Robot Specialists.”

### Announcements

1) UNEXMiN Final Conference - 26 September 2019.
<br>[UNEXMiN](https://www.unexmin.eu/unexmin-final-conference/#tab-id-1)<br>
INFO: We mentioned UNEXMiN and UX-1 robot in 6th entry of this newsletter. On 26th of September this year the project results will be presented in Belgium and you can attend the event free of charge.

2) AI in Finance Summit, New York.
<br>[RE•WORK](https://bit.ly/2JIePpy)<br>
INFO: Discover advances in AI & machine learning tools and techniques from the world's leading innovators across industry, research and the financial sector. As a media partner of the summit, Weekly Robotics readers can now get up to 40% off summit passes using discount code WR20. See the full agenda, list of speakers and registration details [here](https://bit.ly/2JIePpy). Summit passes to the Deep Learning Summit will also grant you access to the AI Assistant Summit and AI in Retail and Advertising Summit.

3) Deep Learning Summit, Europe.
<br>[RE•WORK](https://bit.ly/2VtMw00)<br>
INFO: Bridging the gap between the latest technological research advancements and real-world applications in business and society. Weekly Robotics readers can now get up to 40% off summit passes using discount code WR20. See the full agenda, list of speakers and registration details [here](https://bit.ly/2VtMw00). Summit passes to the Deep Learning Summit will also grant you access to the AI Assistant Summit and AI in Retail and Advertising Summit.
