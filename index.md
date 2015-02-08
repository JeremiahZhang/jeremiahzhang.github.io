---
layout: page
title: 【直奔标竿】
tagline: Loving-Learning-Sharing
---
{% include JB/setup %}

## About Me

安静观察的阅跑者，里外如一，义无反顾，直奔标杆！——Jeremiah Zhang

[我的微博](http://weibo.com/ZhangXiaowoStef)

## 文章列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>



