---
layout: default
title: Archive
---

<style>
  ul {
    margin: 0 !important;
    padding: 0 !important;
  }

  li {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  hr {
    margin: 0 !important;  /* hr 간격 없애기 */
    padding: 0 !important;
  }

  .category-header {
    margin-bottom: 0.1em !important; /* 카테고리 제목과 내용 간 간격 줄이기 */
  }

  .description {
    margin-top: 0.1em !important;
    margin-bottom: 0.1em !important; /* 설명과 내용 간 간격 줄이기 */
  }
</style>

<b><span style = " color: rgba(207, 203, 203, 0.48);font-size: 1.3em;margin-right: 1em;"> Vulnerability Research </span></b>
<br>
<br>
<small>Below are posts about vulnerability research</small>

<br>

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories.first" %}


{% for category in postsByCategory %}
{% if category.name != "Coding" %}
  <b><span style="color: rgb(156, 195, 231); font-size: 0.9em;margin-right: 1em;"> {{ category.name }} </span></b> <!-- 카테고리 이름 출력 -->  
  <hr>
  {% if category.name == "Research" %}
  {% assign subCategories = category.items | where_exp: "post", "post.categories.size > 1" | group_by_exp: "post", "post.categories[1]" %}
  <span style = "font-size: 0.8em;">Research for Vulnerability analysis, Exploit technique, Software internals</span>
  {% for subCategory in subCategories %}
  <b><span style="color: rgb(42, 132, 184); font-size: 0.8em; margin-left: 0.3em;">{{ subCategory.name }}</span></b>
  {% for post in subCategory.items %}
  <span style="color: #8b949e; font-size: 0.8em; margin-right: 0.8em;margin-left: 1.5em;">
  {{ post.date | date: "%Y-%m-%d" }}
  </span>
  <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
  {{ post.title }}
  {% endfor %}
  {% endfor %}
  
  {% elsif category.name == "Writeup" %}
  <span style = "font-size: 0.8em;">CTF, Wargame write up focused on Pwnable and Reversing</span>
  {% elsif category.name == "CVE-Analysis" %}
  <span style = "font-size: 0.8em;">CVE Case Study</span>
  {% elsif category.name == "Post" %}
  {% endif %}
{% endif %}
  <ul style="list-style: none; padding: 0; margin: 0;"> 
    {% for post in category.items %}
    {% unless post.categories contains "Coding" %}
    {% unless post.categories contains "Research" %}
      <li style="margin-bottom: 0.5em;">
        {% if post.published == false %}
          <!-- 비공개 글 -->
          <span style="color: #8b949e; font-size: 0.8em; margin-right: 1em;">
            비공개
          </span>
          <span style="color: rgb(255, 255, 255);">
            {{ post.title }}
          </span>
        {% else %}    
          <!-- 공개 글 -->
          <span style="color: #8b949e; font-size: 0.8em; margin-right: 0.8em;">
            {{ post.date | date: "%Y-%m-%d" }}
          </span>
          <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
            {{ post.title }}
          </a>
        {% endif %}
      </li>
      {% endunless %}
      {% endunless %}
  
  {% endfor %}
  </ul>
  <br>
{% endfor %}