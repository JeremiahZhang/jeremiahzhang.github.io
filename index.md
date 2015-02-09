---
layout: page
title: 【直奔标竿】
tagline: Loving-Learning-Sharing
---
{% include JB/setup %}

## 关于

安静观察的阅跑者，里外如一，义无反顾，直奔标杆！ 
- Jeremiah Zhang

Sina微博:[@雷雨Jeremiah](http://weibo.com/ZhangXiaowoStef)

我的邮箱：zhangleisuda@foxmail.com

## 文章列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>



