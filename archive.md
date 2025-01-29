---
layout: default
title: Archive
---


<b><span style = " color: rgba(207, 203, 203, 0.48);font-size: 1.3em;margin-right: 1em;"> Vulnerability Research </span></b>
<br>
<small>Explain me what like to do <br>Ex) Esspecialiy(Major in) Software vulnerability analysis, Binary exploitation,  Reversing...bla</small>

<br>

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories | join: ', '" %}

{% for category in postsByCategory %}
{% if category.name != "Coding" %}
  <b><span style="color: rgb(156, 195, 231); font-size: 0.9em;margin-right: 1em;"> {{ category.name }} </span></b> <!-- 카테고리 이름 출력 -->  
  <hr>
{% endif %}
  <ul style="list-style: none; padding: 0; margin: 0;"> 
    {% for post in category.items %}
    {% unless post.categories contains "Coding" %}
      <li style="margin-bottom: 0.5em;">
        {% if post.published == false %}
          <!-- 비공개 글 -->
          <span style="color: #8b949e; font-size: 0.7em; margin-right: 1em;">
            비공개
          </span>
          <span style="color: rgb(255, 255, 255);">
            {{ post.title }}
          </span>
        {% else %}
          <!-- 공개 글 -->
          <span style="color: #8b949e; font-size: 0.7em; margin-right: 0.8em;">
            {{ post.date | date: "%Y-%m-%d" }}
          </span>
          <a href="{{ post.url }}" style="font-size: 0.8em; text-decoration: none; color: rgb(255, 255, 255);">
            {{ post.title }}
          </a>
        {% endif %}
      </li>
      {% endunless %}
  
  {% endfor %}
  </ul>
  <br>
{% endfor %}
