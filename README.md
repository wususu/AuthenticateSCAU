# 华南农业大学学生身份认证程序

--------

### 实现原理

基于正方教务系统的学生认证脚本<br/>
原理就是通过输入学号和正方系统密码模拟登录并获取学生的姓名,如过成功则为华农学生,反之不是

### 使用方法

到[1][若快打码]注册帐号<br/>
获取识别的软件Id和软件Key<br/>
在config.py中填写若快帐号,密码,软件Id和软件Key<br/>
在命令行下运行:[python3 index.py 学号 密码],若返回姓名则认证成功,0则失败


[1]:http://www.ruokuai.com/