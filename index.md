---
layout: page
title: 【直奔标竿】
tagline: Loving-Learning-Sharing
---
{% include JB/setup %}

## 关于我

- Long-Life Learner 
- 关注领域：编程、人工智能、机器学习、教育

> 你要保守你心，胜过保守一切，因为一生的果效是由心发出 - 【箴言4：23】  

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



