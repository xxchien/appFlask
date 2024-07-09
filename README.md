## 配置Linux环境

1. 下载VMware

   [VMware - Delivering a Digital Foundation For Businesses](https://www.vmware.com/)

2. 安装Ubuntu-LTS
   [获取Ubuntu服务器版 | Ubuntu](https://cn.ubuntu.com/download/server/step1)

3. 关于Ubantu_Linux一些命令

   1. 查看安装位置

   2. 查看有无安装

4. 安装mysql

   1. 卸载mysql

      ```bash
      #查看已安装的包
      apt list --installed
      #彻底卸载
      sudo apt purge mysql-*
      sudo rm -rf /etc/mysql/ /var/lib/mysql
      sudo apt autoremove
      sudo apt autoclean
      ```

      apt-get purge 与 apt-get remove是不同的，简单来说：
      purge可以将包以及软件的配置文件全部删除
      remove仅可以删除包，但不会删除配置文件

   2. 安装对应版本mysql

      ```bash
      sudo apt-get install mysql-server -y	#mysql 服务端
      sudo apt install mysql-client  -y 	#mysql 客户端
      sudo apt install libmysqlclient-dev -y #mysql 开发包
      ```

   3. 检查mysql服务是否成功启动

      ```bash
      #查看服务运行端口号
      sudo netstat -tap | grep mysql
      # 查看服务运行状态
      sudo service mysql status
      ```

   4. 启动mysql

      ```bash
      sudo service mysql start
      ```

   5. 查看默认登录用户以及密码

      ```bash
      sudo cat /etc/mysql/debian.cnf
      ```

   6. 使用查到的登录用户名和密码登录

      ```bash
      mysql -udebian-sys-maint -pRkqm8f6NHv1CYsrB
      ```

   7. 修改用户名和密码

      ```mysql
      use mysql; #切换至当前数据库
      # 把用户名称改为"test01"
      update user set user='test01' where user='debian-sys-maint';
      # 把用户test01密码改为“078683”
      alter user 'test01'@'localhost' identified with mysql_native_password by '078683';
      #查看用户和密码,plugin密码认证插件
      select user,authentication_string,plugin from user;
      #退出
      exit
      ```

   8. 重启mysql，使用新用户名和密码登录

      ```bash
      mysql -utest01 -p078683
      ```

   9. 创建新用户

      ```mysql
      use mysql
      CREATE USER 'test02'@'localhost' IDENTIFIED WITH mysql_native_password BY '078683';
      ```

   10. 删除用户

       ```mysql
       DROP USER 'test02'@'localhost';
       ```

   11. 配置开启远程访问权限

        ```mysql
       update user set host='%' where user='test02'; # 直接改表
       
       flush privileges; # 刷新
       
       GRANT ALL PRIVILEGES ON *.* TO 'test02'@'%' WITH GRANT OPTION; # 赋予任何主机访问权限：%
       
       GRANT ALL PRIVILEGES ON *.* TO 'test02'@'172.16.16.10' WITH GRANT OPTION; # 允许指定主机(IP地址)访问权限：具体ip 172.16.16.10
       
       FLUSH PRIVILEGES; # 刷新权限表
        ```

5. python3环境

   1. Linux安装python3

      ```bash
      sudo apt insatll python3
      ```

6. 配置虚拟环境
   可以使用venv，也可以使用virtualenv。一般来讲venv功能足够用了，但是virtualenv功能更加丰富。
   以下为python3-venv的创建与使用

   1. 检查有无安装python3-venv
      python3.3 之后的版本已内置了venv，安装前检查有无安装python3-venv

      ```bash
      sudo apt list --installed |grep venv
      ```

   2. 如果没有，安装python3-venv

      ```bash
      sudo apt-get update
      sudo apt-get install python3-venv
      ```

   3. 创建虚拟环境流程

      1. 切换至要创建虚拟环境的目录下

         ```bash
         cdcdcd $home
         ```

      2. 创建一个名为myenv的虚拟环境

         ```bash
         python3 -m venv myenv
         ```

   4. 激活虚拟环境
      在创建虚拟环境的文件夹中（$home)

      ```bash
      source myenv/bin/activate
      ```

   5. 退出虚拟环境

      ```bash
      deactivate
      ```

   6. 删除虚拟环境（直接删除该文件即可）

      进入虚拟环境所在位置，删除名为myenv的虚拟环境

      ```bash
      rm -rf myenv
      ```

   以下为virtualenv.

      1. 检查是否已安装virtualenv 

         ```bash
         virtualenv --version
         ```

      2. 安装virtualenv

         ```bash
         pip install virtualenv
         ```

      3. 创建文件夹

         ```bash
         mkdir my_prject
         ```

      4. 再创建的文件夹中创建环境

         ```bash
         # 创建完全与外部packages隔离的虚拟环境 myenv, python版本可能是最新的python3.8 myenv是虚拟环境名称
         virtualenv --no-site-packages myenv
          
         # 如果新的python虚拟环境也需要原来python的第三方库，可以将第三方库一起复制到新的虚拟环境
         virtualenv --system-site-packages myenv
          
         # 指定使用特定版本的Python创建虚拟环境,指定到python位置
         virtualenv -p /usr/bin/python3.8 myenv
         ```

      5. 激活虚拟环境

         ```bash
         source <环境名称>/bin/activate
         ```

      6. 退出虚拟环境

         ```bash
         deactivate
         ```

      7. 删除虚拟环境
         只需要删除创建的那个环境目录即可。在Linux或macOS上使用`rm -rf`

         ```bash
         rm -rf <环境名称>
         ```

7. git
   目前使用git，拉取代码，部署到Linux上。
   参考资料：[Git使用指南Linux](https://blog.csdn.net/weixin_44966641/article/details/119791118)

   1. 安装git

      ```bash
      sudo apt-get install git
      ```

   2. 配置用户名和邮箱名

      ```bash
      git config --global user.name "Your Name"
      git config --global user.email "email@example.com"
      ```

   3. 配置完后可以通过以下命令查看

      ```bash
      git config user.name
      git config user.email 
      ```

   4. commit

   5. 

8. 配置Flask

   1. 进入安装虚拟环境的文件

   2. 激活虚拟环境

   3. 安装Flask

      ```bash
      pip install flask
      ```

   4. 查验是否已安装

      ```bash
      pip list
      ```

      `````bash
      (myenvtest01) admin01@admin01:~/myenvtest01/bin$ pip list
      Package      Version
      ------------ -------
      blinker      1.8.2
      click        8.1.7
      Flask        3.0.3
      itsdangerous 2.2.0
      Jinja2       3.1.4
      MarkupSafe   2.1.5
      pip          24.0
      Werkzeug     3.0.3
      `````



## flask快速入门

快速入门参考flask官方手册：[Quickstart — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
其他参考资料：[Flask框架入门教程](https://blog.csdn.net/wly55690/article/details/131683846)

Flask是一个非常小的PythonWeb框架，被称为微型框架；只提供了一个稳健的核心，其他功能全部是通过扩展实现的；意思就是我们可以根据项目的需要量身定制，也意味着我们需要学习各种扩展库的使用。

### 以下内容需要掌握：

1）安装： `pip install flask`
2）组成：WSGI系统、调试、路由
3）模板引擎：Jinja2（由Flask核心开发者人员开发）
4）使用到[装饰器](https://www.cnblogs.com/ArmoredTitan/p/8878124.html)：以@开头的代码方法

### Hello, World!

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

1. 首先，我们导入了Flask类的实例。 这个类将是我们的 WSGI 应用程序。
2. 接下来，我们创建此类的实例。第一个参数是 应用程序的模块或包的名称。 是一个 方便的快捷方式适用于大多数情况。 这是必需的，以便 Flask 知道在哪里寻找资源，例如 作为模板和静态文件。`__name__`
3. 然后，我们使用route()装饰器告诉 Flask 什么 URL 应该触发我们的函数。
4. 该函数返回我们想要在用户的 浏览器。默认内容类型为 HTML，因此字符串中的 HTML 将由浏览器呈现。

