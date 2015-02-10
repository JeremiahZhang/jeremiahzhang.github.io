---
layout: page
title: 【直奔标竿】
tagline: Loving-Learning-Sharing
---
{% include JB/setup %}

## 关于我

安静观察的悦跑者，里外如一，义无反顾，直奔标杆！ 
- Jeremiah Zhang

Sina微博:[@雷雨Jeremiah](http://weibo.com/ZhangXiaowoStef)

我的邮箱：zhangleisuda@foxmail.com

## 宣言

> As God is my bloody boss, I’m hell-bent on running for him. 

## 文章列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>



