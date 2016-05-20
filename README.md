# This is a simple attack framework for ctf T_T #

## python version 2.7 ##

## How to use this ##
1.  in utils there are some simple get / post func for you to build a attack method quickly
2.  in attack_method you can define your own attack function afther define it put it into methods array
3.  config something in config.py such as sumit ip, noobs' ip and so on
4.  run main.py
5.  you do not need restart the server after you define a new attack method, it will automatically load the new func in next 30 seconds round.
6.  valid flags will be saved in config.flag_log_path
7.  attack log will be saved in config.req_log_path


## TBD ##
1.  use reg to detect service log to attack backT_T


## 漏洞经验总结 ##
这里总结一下上次0ctf的web题目的反思
0ctf的web题目给出的是一个博客系统,可以发布文章,发表评论等等,py写的.

### 找到flag ###
主要有两方面,
第一个方面是快速的代码review,获得程序可以远程执行命令或者可以远程查看文件的办法,从而读取flag文件并返回.
1.  依赖的库的bug，crash之后可以远程执行shell.
2.  程序本身可以读取文件.
3.  程序可以上传文件，之后可以被远程call这个文件，从而形成调用.

第二个是快速的流量分析：
1.  看别人怎么打我们，然后反打回去T_T.
2.  调用别人在别人服务器上种下猥琐东西.

### 打挂别人的服务器 ###
1.  采用的web框架本身的一些猥琐handler.
2.  依赖的一些库之中可以传入非法值造成crash.
3.  服务器的逻辑编写有问题，就是bug造成crash.
4.  web本身的漏洞，比如cookie种的不合理等等问题.

