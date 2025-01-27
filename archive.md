---
layout: default
title: Archive
---

{% assign postsByCategory = site.posts | group_by_exp: "post", "post.categories | join: ', '" %}

{% for category in postsByCategory %}
  <h2>{{ category.name }}</h2> <!-- 카테고리 이름을 출력 -->

  <ul>
    {% for post in category.items %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <small><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></small>
      </li>
    {% endfor %}
  </ul>
{% endfor %}
