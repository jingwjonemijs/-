部署”我们的故事”爱情的小网站教程
1，这个源码的功能：记录在一起的日期，相片墙，留言评论，我们的计划，时光记录。
2，都添加了防止cc攻击ip记录和xxs攻击和sql注入的漏洞功能。
3，先有一台服务器，国内和国外都可以，然后链接自己的服务器，安装一下宝塔，宝塔只需要安装Mysql相关的服务器，其他的服务器都可以不用安装。
4，这里需要自己这边一个二级免费的域名绑定自己的服务器ip。
5，然后服务器安装python3.8版本的，我这里的是centos7，所有根据教程，Centos7安装Python3.8详细教程_centos7.9安装python38-CSDN博客，自己安装即可。
6，下载网站源码压缩包，上传到服务器网站目录里面，再www/wwwroot即可，然后解压压缩包里面有一个requirements.txt，然后一键安装命令：pip install -r requirements.txt，如果出现错误，去除后面的版本号即可。
在服务器的mysql，新建一个数据库，新建完成之后，在源码的目录：cdfs\love_site\settings.py这里面有一个修改mysql服务器的代码
![image](https://github.com/user-attachments/assets/c79ad577-fd7f-4828-9029-caaf59349226)

8，在源码的根目录：cdfs这里，执行一下python manage.py createsuperuser，这个是设置后台管理员的账号和密码。
![image](https://github.com/user-attachments/assets/6adfcf81-fee6-4453-b352-ebb3457d09a2)

9，然后在执行python manage.py makemigrations，然后在执行：python manage.py migrate ，在执行：python manage.py collectstatic，最后执行：python manage.py runserver 0.0.0.0:8000即可。
10，后台在：http://网站:8000/admin，登录网站，设置你的QQ账号和名称，对方的QQ账号和名称。
