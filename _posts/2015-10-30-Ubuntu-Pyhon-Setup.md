---
layout: post
category : 编程
tagline: "悦跑者"
tags : [思考]
---
{% include JB/setup %}

# Ubuntu Python 环境配置

从win转到Ubuntu 进行Pyhon学习 恩 尝试回顾走过的坑

## Go 

- 你首先参考 [在Ubuntu下配置舒服的Pyhon开发环境](http://xiaocong.github.io/blog/2013/06/18/customize-python-dev-environment-on-ubuntu/) 
	- 安装pip和virtualenv

			# 安装 pip
			sudo apt-get install python-pip
			# 安装 virtualenv
			sudo pip install virtualenv

	- 安装 git 和 gitflow
	- 安装 bash-it
	- 安装 Sublime Text 2
		- 这个你之前折腾过 [ST2与Py环境配置](https://jeremiahzhang.gitbooks.io/omooc2py/content/0MOOC/SubPy.html) 

以上 你折腾了蛮长时间 因为unix系统还不熟悉 所以尝试起来 暂时挺不顺手的 尤其在安装python的时候 后来：

- 大妈在2wd4的公开课中讲到了 pyenv 你就去尝试了 安装

		git clone https://github.com/yyuu/pyenv.git ~/.pyenv
		git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv # 配置插件
	- 然后你在 ～/.bash_profile 文件 添加 以下这些 干吗用的 猜测配置吧 你也不太清楚

			#   for PyEnv
			export PYENV_ROOT="$HOME/.pyenv"
			export PATH="$HOME/.pyenv/bin:$PATH"
			export PATH="$HOME/.pyenv/shims:$PATH"
			eval "$(pyenv init -)"

	- 而后pyenv安装python就更方便了
		
			pyenv install --list # 查看python所有版本
			pyenv virtualenv 2.7.10 # 安装python2.7.10

以上 pyenv 的确好使啊！

环境配置好了 继续[Python Star Trek](https://jeremiahzhang.gitbooks.io/omooc2py/content/) 

## 总

Ubuntu 刚上手 有点不适应 慢慢适应就好了 接下来 不用win啦 开心

星期五, 30. 十月 2015 08:10下午 


















		