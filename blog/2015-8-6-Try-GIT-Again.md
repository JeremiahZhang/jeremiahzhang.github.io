---
layout: post
section-type: post
title: mind models
category: Mind
tags: [ 'reading']
---
# Try Git #

自从建好自己的博客以来，就没有怎么用GIT了，只是偶尔更新文件就一直使用：  

- git add --a  
- git commit -m " add new poster"  
- git push origin master  

然后以前学得不怎么就忘记了，看来是时候建立自己的学习记录。

----------

## 资源 ##

- [安装下载](http://git-scm.com/downloads)
- Code school的[Try Git](https://try.github.io/levels/1/challenges/1)用来简单入门
- dive in
	- [Git Real](http://gitreal.codeschool.com/levels/1)
	- [廖雪峰GIT教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
	- [git book](http://git-scm.com/book/en/v2)
	- [git magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/zh_cn/index.html)
- 帮助
	- [help github](https://help.github.com/)
	- [git document](http://git-scm.com/docs)
- [学习卡片cheatsheet-1](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
- [学习卡片cheatsheet-2](http://ndpsoftware.com/git-cheatsheet.html)

----------

## GIT ##

### 什么是GIT? ###

- DVCS(Distributed Version Control System)

### Level 1 ###

- git help 不懂的命令可以直接git help 去查询
- 设置GIT
	- git config --global user.name "jeremiahzhang"
	- git config --global user.email zhangleisuda@hotmail.com
	- git config --global color.ui true  %% 设置命令行颜色
- git init：初始化GIT repository，将目录变为GIT可以管理的仓库  
    `$ mkdir gitlearn 	%% 【创建空目录】 `   
	`$ cd gitlearn	%% 【打开】`  
	`$ pwd	%% 【显示当前目录】`	  
	`$ git init ` 			
- 增加文件，比如在gitlearn文件夹中添加了README.txt文件  
    `$ git status  %% 查看最后一次commit后到目前为止有没有出现变动的地方`  
    `$ git add README.txt  `   
    `$ git status  %% check out the change`
    `$ git commit -m "creat a README"   %% 每一次commit委托给git，就相当于一次截取截图-截取（记录）时间节点`  
- 修改了文件README.txt和增加文件LICENSE  
    `$ git status`  
    `$ git add README.txt LICENSE`
    或者
    `$ git add --all  %% 增加所有修改过的和新增文件`  
    `$ git commit -m "Modify README and ADD LICENSE"`  
- 关于git add 的所有使用方法
    `$ git add <文件名列表>  %% 如git add README.txt LICENSE中 README.txt和LICENSE就是文件名列表，不用加<> `  
    `$ git add --all  %% 添加所有文件`   
    `$ git add *.txt  %% 添加当前目录下所有txt文件`
    `$ git add docs/*.txt  %% 添加docs目录中所有txt文件`
    `$ git add docs/  %% 添加docs目录中所有文件`
    `$ git add "*.txt"  %% 添加当前项目中所有txt文件`
- git log %% 使用查看记录

#### 总结-01 ####

- 设置GIT 
	- it help
	- git config
- git status的使用，查看那些更新或修改
- git add
- git commit 每一次完成修改之后，及时commit，相当于git“截图”，截取时间节点，方便以后版本回退。
- git log %% 使用查看记录
