---
layout: page
title: Archive
description: Weekly Robotic Archive.
---
<div class="hero">
	<!-- <img src="img/weeklyrobotics-hero.png" alt="Weekly Robotics">
	<small class="source">Photo by <a href="https://unsplash.com/@umby" target="_blank">Umberto</a> on Unsplash</small> -->
			<p>Weekly Robotics is a technical newsletter with handpicked news, projects (both professional and DIY) related to robotics, drones, space technologies and more. A new issue of the newsletter is published every Monday. </p>

	<div class="read-latest">
		<h4>READ OUR ARCHIVE</h4>
		<span class="read-latest-bubble">
			<a href="#archive-list">↓</a>
		</span>
	</div>
</div>

<main class="row-full">
	<section class="newsletter container">
		<div class="row">
			<div class="col-1 d-none d-sm-block"></div>
			<div class="col-sm-12 col-md-8">
				<h3 id="archive-list">ARCHIVE</h3>
				<h4 class="white">One page, every newsletter.</h4>
			</div>
		</div>
		<div class="row">
			<div class="col-2 d-none d-sm-block"></div>
			<div class="col-sm-12 col-md-8">
				{% assign postsByYearMonth = site.posts | group_by_exp:"post", "post.date | date: '%Y %b'"  %}
				{% for yearMonth in postsByYearMonth %}
				  <h3 id="yearDate">{{ yearMonth.name }}</h3>
				    <ul class="archive-list">
				      {% for post in yearMonth.items %}
				        <li><a href="{{ post.url }}">{{ post.title }}{% if post.idx %} #{{ post.idx }}{% endif %}</a></li>
				      {% endfor %}
				    </ul>
				{% endfor %}
			</div>
		</div>
	</section>
</main>
