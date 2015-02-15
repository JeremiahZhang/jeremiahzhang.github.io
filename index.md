---
layout: page
title: 【直奔标竿】
tagline: Loving-Learning-Sharing
---
{% include JB/setup %}

## 关于我

安静观察的悦跑者，里外如一，义无反顾，直奔标竿！ 
- Jeremiah Zhang

> 心中安静，是肉体的生命 - 【箴言14：30】  

Sina微博:[@雷雨Jeremiah](http://weibo.com/ZhangXiaowoStef)

我的邮箱：zhangleisuda@foxmail.com

Favorite Movie：[Forrest Gump](http://movie.douban.com/subject/1292720/)

## 宣言

> As God is my bloody boss, I’m hell-bent on running for him. 

## 文章列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>



