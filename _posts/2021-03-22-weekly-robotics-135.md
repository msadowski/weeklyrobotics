---
title: "Weekly Robotics"
description: "This week in WeeklyRobotics newsletter: crab robots, self-study plan for electrical engineering, dangerous self-driving cars and more!"
date: 2021-03-22
tags: [Robotics, Drones, AutonomousCars, Courses, MobileRobots, Research]
idx: 135
---

{:.post-image}
![Issue {{page.idx}}](/img/headers/{{page.idx}}.jpg "Issue {{page.idx}}")
*Image Credit: [MIT]()*

> Last Thursday the WR Community Meeting went well and Victor Klemm made an amazingly detailed presentation on Ascento wheeled-bipedal robot. If you have missed it then you can check out the video recording [here](https://t.co/hmv1IAHl95). Huge thanks to Victor for taking the time to present his team's work and to [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/) for putting together the video recording.

----
<div class="sponsor-snippet-wrapper">
    <div class="sponsor-snippet container-fluid">
        <div class="row">
            <div class="col-3 d-none d-sm-block"></div>
                <div class="col-sm-12 col-md-6 nopadding">
                    <h3 id="spoonsored">Sponsored</h3>
                    <h4 class="post-entry-title">The Prepared</h4>
                    <span class="sponsor-source">
                        <a href="https://theprepared.org?utm_source=wr&utm_medium=email&utm_campaign=135">theprepared.org</a>
                    </span>
                <p class="sponsor-blurb">Join 10,000 designers, engineers, and operators and <a href="https://theprepared.org/newsletter?utm_source=wr&utm_medium=email&utm_campaign=135">subscribe to The Prepared</a> - your weekly email dose of logistical factoids and videos of obscure manufacturing processes. Make your Mondays a little more industrial, for free -> <a href="https://theprepared.org/newsletter?utm_source=wr&utm_medium=email&utm_campaign=135">here</a>.</p>
            </div>
        </div>
    </div>
</div>
----

{:.post-entry-title}
#### MIT’s HERMIT Crab Robots Can Do Anything You Shell Them To

{:.post-source}
[IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/mits-hermit-crab-robots-can-do-anything-you-shell-them-to)

"Ken Nakagaki, a roboticist at the MIT Media Lab, made a minor modification to the Toio robots by adding a little servo motor that can poke a pin up out of the robot’s top. It’s just a small change, but it enables all kinds of new things, since it allows the robots to drive inside of custom shells and dock with them, just like a hermit crab. But unlike any hermit crab I’ve ever seen, these shells can be endowed with clever mechanical transmission systems that leverage the robots’ motors to give them highly specialized capabilities on-demand". I can't recommend the video featured in the article enough, I found it to be very creative!

----

{:.post-entry-title}
#### My self-study plan for electrical engineering

{:.post-source}
[i-kh.net](https://i-kh.net/2021/03/20/electrical-engineering-study-plan/)

Iouri Khramtsov had come up with a plan for self-learning electrical engineering that I thought some of the readers might be interested in.

----

{:.post-entry-title}
#### Ingeniuity Testing - Coming Soon to the Planet Next to You

{:.post-source}
[Twitter](https://twitter.com/NASAPersevere/status/1373708912281542665)

It's a small drop of debris shield for the rover but a giant leap for Martian aviation? Long story short Ingenuity, the martian helicopter on-board Perseverence is fully exposed to the Martian atmosphere since yesterday's removal of the debris shield. Tomorrow [NASA had scheduled](https://mars.nasa.gov/news/8891/nasa-to-host-briefing-to-preview-first-mars-helicopter-flights/) a briefing where we will most likely learn more about the test. The helicopter flight will not happen earlier than the first week of April.

----

{:.post-entry-title}
#### Robotics Weekends

{:.post-source}
[YouTube](https://www.youtube.com/c/RoboticsWeekends/videos)

Robotics Weekends is a YouTube channel with some video only tutorials/showcases of some DIY robotics hardware and software integrations.

----

{:.post-entry-title}
#### [FSD Beta 8.2] Oakland - Close Calls, Pedestrians, Bicycles!

{:.post-source}
[YouTube (AI Addict)](https://youtu.be/antLneVlxcs)

The video above showcasing Tesla's latest "Full Self Driving" beta made quite some news [1](https://www.thedrive.com/tech/39647/tesla-admits-current-full-self-driving-beta-will-always-be-a-level-2-system-emails), [2](https://www.roadandtrack.com/news/a35878363/teslas-full-self-driving-beta-is-just-laughably-bad-and-potentially-dangerous/). In the video you will see many close calls that could potentially cause serious accidents if the driver would not take control. As much as I want Tesla to succeed I feel like calling such a system "Full Self Driving" and pushing it to some customers to test on public roads could be considered negligent. There is a [follow up video](https://youtu.be/6nr9_wBPAHs) where the same people take the car on highway 9 in Saratoga, California. The car is managing much better on this kind of road, however, there are still some near misses. For example, I noticed that around 7:10 the car does not detect an oncoming bicycle at all (or at least there doesn't seem to be a bounding box for it visible on the screen).

----

{:.post-entry-title}
#### Publication of the Week - The Driving Safety Show #20 - Michael DeKort, Autonomous Vehicles Warning (2019)

{:.post-source}
[YouTube (Driver's Alert)](https://youtu.be/z2GeDMYhTbo)

In the spirit of Autonomous Car's safety let's watch this interview Rich Sordahl interviews Michael DeKort about the state of autonomous vehicles - focusing mostly on safety, the importance of real-time operation and leveraging proper deterministic simulation tools.

----

### Announcements

{:.post-entry-title}
#### Self-Driving Cars with Duckietown

{:.post-source}
[edX](https://www.edx.org/course/self-driving-cars-with-duckietown)

On a much lighter note, the free self-driving cars with Duckietown course on edX starts today!

----

{:.post-entry-title}
#### DodgeDrone-Challenge

{:.post-source}
[Robotics and Perception Group](https://uzh-rpg.github.io/PADE-ICRA2021/ddc/)

The DodgeDrone challenge revisits the popular dodgeball game in the context of autonomous drones. Specifically, participants will have to code navigation policies to fly drones between waypoints while avoiding dynamic obstacles. Drones are fast but fragile systems: as soon as something hits them, they will crash! Since objects will move towards the drone with different speeds and accelerations, smart algorithms are required to avoid them! The competition consists of two challenges: (i) navigation in a static environment, and (ii) navigation in a dynamic environment. The navigation policy can only rely on on-board perception (dense depth, agent and goal location). These two modalitites will help participants to concentrate on different aspects of the navigation algorithm. Two environments are used for the competition: a simple and irrealistic one (which you should reserve for training and development); and a testing one consising of a photorealistic forest, where drones have to avoid the vegetation, as well as the rocks and birds that will obstruct their path.
