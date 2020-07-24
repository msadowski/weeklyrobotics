---
title: "Weekly Robotics"
description: "In 100th(!) issue of Weekly Robotics: a simple mobile robot you could use at home, haircutting robot, two cable robots doing vastly different things and more!"
date: 2020-07-20
tags: [Robotics, Careers, Drones, MobileRobots, DIY, CableRobots, RobotArms, ConsumerRobots]
idx: 100
---
{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [Hello Robot](https://hello-robot.com)*

> Last week Grant Imahara, one of the hosts of Mythbusters, passed away. As a 90s kid, I was heavily influenced by some of his work on Mythbusters and I'm not sure if I would be where I am today without this kind of inspiration. If you would like to feel a bit nostalgic I highly recommend. [this tribiute](https://youtu.be/Px_5Z0pPlPc) from Discovery. The most clicked last week was [the Medium article on motion planning in Robotics](https://medium.com/@gunjangiri8410/motion-path-planning-in-robots-3a48cfaf58cc) with 16.1% opens.

{:.post-entry-title}
#### Ex-Googler's Startup Comes Out of Stealth With Beautifully Simple, Clever Robot Design.

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/home-robots/hello-robots-stretch-mobile-manipulator)

Stretch is a mobile robot with a 3 DoF robot arm with 2 linear joints. With a weight of 23 kg, it's certainly a robot that you could use at home and I think the simple construction is a breath of fresh air. The robot uses a Realsense D435i, that is attached to a very top of the robot, and an RPLidar A1 on the robot base level. Interestingly the robot has a mecanum wheel in the back. Traditionally I would expect a caster there. As far as I can tell browsing through [the repositories](https://github.com/hello-robot) the mecanum wheel is not actuated. If you want to dive into the repos then I recommend starting with [stretch_docs](https://github.com/hello-robot/stretch_docs) - they are very good!

{:.post-entry-title}
#### I Made a Robot to Cut My Hair with Scissors.

{:.post-source}
[YouTube (Stuff Made Here)](https://youtu.be/7zBrbdU_y0s)

Would you allow a robot to cut your hair? Shane did after building this robot. I think using limit switches instead of a depth camera is quite clever!

{:.post-entry-title}
#### Making Aerial Fiber Deployment Faster and More Efficient.

{:.post-source}
[Facebook](https://engineering.fb.com/connectivity/aerial-fiber-deployment/)

Facebook is developing a robot that can wrap custom-designed fiber cables onto an existing powerline infrastructure. The cable is cleverly folded in the way that allows keeping the COG in the same place and from the video featured in the article it seems that the early prototypes had used propellers for maintaining balance. The robot is also articulated so that it can pass any obstacles on the power lines.

{:.post-entry-title}
#### RC Car Becomes Cable Cam.

{:.post-source}
[Hackaday](https://hackaday.com/2020/07/19/rc-car-becomes-cable-cam/)

While we are on the cable robots here is how you can make your own that is equipped with an Insta360 camera.

{:.post-entry-title}
#### Sharing Pixelopolis, a Self-Driving Car Demo from Google I/O Built with TF-Lite.

{:.post-source}
[Tensorflow](https://blog.tensorflow.org/2020/07/pixelopolis-self-driving-car-demo-tensorflow-lite.html?m=1)

"Pixelopolis is an interactive installation that showcases self-driving miniature cars powered by TensorFlow Lite. Each car is outfitted with its own Pixel phone, which used its camera to detect and understand signals from the world around it. In order to sense lanes, avoid collisions and read traffic signs, the phone uses machine learning running on the Pixel Neural Core, which contains a version of an Edge TPU"

{:.post-entry-title}
#### Rosbag Snapshot.

{:.post-source}
[GitHub](https://github.com/ros/rosbag_snapshot)

If you are using ROS and would like to have more control over your bagfiles then you might find this package interesting. One of the interesting functionality is saving a fixed buffer of messages that can be a good debugging tool.

{:.post-entry-title}
#### Festo's New Bio-Inspired Robots Include a Feathery Bionic Bird.

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/festo-bioinspired-robots-bionicswift)

Here is yet another bionic robot from Festo (for some of the examples see the first paragraph of the article). This time it is a flappy wing robot that weighs 42g, uses 3 motors (one for flapping and 2 for steering). The 6g battery allows for 7 minutes of flight time.

### Sponsored

{:.post-entry-title}
#### Humble Book Bundle: Programming for Makers by Make Co.

{:.post-source}
[Humble Bundle](https://www.humblebundle.com/books/programming-for-makers-make-co-books?partner=weeklyrobotics)

Learn how to program - the Makers way, with this ebook bundle! Get books like Making Makers, AVR Programming, Make: Arduino Bots and Gadgets, Make: Linux for Makers, and more. As usual with Humble Bundle links featured by purchasing the books using the link above you can choose to support Weekly Robotics and help grow the newsletter. Thanks!
