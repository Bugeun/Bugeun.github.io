---
layout: default
title: Archive
---

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories | join: ', '" %}

{% for category in postsByCategory %}
  <h2>{{ category.name }}</h2> <!-- 카테고리 이름 출력 -->

  <ul style="list-style: none; padding: 0; margin: 0;">
    {% for post in category.items %}
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
          <span style="color: #8b949e; font-size: 0.7em; margin-right: 1em;">
            {{ post.date | date: "%Y-%m-%d" }}
          </span>
          <a href="{{ post.url }}" style="text-decoration: none; color: rgb(255, 255, 255);">
            {{ post.title }}
          </a>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
{% endfor %}
