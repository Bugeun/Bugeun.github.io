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

<b><span style = " color: rgba(207, 203, 203, 0.48);font-size: 1.3em;margin-right: 1em;"> Research Publications </span></b>
<br>
<br>
<small>Below is summary of vulnerability research</small>
<br>
<p style="line-height: 2;">

<small>Find my <span style="color: rgb(156, 195, 231);">Writeup</span> of CTF/Wargame on => </small>
<small><a href = "https://bugeun1007.tistory.com/category/CTF%2CWargame"> Here</a></small>
<br>
<br>

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories.first" %}

{% for category in postsByCategory %}
{% if category.name != "Coding" and category.name != "Vulnerability Reports" %}
  <p style="line-height: 2em;">
  
  <div><b><span style="color: rgb(156, 195, 231); font-size: 1.1em;margin-right: 1.2em; margin: 0em;"> {{ category.name }} </span></b></div> 
  <hr>

  {% if category.name == "Blog" %}
      <ul style="list-style: none; padding: 0; margin: 0;"> 
      {% for post in category.items %}
        <li style="margin-bottom: 0.3em;">
            <span style="color: #8b949e; font-size: 0.8em; margin-right: 0.8em;margin-left: 0em;">
              {{ post.date | date: "%Y-%m-%d" }}
            </span>
            <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
              {{ post.title }}
            </a>
        </li>
      {% endfor %}
        <div><br></div>
      </ul>
  
<!-- Writeup -->
  {% elsif category.name == "Writeup" %}
    <span style = "font-size: 0.8em; margin-left: 0em;">CTF, Wargame write up focused on Pwnable and Reversing</span>
    <p style="line-height: 1.5;">
      <ul style="list-style: none; padding: 0; margin: 0;"> 
      {% for post in category.items %}
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
      </ul>
{% endif %}
{% endif %}
{% endfor %}

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories.first" %}

{% for category in postsByCategory %}
{% if category.name != "Coding" and category.name != "Blog" %}
  <p style="line-height: 2em;">
  
  <div><b><span style="color: rgb(156, 195, 231); font-size: 1.1em;margin-right: 1.2em; margin: 0em;"> {{ category.name }} </span></b></div> 
  <hr>

{% if category.name == "Vulnerability Reports" %}
      <ul style="list-style: none; padding: 0; margin: 0;"> 
      {% for post in category.items %}
      {% if category.name != "Coding" and category.name != "Blog" %}
        <li style="margin-bottom: 0.3em;">
            <span style="color: #8b949e; font-size: 0.8em; margin-right: 0.8em;margin-left: 0em;">
              {{ post.date | date: "%Y-%m-%d" }}
            </span>
            <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
              {{ post.title }}
            </a>
        </li>
        {% endif %}
      {% endfor %}
<div><br></div>
</ul>
{% endif %}
{% endif %}
{% endfor %}
