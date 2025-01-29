---
layout: default
title: Coding
---

{% assign postsByCategory = site.posts | group_by_exp: "Coding", "Coding.categories | join: ', '" %}

{% for category in postsByCategory %}
{% if category.name contains "Coding" %}


  <ul style="list-style: none; padding: 0; margin: 0;">
    {% for Coding in category.items %}
      <li style="margin-bottom: 0.5em;">
        {% if post.published == false %}
          <!-- 비공개 글 -->
          <span style="color: #8b949e; font-size: 0.7em; margin-right: 1em;">
            비공개
          </span>
          <span style="color: rgb(255, 255, 255);">
            {{ Coding.title }}
          </span>
        {% else %}
          <!-- 공개 글 -->
          <span style="color: #8b949e; font-size: 0.7em; margin-right: 1em;">
            {{ Coding.date | date: "%Y-%m-%d" }}
          </span>
          <a href="{{ Coding.url }}" style="text-decoration: none; color: rgb(255, 255, 255);">
            {{ Coding.title }}
          </a>
        {% endif %}
      </li>
    {% endfor %}
  </ul>

  {% endif %}
{% endfor %}

