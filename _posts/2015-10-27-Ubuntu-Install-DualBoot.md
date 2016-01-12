---
layout: post
section-type: post
title: ubuntu install
category: tech
tags: [ 'python' ]
---

# Ubuntu 安装 #

昨天你折腾了近8个小时的Ubuntu安装 终于将Ubuntu安装在你原系统为win7的笔记本上 并让笔记本成为了双系统 嗯Cool   
这下 你可以折腾 学习unix

## 触发 ##

win上你让cli折腾的毫无体肤 你又每天买mac     
太恼怒了 于是乎 你准备转向Unix系统试试 那么入门最好的就是Ubuntu  

Linus说：

> - Microsoft isn't evil, they just make really crappy operating systems.  
- Software is like sex: it's better when it's free.

## 安装进程 ##

- 准备阶段
	- 你确定使用USB U盘安装Ubuntu系统 所以你检测你的电脑能否是使用USB Boot[http://www.pendrivelinux.com/testing-your-system-for-usb-boot-compatibility/](http://www.pendrivelinux.com/testing-your-system-for-usb-boot-compatibility/)
	- 你进行了检测 你的电脑是`esc`进入电脑的BOOT 设置 你将先前的`CD ROM` boot修改 为USB BOOT 这样你的电脑就能使用USB U盘安装Ubuntu系统
	- 你从官网下载好Ubuntu14.04.3LTS[http://releases.ubuntu.com/14.04.3/](http://releases.ubuntu.com/14.04.3/) 
	- **Universal-USB-Installer** 下载好之后你就参考[https://help.ubuntu.com/community/Installation/FromUSBStickQuick](https://help.ubuntu.com/community/Installation/FromUSBStickQuick) 安装USB installer [http://www.pendrivelinux.com/downloads/Universal-USB-Installer](http://www.pendrivelinux.com/downloads/Universal-USB-Installer) 这样你就可将下载好的Ubuntu ISO 镜像文件 `刻录`到U盘 并将U盘作为UBS driver 驱动安装系统了
	- **分割磁盘** 在win下 你使用计算机（右击计算机）的`管理`中`磁盘管理` 对空闲的F盘进行 `压缩卷` 分隔出40G 并`删除卷`
- 安装
	- [https://help.ubuntu.com/community/WindowsDualBoot](https://help.ubuntu.com/community/WindowsDualBoot)
	- 使用USB启动安装
		- 进入 install ubuntu
		- 你选择了中文安装 嗯 其实你需要英文的呀 后来你在系统里面自己改好
		- 之后 你选择`自动分区`
		- 会显示你之前压缩的`40g`为空闲的状态
			- 因为win只能有3+1个主分区 所以压缩出来的那`40G`成为了`逻辑分区` 你对那`40G`分割形成Ubuntu挂载点的时候 需要选择`逻辑分区` 不要选择`主分区` 这样你进行为Ubuntu分区的时候 剩余的磁盘（40G的那）就不会显示不可用了 你在这里折腾了漫长时间的
		- 进行挂载点分配 (选择逻辑分区)
			- /boot 101M ext4
			- / 20G ext4
			- / home 10G ext4
			- / usr 5G ext4
			- / tmp 3G ext4
			- swap 2G
		- 一路安装就OK了
- 可选择进入系统
	- 你安装好之后 开机直接进入的是WIN7 
	- 接下来你就使用EasyBCD2.3 来修改了 你参考了
		- https://help.ubuntu.com/community/WindowsDualBoot 中启动部分Master Boot Record and Boot Manager
		- http://neosmart.net/EasyBCD/
- 修改之后 重新启动 你然可以进行选择 是进入Ubuntu还是进入Windows

----------

## 总 ##

- 安装 一定要从元知识开始 直接从Ubuntu官网进行选择 阅读
- 还是回到 元知识
- 还是回到 元知识

嗯 就这样 你可以开始Ubuntu的探索了