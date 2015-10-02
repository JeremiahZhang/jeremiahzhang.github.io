---
layout: page
title: Renew Mind
tagline: Loving-Learning-Sharing
---
{% include JB/setup %}

## 关于我

- Jeremiah Zhang (雷雨Jeremiah)
- 成长学习中的基督徒、Long-Life Learner、阅跑者
- 关注领域：教育、机器学习、心理学
- 爱好：跑步、骑行、阅读
- Favorite Movie：[Forrest Gump](http://movie.douban.com/subject/1292720/)

> - 你要保守你心，胜过保守一切，因为一生的果效是由心发出 - 【箴言4：23】  

### 联系 ###

- Sina微博:[@雷雨Jeremiah](http://weibo.com/ZhangXiaowoStef)  
- 我的邮箱：zhangleisuda@hotmail.com

----------

## 文章列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>



