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

<small>Find my <a href = "https://bugeun1007.tistory.com/category/CTF%2CWargame"><span style="color: rgb(156, 195, 231);">Writeup</span></a> of CTF/Wargame
<br>
<br>

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories.first" %}

{% for category in postsByCategory %}
  <p style="line-height: 2em;">
  
  <div><b><span style="color: rgb(156, 195, 231); font-size: 1.1em;margin-right: 1.2em; margin: 0em;"> {{ category.name }} </span></b></div> 
  <hr>

  {% if category.name == "Articles,Papers" %}
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
  

  {% endif %}
  {% endfor %}
