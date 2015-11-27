---
layout: page
title: Renew Mind
tagline: Loving-Learning-Sharing
---
{% include JB/setup %}

## 关于我

- Jeremiah Zhang (雷雨Jeremiah)
	- 基督徒
	- 阅跑者
	- 向黑客学习
- 关注领域
	- 教育
	- 心理学
	- Machine Learning
- 爱好
	- 跑步
	- 骑行
	- 阅读
	- 编程
- 警醒
	
> 你要保守你心，胜过保守一切，因为一生的果效是由心发出 - 【箴言4：23】  

### 联系 ###

- 邮箱: zhangleisuda@gmail.com   
- Github: [@Jeremiahzhang](https://github.com/JeremiahZhang)    
- 微博:[@雷雨Jeremiah](http://weibo.com/ZhangXiaowoStef)    
- 豆瓣: [雷雨Jeremiah](http://www.douban.com/people/jesuslovingyou/) 


***

## (￣▽￣) 
[如何成为一名黑客](http://translations.readthedocs.org/en/latest/hacker_howto.html#id3)
> 你必须建立对于自己学习能力的信念——就算你掌握的知识不足以解决当前的问题，如果你从问题的一小部分下手并从中学习，你将学到足够的知识用来解决下一部分——以此类推，直到整个问题都被你解决为止。

[The Glider: A Universal Hacker Emblem ](http://www.catb.org/~esr/hacker-emblem/)

![Glider](http://www.catb.org/~esr/hacker-emblem/glider.png)
----------

## 文章列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>



