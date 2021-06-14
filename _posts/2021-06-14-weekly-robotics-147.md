---
title: "Weekly Robotics"
description: "Today in WR newsletter: a DIY ROS controller, an introduction to Behavior Trees, A/B testing in robotics, MIT bipedal robot and more!"
date: 2021-06-14
tags: [Robotics, ros, control, ai, bipedal_robots, drones]
idx: 147
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")

> Last week, we've closed the 1st season of Weekly Robotics Meetups. I'm so grateful to everyone that presented. I've learned a tonne of stuff watching the presentations and talking to the presenters. Next week I'll do a quick summary of all the talks that happened since February, hopefully allowing you to pick the most interesting ones to you. If you don't want to wait then [this playlist](https://www.youtube.com/playlist?list=PL4NxwwJKGEA-LDNgkp1UPVwhu34xvhd7w) holds the first 11 videos, and the last presentation will be uploaded later this week. If you watched even one presentation I would hugely appreciate it if you could take 2 minutes to complete [this survey](https://forms.gle/fx8rg8tGp9dkUWgk7). If you have an idea for future guests when we restart in September then [please let me know](mailto:mat@weeklyrobotics.com).  As usual in the past couple of weeks, the publication of the week section is manned by [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/). The most clicked link last week was [the blog post on best engineering advice stolen from non-tech people](https://bellmar.medium.com/all-the-best-engineering-advice-i-stole-from-non-technical-people-eb7f90ca2f5f) with 19.1% opens.

{:.post-entry-title}
#### Making a ROS Controller

{:.post-source}
[Medium](https://medium.com/@mr_koz/making-a-ros-controller-720caa36abd2)

Adam Purdie had built a handheld ROS controller with some analogue controllers. The device is based on a Teensy 3.2, Raspberry Pi4 and a 7" touch screen. As the author mentions in the blog post: it looks like a great tool to have in the field. Amazingly, the project is open source and [available on GitHub](https://github.com/mrkoz/spider-controller).

----

{:.post-entry-title}
#### Introduction to Behavior Trees

{:.post-source}
[Robotics Sea Bass](https://roboticseabass.wordpress.com/2021/05/08/introduction-to-behavior-trees/)

In this blog post, Sebastian Castro does a quick introduction to Beahvior Tree concepts. If you want to start with BTs then I think Sebastian's post is a great first step.

----

{:.post-entry-title}
#### The Importance of A/B Testing in Robotics

{:.post-source}
[Google AI Blog](https://ai.googleblog.com/2021/06/the-importance-of-ab-testing-in-robotics.html)

In this blog post Researchers at Google discuss A/B testing in robotics, and how random assignment can help with environmental changes affecting the results. Big thanks to [Artur](https://github.com/ArturSkowronski/) for letting me know about this article.

----

{:.post-entry-title}
#### NASA’s Intelligent Flight Control System

{:.post-source}
[Medium](https://medium.com/geekculture/nasas-intelligent-flight-control-system-5dac0a3d3837)

A very interesting article from Rodney Rodriguez, about using AI in jetfighter control systems to create self-healing controllers.

----

{:.post-entry-title}
#### Open-PhenoLiDAR

{:.post-source}
[GitHub](https://github.com/OpenAgriTech/Open-PhenoLiDAR)

"Open PhenoLiDAR, an open-source pipeline for integrating LiDAR sensors in plant phenotyping and, more broadly, for crop monitoring applications. Open PhenoLiDAR spans from data acquisition (including instructions for integrating the LIDAR and GNSS receiver) to data analysis and obtaining primary plant traits. The data acquisition and sensor integration are developed using ROS (Robotic Operating System), which provides modularity for adopting different LiDAR models and GNSS/IMU receivers".

----

{:.post-entry-title}
#### MIT is Building a Dynamic, Acrobatic Humanoid Robot

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/humanoids/mit-dynamic-acrobatic-humanoid-robot)

MIT Researchers are building a new humanoid robot (the design in some ways reminds me of [Mini Cheetah quadruped](https://news.mit.edu/2019/mit-mini-cheetah-first-four-legged-robot-to-backflip-0304)). The publication mentioned in the article covers some very dynamic motion in simulation. I'm looking forward to the first physical prototypes!

----

{:.post-entry-title}
#### Publication of the Week - Soft Hybrid Aerial Vehicle via Bistable Mechanism (2020)

{:.post-source}
[arXiv](https://arxiv.org/abs/2011.00426)

Imagine combining the agility of hovers in tight spaces with the efficiency of fixed-wing aircraft over long distances flights. This ICRA 2021 Awards finalist paper presents a morphing hybrid aerial vehicle (HAV) that is capable of doing both without the need for extra actuators. The HAV comes with a pair of wings made with a soft material that allows them to deform between two configurations, deployed and folded. By leveraging a bistable mechanism and vehicle accelerations, it is possible to change between these two configurations. The bistable mechanism was generated by topology optimization and can maintain each mode stable with no external loads to prevent accidental mode switching.
