---
title: "Weekly Robotics #131 - Perseverance Special"
description: "Perseverance and Ingenuity are on Mars and in good health! In this special issue we go through some of the most interesting details of the Mars 2020 mission. Enjoy!"
date: 2021-02-22
tags: [Robotics, Rovers, Mars, Drones, Perseverance, Ingenuity, Space]
---

{:.post-image}
![Issue {{page.idx}}](/img/features/perseverance/FLR_0000_0666952977_663ECM_T0010044AUT_04096_00_2I3J01_800.jpg "First photo from Perseverance")
*Image Credit: [NASA](https://www.nasa.gov/)*

> On Thursday last week we have held the first public Weekly Robotics meetup. We've had Kenneth Blomqvist present his iOS app for RGB-D data capture. Unfortunately, I screwed up the session recording and did not capture sound, but if you would still like to check out Kenneth slides then you will find them on [YouTube](https://youtu.be/94K0RI0a0mA). Today's issue covers the Perseverance rover in detail. Hope you will learn something new, I know I've learned a ton while researching data on this issue. Big thanks to [Rodrigo](https://www.linkedin.com/in/rodrigo-lopes-catto/) for finding and covering the papers on the cameras and microphone on the rover.

{:.post-entry-title}
#### Launch

Perseverance was launched on the 30th of July last year onboard [Atlas V](https://en.wikipedia.org/wiki/Atlas_V) rocket. Let's briefly look at the stages of the launch.

<figure>
  <img src="/img/features/perseverance/stages.jpg" alt="Atlas V - Rover Stages">
  <figcaption>Atlas stages for curiosity mission. Source: <a href="https://robohub.org/mars-science-laboratory-msl-curiosity-mars-mission/">Robohub</a></figcaption>
</figure>

As you can see in the diagram above the rover fits snuggly in the entry vehicle system. Here is how it looks like in a clean room:

<figure>
  <img src="/img/features/perseverance/25060_PIA23925-web.jpg" alt="">
  <figcaption>Entry vehicle assembly. Source: <a href="https://mars.nasa.gov/resources/25060/one-last-earthly-look/">NASA</a></figcaption>
</figure>

{:.post-entry-title}
#### Landing

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Your front-row seat to my Mars landing is here. Watch how we did it.<a href="https://twitter.com/hashtag/CountdownToMars?src=hash&amp;ref_src=twsrc%5Etfw">#CountdownToMars</a> <a href="https://t.co/Avv13dSVmQ">pic.twitter.com/Avv13dSVmQ</a></p>&mdash; NASA&#39;s Perseverance Mars Rover (@NASAPersevere) <a href="https://twitter.com/NASAPersevere/status/1363929492138254340?ref_src=twsrc%5Etfw">February 22, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The landing needs to happen autonomously. When the spacecraft is already parachuting to the landing spot the Terrain-Relative Navigation module kicks in, allowing the rover to localize itself with accuracy higher than 40 meters (130 feet). With the Terrain-Relative Navigation, the team boasts an expected landing success rate of 99% (compared to 80-85% without it). Here is how the module works according to [this page](https://mars.nasa.gov/mars2020/mission/technology/#Terrain-Relative-Navigation):

• Using images from Mars orbiters, the mission team creates a map of the landing site. <br>
• The rover stores this map in its new computer "brain," designed specifically to support Terrain-Relative Navigation.<br>
• Descending on its parachute, the rover takes pictures of the fast-approaching surface.<br>
• To figure out where it's headed, the rover quickly compares the landmarks it sees in the images to its onboard map.<br>
• Armed with the knowledge of where it’s headed, the rover searches another onboard map of safe landing zones to find the safest place it can reach. The rover can avoid dangerous ground up to about 1,100 feet (335 meters) in diameter (about the size of three football fields end-to-end), by diverting itself toward safer ground.<br>

One could think that the scientific mission begins after touch down, however, as the spacecraft enters the red planet it uses sensors both in the backshell and the heat shield to gather scientific information about the atmosphere.

The descent stage has 8 engines pointing down that will slow down the spacecraft (the parachute alone would not do the job due to the thin atmosphere. Still, the parachute will slow the vehicle down to 320 km/h (200 mph)). The jet engines are fired at about 2100 m (6,900 feet) above the ground once the rover separates from the backshell.

<figure>
  <img src="/img/features/perseverance/25609_1-PIA24428-1200.jpg" alt="">
  <figcaption>Skycrane manouver. Source: <a href="https://mars.nasa.gov/resources/25609/high-resolution-still-image-of-perseverances-landing/">NASA</a></figcaption>
</figure>


At about 20 meters from the surface, the spacecraft performs a Skycrane manoeuvre: the descent stage lowers the rover onto the surface on a set of cables. Once the rover's wheels make contact with the ground it snips the cables and the descent stage flies off to crash far away from the Rover. Here is how it looked like for Curiosity:

<figure>
  <img src="/img/features/perseverance/4406_pia16042_Sell-4SIDEBYSIDE-full2.jpg" alt="">
  <figcaption>Curiosity landing stage crash cloud. Source: <a href="https://mars.nasa.gov/resources/4406/witnessing-the-descent-stage-crash/">NASA</a></figcaption>
</figure>

If you missed the touch down moment and want to relive it, then here you go:

<iframe width="560" height="315" src="https://www.youtube.com/embed/5oyAsuviu5c?start=5238" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

One of Reddit's user also posted a wholesome video of his father reaction to the landing that I [highly recommend checking out](https://www.reddit.com/r/nextfuckinglevel/comments/lod395/man_works_from_home_on_the_perseverance_project/).

{:.post-entry-title}
#### On the ground

Now that we've landed we can enjoy some of the [imagery captured by the rover](https://mars.nasa.gov/mars2020/multimedia/raw-images/). The conventional wisdom is that anything that separates you from the ground (mattress, shoes, flooring) should be of high quality to increase your comfort. This must be true for Rovers as well as the wheels on Perseverance are so pristine:

<figure>
  <img src="/img/features/perseverance/perseverance_wheels.png" alt="">
  <figcaption>Perseverence wheels. Source: NASA</figcaption>
</figure>

Compared to Curiosity, Perseverance wheels are slightly narrower and taller. They are machined from a lightweight aluminum alloy. Each wheel has an aggressive tread composed of 48-grousers (or cleats), machined into its surface. The grousers give the rover excellent traction when driving in both soft sand and on hard rocks [Source](https://mars.nasa.gov/mars2020/spacecraft/rover/wheels/). The wheel skin is also twice as thick as Curiosity's which is a good idea given the current shape of its wheels:

<figure>
  <img src="/img/features/perseverance/curiosity_wheels.png" alt="">
  <figcaption>Curiosity wheels. Source: NASA</figcaption>
</figure>

{:.post-entry-title}
#### Cameras

The rover is equipped with 19 various cameras that are used for science mission and navigation. [This paper](https://link.springer.com/article/10.1007/s11214-020-00765-9) shared with me by Rodrigo covers them in detail. For me, the most surprising finding was that the navcams are using Sun to determine rover's attitude: "Navcam images of the sun are used to autonomously determine the sun location in the local Mars coordinate frame. The derived sun location is subsequently used by the rover FSW to determine the rover three-axis attitude. There are three primary methods to determine the vector to the sun with the Navcam: 1) sun find, 2) sun update, and 3) sun gaze. All three methods use a disk centroiding algorithm to identify the location of the Sun in a Navcam image".

I was trying to find more information about the odometry and localization in Perseverance, however, I couldn't find any sources on how it works, in case you are interested in some entry points for that then you can check out [this paper](https://onlinelibrary.wiley.com/doi/pdf/10.1002/rob.20184) that discusses visual odometry on Spirit and Opportunity rovers.

{:.post-entry-title}
#### Ingenuity

Ingenuity, the little Mars helicopter, is the part of the mission I'm currently most excited about. The helicopter already reported all-OK back to Earth. It will be attached to the bottom of Perseverance for 30-60 days and will be trickle-charged over time. Once the helicopter is deployed it will solely depend on its solar panel for charging for any further flights.

<figure>
  <img src="/img/features/perseverance/jpegPIA23882.width-1600.jpg" alt="">
  <figcaption>Ingenuity Helicopter. Source: <a href="https://www.jpl.nasa.gov/images/nasas-ingenuity-mars-helicopter">NASA/JPL</a></figcaption>
</figure>

As soon as Ingenuity is able to take off and hover over 90% of this mission goals are achieved. Best case scenario up to 4 90 second flights are going to be performed. Here is how it will look like:

<iframe width="560" height="315" src="https://www.youtube.com/embed/vnH4yD0s8QM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The guidance loops of Ingenuity run at 500Hz. On top of that, a visual odometry seems to be performed at 30Hz. The hardware choices are unprecedented as well: the system uses a cellphone-grade IMU, a laser altimeter from SparkFun and a VGA camera used for relative navigation. It also uses a cellphone grade 13 megapixel camera that will be used for documenting the flight. When flying the copter will execute a pre-defined trajectory in automatic mode [[Source](https://spectrum.ieee.org/automaton/aerospace/robotic-exploration/nasa-designed-perseverance-helicopter-rover-fly-autonomously-mars)].

The [flight stack](https://github.com/nasa/fprime) for the helicopter is called F', is open source (yay!) and is targetting Linux systems. Yes, this means that Mars became the 2nd planet that has [more computers running Linux than Windows](https://twitter.com/mikko/status/1362763793042972673).

If you want to learn more about this aircraft then you might find [this paper](https://trs.jpl.nasa.gov/bitstream/handle/2014/46229/CL%2317-6243.pdf) a good starting point. Want even more? Then [this Hackaday post](https://hackaday.com/2020/09/02/an-up-close-look-at-the-first-martian-helicopter/) has a video that shows the helicopter will be placed on the ground and if you want to see how it was tested on Earth then this media reel will be of interest:

<iframe width="560" height="315" src="https://www.youtube.com/embed/nAQxNd3uBN0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{:.post-entry-title}
#### Caching System

Perseverance's caching system is out of this world. Check for yourself:

<iframe width="560" height="315" src="https://www.youtube.com/embed/MFyv8mtRPCA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

As Adam Steltzner says in the video: "In terms of robots that go into space the sampling and caching system on Mars 2020 mission is the most complicated, most sophisticated thing that we know how to build". For more information about this system, you can check out [this Hacakday article](https://hackaday.com/2020/07/30/geocaching-on-mars-how-perseverance-will-seal-martian-samples-with-a-return-to-earth-in-mind/).

{:.post-entry-title}
#### Outro

Did you make it this far? I hope that you enjoyed this write up, even though I only skimmed over the most interesting bits. There is a lot more to the mission than I could cover in a single newsletter issue. For more information, you can browse through [Mars 2020 website](https://mars.nasa.gov/mars2020/spacecraft/instruments/) or if you want a good read about all aspects of Mars Rover then I can recommend [The Design and Engineering of Curiosity](https://www.goodreads.com/book/show/36084507-the-design-and-engineering-of-curiosity) by Emily Lakdawalla.
