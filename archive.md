---
layout: default
title: Archive
---

<style>
  ul {
    margin-bottom: 0.5em !important;
    padding: 0 !important;
  }

  li {
    margin-top: 0.3 !important;
    margin-bottom: 0 !important;
  }

  hr {
    margin-bottom: 0.5em !important;  /* hr 간격 없애기 */
    margin-top: 0.3em !important;
    padding: 0 !important;
  }

  .category-header {
    margin-bottom: 0.7em !important; /* 카테고리 제목과 내용 간 간격 줄이기 */
  }

  .description {
    margin-top: 0em !important;
    margin-bottom: 0em !important; /* 설명과 내용 간 간격 줄이기 */
  }
</style>

<b><span style = " color: rgba(207, 203, 203, 0.48);font-size: 1.3em;margin-right: 1em;"> Vulnerability Research </span></b>
<br>
<br>
<small>Below are posts about vulnerability research</small>
<br>
<br>

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories.first" %}

{% for category in postsByCategory %}
{% if category.name != "Coding" %}
  <p style="line-height: 2em;">
  <div><b><span style="color: rgb(156, 195, 231); font-size: 1.1em;margin-right: 1.2em; margin: 0em;"> {{ category.name }} </span></b></div> 
  <hr>

  {% if category.name == "Posts" %}
  {% assign subCategories = category.items | where_exp: "post", "post.categories.size > 1" | group_by_exp: "post", "post.categories[1]" %}
  {% for subCategory in subCategories %}
  <p style="line-height: 1.5;">
  <div><b><span style="color: rgb(151, 162, 170); font-size: 0.8em; margin-left: 0.5em;margin-bottom: 0.8em;">{{ subCategory.name }}</span></b></div>

  <ul style="list-style: none; padding: 0; margin: 0;"> 
  {% for post in subCategory.items %}
  <li style="margin-bottom: 0.5em;">
  <span style="color: #8b949e; font-size: 0.8em; margin-right: 0.8em;margin-left: 0.5em;">
  {{ post.date | date: "%Y-%m-%d" }}
  </span>
  <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
  {{ post.title }}
  </a>
  </li>
  {% endfor %}
  <div><br></div>
  {% endfor %}
  </ul>
  
<!-- Writeup -->
  {% elsif category.name == "Writeup" %}
    <span style = "font-size: 0.8em;">CTF, Wargame write up focused on Pwnable and Reversing</span>
    <div><br></div>
      <ul style="list-style: none; padding: 0; margin: 0;"> 
      {% for post in category.items %}
        <li style="margin-bottom: 0.3em;">
            <span style="color: #8b949e; font-size: 0.8em; margin-right: 0.8em;">
              {{ post.date | date: "%Y-%m-%d" }}
            </span>
            <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
              {{ post.title }}
            </a>
        </li>
      {% endfor %}
        <div><br></div>
      </ul>


<!-- Analysis Reports -->
  {% elsif category.name == "Analysis Reports" %}
  {% assign subCategories = category.items | where_exp: "post", "post.categories.size > 1" | group_by_exp: "post", "post.categories[1]" %}
  {% for subCategory in subCategories %}
  <p style="line-height: 1.5;">
  <div><b><span style="color: rgb(151, 162, 170); font-size: 0.8em; margin-left: 0.5em;margin-bottom: 0.5em;margin-top: 0.5em;">{{ subCategory.name }}</span></b></div>
  
  <ul style="list-style: none; padding: 0; margin: 0.2;"> 
  {% for post in subCategory.items %}
  <li style="margin-bottom: 0.3em;">
  <span style="color: #8b949e; font-size: 0.8em; margin-right: 0.8em;margin-left: 0.5em;">
  {{ post.date | date: "%Y-%m-%d" }}
  </span>
  <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
  {{ post.title }}
  </a>
  </li>
  {% endfor %}
  <div><br></div>
  {% endfor %}
  </ul>
{% endif %}
{% endif %}
{% endfor %}
