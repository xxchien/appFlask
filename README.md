# FLASK

## 配置Linux环境

### 配置虚拟机

1. 下载VMware

   [VMware - Delivering a Digital Foundation For Businesses](https://www.vmware.com/)


### 安装Linux

1. 安装Ubuntu-LTS
   [获取Ubuntu服务器版 | Ubuntu](https://cn.ubuntu.com/download/server/step1)

2. 关于Ubantu_Linux一些命令

   1. 查看安装位置

   2. 查看有无安装


### 数据库

1. 安装mysql

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


### python

1. python3环境

   1. Linux安装python3
      ```bash
      sudo apt insatll python3
      ```

2. 配置虚拟环境
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


### git

1. git
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

### Flask

1. 配置Flask

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



---



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

### 外部服务器的访问

如果运行服务器，您会注意到只能访问服务器 来自您自己的计算机，而不是来自网络中的任何其他计算机。这是 默认值，因为在调试模式下，应用程序的用户可以执行 计算机上的任意 Python 代码。

如果禁用了调试器或信任网络上的用户， 只需将服务器添加到命令行中，即可使服务器公开可用：`--host=0.0.0.0`

```
$ flask run --host=0.0.0.0
```

这会告诉您的操作系统侦听所有公共 IP。

```bash
$ flask run --host=0.0.0.0
```

`````python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
# 配置host='0.0.0.0'使得可以连接网络中的外部服务器，而非本地
`````

### 调试模式

通过启用调试模式，如果出现以下情况，服务器将自动重新加载 代码更改，并将在浏览器中显示交互式调试器。

若要启用调试模式，请使用该选项。`--debug`

```bash
$ flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

`````python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
# 配置debug=True，使用调试模式
`````

### HTML 转义

返回 HTML（Flask 中的默认响应类型）时，任何 必须对输出中呈现的用户提供的值进行转义以保护 来自注入攻击。

`````python
from markupsafe import escape
from flask import Flask

app = Flask(__name__)
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
`````

如果用户设法提交了名称， 转义会导致它呈现为文本，而不是运行 脚本。`<script>alert("bad")</script>`

`<name>`在路由中捕获 URL 中的值并将其传递给 视图函数。下面将介绍这些可变规则。

### 路由

使用装饰器将函数绑定到 URL。

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

### 变量规则

通过用 标记部分来向 URL 添加可变部分。函数将收到关键字作为参数。

可以使用转换器来指定类型 的参数，如 .`<variable_name>``<variable_name>``<converter:variable_name>`

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

转换器类型：

| `string` | （默认）接受任何不带斜杠的文本 |
| -------- | ------------------------------ |
| `int`    | 接受正整数                     |
| `float`  | 接受正浮点值                   |
| `path    | 接受斜杠`string`               |
| `uuid`   | 接受 UUID 字符串               |

### 唯一 URL/重定向行为

以下两条规则在尾部斜杠的使用上有所不同。

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

终结点的规范 URL 具有尾部斜杠。 它类似于文件系统中的文件夹。如果您访问没有尾部斜杠，Flask会将您重定向到规范 URL 带有尾部斜杠。`projects``/projects``/projects/`

终结点的规范URL没有尾随斜线。它类似于文件的路径名。使用尾部斜杠产生 404“未找到”错误。这有帮助保持这些资源的URL唯一，这有助于搜索引擎避免将同一页面编入索引两次。`about``/about/`

### URL建设

用于生产特定函数的URl。它接受函数的名称作为其第一个参数，并接受任意数量的 关键字参数，每个参数对应于 URL 规则的变量部分。 未知变量部分将作为查询参数追加到 URL 中。

为什么要使用 URL 反转功能[``](https://flask.palletsprojects.com/en/3.0.x/api/#flask.url_for)构建 URL，而不是将它们硬编码到模板中？

1. 反转通常比对 URL 进行硬编码更具描述性。
2. 您可以一次性更改 URL，而不需要记住 手动更改硬编码的 URL。
3. URL 构建以透明方式处理特殊字符的转义。
4. 生成的路径始终是绝对的，避免了意外行为 浏览器中的相对路径。
5. 如果应用程序位于 URL 根目录之外，例如，in 而不是 ，[``](https://flask.palletsprojects.com/en/3.0.x/api/#flask.url_for)则正确地 为您处理。

通俗的来说此方法可以输出特定名称路由

```python
from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```bash
/
/login
/login?next=/
/user/John%20Doe
```

### HTTP 方法

Web 应用程序在访问 URL 时使用不同的 HTTP 方法。使用 Flask 时，应熟悉这些 HTTP 方法。默认情况下，路由仅响应 `GET` 请求。可以使用 `route()` 装饰器的 `methods` 参数来处理不同的 HTTP 方法。

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

上面的示例将一个路由的所有方法放在一个函数内，当每个部分使用一些公共数据时，这会很有用。

你也可以将不同方法的视图分离到不同的函数中。Flask 提供了快捷方式，可以使用 `get()`、`post()` 等装饰每个常见的 HTTP 方法路由。

```python
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
```

如果 `GET` 方法存在，Flask 会自动添加对 `HEAD` 方法的支持，并根据 HTTP RFC 处理请求。同样，`OPTIONS` 方法也会为你自动实现。

### 静态文件

动态 Web 应用程序也需要静态文件。这通常是 CSS 和 JavaScript 文件的来源。理想情况下，Web 服务器配置为为你提供这些文件，但在开发过程中，Flask 也可以做到这一点。只需在你的包或模块旁边创建一个名为 `static` 的文件夹，它将在应用程序上可用。

```plaintext
/static
```

要为静态文件生成 URL，请使用特殊的端点名称：`'static'`

```python
url_for('static', filename='style.css')
```

文件必须存储在文件系统中的路径为：

```plaintext
static/style.css
```

### 渲染模板

从 Python 中生成 HTML 并不是一件有趣的事情，实际上非常麻烦，因为你必须自己进行 HTML 转义以保持应用程序的安全。因此，Flask 自动为你配置了 Jinja2 模板引擎。

模板可以用于生成任何类型的文本文件。对于 Web 应用程序，主要是生成 HTML 页面，但你也可以生成 Markdown、电子邮件的纯文本以及其他任何内容。

要渲染模板，可以使用 `render_template()` 方法。你只需提供模板的名称以及要传递给模板引擎的变量作为关键字参数。以下是一个渲染模板的简单示例：

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
```

Flask 会在 `templates` 文件夹中查找模板。如果你的应用程序是一个模块，该文件夹就在模块旁边；如果是一个包，则位于包内：

情况 1：一个模块：

```
/application.py
/templates
    /hello.html
```

情况 2：一个包：

```
/application
    /__init__.py
    /templates
        /hello.html
```

对于模板，你可以使用 Jinja2 模板的全部功能。可以访问 [官方 Jinja2 模板文档](https://jinja.palletsprojects.com/en/3.0.x/templates/) 了解更多信息。

以下是一个示例模板：

```html
<!doctype html>
<title>Hello from Flask</title>
{% if person %}
  <h1>Hello {{ person }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

在模板中，你还可以访问 [`config`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.config), [`request`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.request), [`session`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.session)和 [`g`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.g) [[1\]](https://flask.palletsprojects.com/en/3.0.x/quickstart/#id3) 对象，以及 [`url_for()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.url_for) 和[`get_flashed_messages()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.get_flashed_messages) 函数。

如果使用继承，模板将特别有用。模板继承可以使每个页面保留某些元素（如头部、导航和页脚）。有关详细信息，请参阅 [模板继承](https://jinja.palletsprojects.com/en/3.0.x/templates/#template-inheritance)。

自动转义是启用的，因此如果 `person` 包含 HTML，它将自动被转义。如果你可以信任一个变量，并且你知道它将是安全的 HTML（例如，因为它来自将 wiki 标记转换为 HTML 的模块），可以使用 `Markup` 类或在模板中使用 `|safe` 过滤器将其标记为安全。访问 [Jinja 2 文档](https://jinja.palletsprojects.com/en/3.0.x/templates/#working-with-automatic-escaping) 获取更多示例。

以下是 `Markup` 类的基本介绍：

```python
from markupsafe import Markup

Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# 输出: Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

Markup.escape('<blink>hacker</blink>')
# 输出: Markup('&lt;blink&gt;hacker&lt;/blink&gt;')

Markup('<em>Marked up</em> &raquo; HTML').striptags()
# 输出: 'Marked up » HTML'
```

#### 版本变更

在 0.5 版本中发生了变化：自动转义不再对所有模板启用。以下扩展名的模板会触发自动转义：`.html`、`.htm`、`.xml`、`.xhtml`。从字符串加载的模板将禁用自动转义。

[1] 不确定 [`g`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.g) 对象是什么？它是一个可以存储您所需信息的对象。请参阅 Flask 文档中的  [`flask.g`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.g) 和 [Using SQLite 3 with Flask](https://flask.palletsprojects.com/en/3.0.x/patterns/sqlite3/)。

#### 参考

- [Flask 模板渲染文档](https://flask.palletsprojects.com/en/2.3.x/templating/)
- [flask.g 对象文档](https://flask.palletsprojects.com/en/2.3.x/api/#flask.g)
- [使用 SQLite 3 与 Flask](https://flask.palletsprojects.com/en/2.3.x/patterns/sqlite3/)

### 访问请求数据
对于 web 应用程序来说，响应客户端发送到服务器的数据至关重要。在 Flask 中，这些信息由全局[`request`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.request)对象提供。如果您有一些 Python 经验，您可能会想知道该对象如何能是全局的，以及 Flask 如何设法在这种情况下仍然保持线程安全。答案是上下文局部变量：

#### 上下文局部变量

> 内部信息:
>
> 如果您想了解其工作原理以及如何使用上下文局部变量实现测试，请阅读本节内容，否则可以跳过。

在 Flask 中，某些对象是全局对象，但不是通常意义上的全局对象。这些对象实际上是特定上下文中对象的代理。这听起来有点复杂，但其实很容易理解。

想象上下文是处理线程。一个请求进入，web 服务器决定生成一个新线程（或者其他东西，底层对象能够处理除线程之外的并发系统）。当 Flask 开始其内部请求处理时，它会发现当前线程是活动上下文，并将当前应用程序和 WSGI 环境绑定到该上下文（线程）。它以一种智能的方式进行处理，使得一个应用程序可以调用另一个应用程序而不被破坏。

这对你意味着什么？基本上，你可以完全忽略这个机制，除非你在做单元测试。你会注意到依赖于请求对象的代码突然崩溃，因为没有请求对象。解决方法是自己创建一个请求对象并将其绑定到上下文中。单元测试最简单的解决方案是使用 [`test_request_context()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.test_request_context)上下文管理器。结合 `with` 语句，它会绑定一个测试请求，以便你可以与其交互。以下是一个示例：

```python
from flask import request

with app.test_request_context('/hello', method='POST'):
    # 现在你可以在 with 块结束之前对请求进行操作，例如基本断言：
    assert request.path == '/hello'
    assert request.method == 'POST'
```

另一种可能性是将整个 WSGI 环境传递给 [`request_context()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.request_context) 方法：

```python
with app.request_context(environ):
    assert request.method == 'POST'
```

#### 请求对象

请求对象在 API 部分有详细记录，我们不会在此详细介绍（请参见 [`Request`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request)）。以下是一些最常见操作的概述。首先，你需要从模块中导入它：

```python
from flask import request
```

通过 [`method`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.method) 属性可以获得当前请求的方法。要访问表单数据（通过 `POST` 或 `PUT` 请求传输的数据），可以使用 [`form`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.form)属性。以下是上述两个属性的完整示例：

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 如果请求方法是 GET 或凭据无效，以下代码将被执行
    return render_template('login.html', error=error)
```

如果 `form` 属性中不存在该键会发生什么？在这种情况下，会引发一个特殊的 [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) 。你可以像标准  [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) 一样捕获它，但如果你不这样做，会显示一个 HTTP 400 错误页面。因此，在许多情况下，你不需要处理这个问题。

要访问 URL 中提交的参数（例如 `?key=value`），可以使用 [`args`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.args) 属性：

```python
searchword = request.args.get('key', '')
```

我们建议使用 `get` 方法访问 URL 参数，或捕获 [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) ，因为用户可能会更改 URL，在这种情况下，显示 400 错误页面对用户来说不够友好。

有关请求对象的所有方法和属性的完整列表，请参见 [`Request`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request) 。

#### 文件上传

你可以轻松地使用 Flask 处理文件上传。只需确保在 HTML 表单中设置 `enctype="multipart/form-data"` 属性，否则浏览器将不会传输文件。

上传的文件存储在内存中或文件系统的临时位置。你可以通过请求对象的 `files` 属性访问这些文件。每个上传的文件都存储在该字典中。它的行为类似于标准 Python 对象，但还具有 [`save()`](https://werkzeug.palletsprojects.com/en/3.0.x/datastructures/#werkzeug.datastructures.FileStorage.save) 方法，允许你将文件存储在服务器的文件系统上。以下是一个简单的示例，展示了如何使用它：

```python
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
```

如果你想知道文件在上传到应用程序之前在客户端的名称，可以访问 [`filename`](https://werkzeug.palletsprojects.com/en/3.0.x/datastructures/#werkzeug.datastructures.FileStorage.filename) 属性。但请记住，这个值可能被伪造，所以不要轻易相信这个值。如果你想使用客户端的文件名将文件存储在服务器上，可以通过 Werkzeug 提供的 [`secure_filename()`](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.utils.secure_filename) 函数处理它：

```python
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ...
```

有关更详细的示例，请参见 [上传文件](https://flask.palletsprojects.com/en/3.0.x/patterns/fileuploads/)。

#### Cookies

要访问 cookies，可以使用 [`cookies`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.cookies) 属性。要设置 cookies，可以使用响应对象的 [`set_cookie`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Response.set_cookie) 方法。请求对象的 [`cookies`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Request.cookies) 属性是一个字典，包含客户端传递的所有 cookies。如果你想使用会话，不要直接使用 cookies，而应使用 Flask 中的 [Sessions](https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions)，它在 cookies 上添加了一些安全措施。

读取 cookies：

```python
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # 使用 cookies.get(key) 而不是 cookies[key] 以避免在 cookie 缺失时引发 KeyError。
```

存储 cookies：

```python
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```

请注意，cookies 是在响应对象上设置的。由于你通常只是从视图函数中返回字符串，Flask 会将它们转换为响应对象。如果你希望显式地进行转换，可以使用 [`make_response()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.make_response) 函数，然后进行修改。

有时你可能希望在响应对象还不存在的情况下设置 cookie。这可以通过使用 [Deferred Request Callbacks](https://flask.palletsprojects.com/en/3.0.x/patterns/deferredcallbacks/) 模式来实现。

有关响应的更多信息，请参见 [About Responses](https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses)。

### 重定向和错误

要将用户重定向到另一个端点，使用 [`redirect()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.redirect) 函数；要提前中止请求并返回错误代码，使用 [`abort()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.abort) 函数：

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

这是一个相当无意义的示例，因为用户会从首页被重定向到一个他们无法访问的页面（401 意味着访问被拒绝），但它展示了如何操作。

默认情况下，每个错误代码都会显示一个黑白的错误页面。如果你想自定义错误页面，可以使用 [`errorhandler()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.errorhandler) 装饰器：

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

注意 `render_template()` 调用后的 `404`。这告诉 Flask 该页面的状态码应该是 404，表示未找到。默认情况下假设状态码为 200，这意味着一切正常。

有关更多详细信息，请参见 [处理应用程序错误](https://flask.palletsprojects.com/en/3.0.x/errorhandling/)。

### 关于响应

视图函数的返回值会自动转换为响应对象。如果返回值是字符串，它会被转换为一个响应对象，字符串作为响应体，状态码为默认值，MIME 类型为 `text/html`。如果返回值是字典或列表，则会调用 [`jsonify()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify) 来生成响应。Flask 将返回值转换为响应对象的逻辑如下：

1. 如果返回的是正确类型的响应对象，它将直接从视图中返回。
2. 如果返回的是字符串，则会用该数据和默认参数创建一个响应对象。
3. 如果返回的是迭代器或生成器，它返回字符串或字节，则会被视为流式响应。
4. 如果返回的是字典或列表，则会使用 [`jsonify()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify) 创建响应对象。
5. 如果返回的是一个元组，元组中的项可以提供额外的信息。这样的元组必须是以下形式之一：`(response, status)`、`(response, headers)` 或 `(response, status, headers)`。`status` 值将覆盖状态码，`headers` 可以是额外的头部值的列表或字典。
6. 如果以上都不符合，Flask 将假定返回值是一个有效的 WSGI 应用程序，并将其转换为响应对象。

如果你想在视图中获取生成的响应对象，可以使用 [`make_response()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.make_response) 函数。

假设你有一个这样的视图：

```python
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

你只需将返回表达式用 [`make_response()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.make_response) 包装起来，以获取响应对象进行修改，然后返回它：

```python
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

#### 使用 JSON 的 API

在编写 API 时，JSON 是一种常见的响应格式。使用 Flask 编写这样的 API 很简单。如果你从视图中返回一个 `dict` 或 `list`，它会被转换为 JSON 响应。

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
```

这是将数据传递给 [`jsonify()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify) 函数的快捷方式，该函数会序列化任何支持的 JSON 数据类型。这意味着 `dict` 或 `list` 中的所有数据必须是 JSON 可序列化的。

对于复杂类型，例如数据库模型，你可能需要使用序列化库来先将数据转换为有效的 JSON 类型。社区中有许多序列化库和 Flask API 扩展，支持更复杂的应用程序。

### 会话（Sessions）

除了请求对象外，还有一个名为 [`session`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.session) 的对象，它允许您在一次请求到下一次请求之间存储特定于用户的信息。这是基于 cookies 实现的，并且会对 cookies 进行加密签名。这意味着用户可以查看 cookie 的内容，但不能修改它，除非他们知道用于签名的秘密密钥。

为了使用会话，您必须设置一个秘密密钥。会话的工作方式如下：

```python
from flask import session

# 将秘密密钥设置为一些随机字节。请务必保密！
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # 如果会话中存在用户名，则将其删除
    session.pop('username', None)
    return redirect(url_for('index'))
```

如何生成好的秘密密钥

秘密密钥应该尽可能随机。您的操作系统有生成基于加密随机生成器的相当随机数据的方法。使用以下命令可以快速生成一个值（或 [`SECRET_KEY`](https://flask.palletsprojects.com/en/3.0.x/config/#SECRET_KEY)）：**Flask.secret_key**

```bash
$ python -c 'import secrets; print(secrets.token_hex())'
'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

关于基于 cookies 的会话的说明：Flask 会将您放入会话对象中的值序列化到 cookie 中。如果您发现一些值在请求之间无法持久化，cookies 已启用，并且没有清晰的错误消息，请检查页面响应中 cookie 的大小与 Web 浏览器支持的大小比较。

除了默认的客户端侧会话外，如果您想在服务器端处理会话，还可以使用一些支持此功能的 Flask 扩展。

### 消息闪现

优秀的应用程序和用户界面都注重反馈。如果用户没有得到足够的反馈，他们可能最终会讨厌这个应用程序。Flask 提供了一种非常简单的方式通过闪现系统来向用户提供反馈。闪现系统基本上使得在请求结束时记录一条消息并在下一次（且仅限下一次）请求时访问它成为可能。这通常与布局模板结合使用以显示消息。

要闪现一条消息，请使用 [`flash()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.flash) 方法，要获取这些消息，可以使用 [`get_flashed_messages()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.get_flashed_messages) 方法，该方法在模板中也可用。有关完整示例，请参见 [消息闪现](https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/)。

### 日志记录

<details class="changelog" open="" style="color: rgb(62, 67, 73); font-family: Garamond, Georgia, serif; font-size: 17px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><summary style="cursor: pointer; font-style: italic; margin-bottom: 10px;">更新日志</summary><div class="versionadded"><p style="hyphens: auto; line-height: 1.4;"><span class="versionmodified added" style="font-style: italic;">新功能于 0.3 版本添加。</span></p></div></details>

有时您可能会遇到处理的数据应该是正确的，但实际上并非如此。例如，您可能有一些客户端代码发送 HTTP 请求到服务器，但显然格式错误。这可能是由于用户篡改数据或客户端代码失败引起的。在大多数情况下，回复 `400 Bad Request` 是可以的，但有时这并不足够，代码必须继续工作。

您可能仍然希望记录下发生了一些可疑的事情。这时日志记录器就派上用场了。从 Flask 0.3 开始，日志记录器已经为您预配置好。

以下是一些示例日志调用：

```python
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

附带的 [`logger`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.logger) 是一个标准的日志记录 [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger)，有关更多信息，请查看官方 [`logging`](https://docs.python.org/3/library/logging.html#module-logging) 文档。

请参见 [处理应用程序错误](https://flask.palletsprojects.com/en/3.0.x/errorhandling/)。

### 挂钩 WSGI 中间件

要将 WSGI 中间件添加到您的 Flask 应用程序，请包装应用程序的 `wsgi_app` 属性。例如，要应用 Werkzeug 的 [`ProxyFix`](https://werkzeug.palletsprojects.com/en/3.0.x/middleware/proxy_fix/#werkzeug.middleware.proxy_fix.ProxyFix) 中间件以在 Nginx 后运行：

```python
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
```

包装 `app.wsgi_app` 而不是 `app` 意味着 `app` 仍然指向您的 Flask 应用程序，而不是中间件，因此您可以继续直接使用和配置 `app`。

### 使用 Flask 扩展

扩展是帮助您完成常见任务的软件包。例如，Flask-SQLAlchemy 提供了 SQLAlchemy 支持，使其与 Flask 一起使用变得简单易行。

有关 Flask 扩展的更多信息，请参见 [扩展](https://flask.palletsprojects.com/en/3.0.x/extensions/)。

### 部署到 Web 服务器

准备好部署您的新 Flask 应用程序了吗？请参见 [部署到生产环境](https://flask.palletsprojects.com/en/3.0.x/deploying/)。



---



##	模块化应用程序Blueprints

官方参考文档：[Modular Applications with Blueprints](https://flask.palletsprojects.com/en/3.0.x/blueprints/)

Flask 使用*蓝图*的概念来制作应用程序组件和 支持应用程序内或跨应用程序的常见模式。 蓝图可以大大简化大型应用程序的工作方式，并提供 Flask 扩展用于注册应用程序操作的中心方式。 [``](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Blueprint)对象的工作方式与[``](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask)应用程序对象类似，但它实际上不是应用程序。相反，它是关于如何构建或扩展应用程序的*蓝图*。

Flask 中的蓝图适用于以下情况：

- 将应用程序分解为一组蓝图。这是理想的 更大的应用;一个项目可以实例化一个应用程序对象， 初始化多个扩展，并注册蓝图集合。
- 在应用程序的 URL 前缀和/或子域上注册蓝图。 URL 前缀/子域中的参数成为通用视图参数 （使用默认值）跨蓝图中的所有视图函数。
- 在具有不同 URL 的应用程序上多次注册蓝图 规则。
- 提供模板筛选器、静态文件、模板和其他实用程序 通过蓝图。蓝图不必实现应用程序 或查看函数。
- 在以下情况下，在应用程序上注册任何一种情况的蓝图 初始化 Flask 扩展。

Flask 中的蓝图不是可插入的应用程序，因为它实际上不是 应用程序 – 它是一组可以在 应用，甚至多次。为什么不有多个应用程序 对象？您可以这样做（请参阅[应用程序调度](https://flask.palletsprojects.com/en/3.0.x/patterns/appdispatch/)），但是您的应用程序将具有单独的配置，并将在WSGI中进行管理层。

蓝图则在Flask级别提供分离，共享应用程序配置，并可以根据需要更改应用程序对象正在注册。缺点是**无法取消注册蓝图**一旦创建了一个应用程序，而不必破坏整个应用程序 Application 对象。

### 蓝图的概念

蓝图的基本概念是它们记录要执行的操作 在应用程序上注册时。Flask 将视图函数与 从一个端点调度请求和生成 URL 时的蓝图 到另一个。

这是一个非常基本的蓝图的样子。在这种情况下，我们想要 实现一个蓝图，用于对静态模板进行简单渲染：

```python
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# 创建一个名为'simple_page'的蓝图，并指定模板文件夹为'templates'
simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

# 定义一个路由处理函数'show'，默认页面为'index'
@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')  # 这个路由可以匹配任意页面名称
def show(page):
    try:
        # 尝试渲染'pages'文件夹下的'{page}.html'模板
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        # 如果模板未找到，则返回404错误
        abort(404)

```

当您在装饰器的帮助下绑定函数时，蓝图将记录注册在以后注册应用程序时在应用程序上运行。 此外，它还会在函数的端点前面加上提供给构造函数的蓝图的名称（在本例中也是）。蓝图的名称不修改URL，只修改端点。

### 注册蓝图

如何注册该蓝图

```python
from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
```

如果您检查应用程序上注册的规则，您会发现 这些：

```python
app.url_map
Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/' (HEAD, OPTIONS, GET) -> simple_page.show>])
```

蓝图也可以挂载到不同的位置：

```python
app.register_blueprint(simple_page, url_prefix='/pages')
```

这些是生成的规则：

```python
app.url_map
Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/pages/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/pages/' (HEAD, OPTIONS, GET) -> simple_page.show>])
```

最重要的是，您可以多次注册蓝图，但不是每次 blueprint 可能会对此做出适当的响应。事实上，这取决于 如果可以多次挂载蓝图，则实施蓝图。

#### 嵌套蓝图

可以在另一个蓝图上注册一个蓝图。

```python
parent = Blueprint('parent', __name__, url_prefix='/parent')
child = Blueprint('child', __name__, url_prefix='/child')
parent.register_blueprint(child)
app.register_blueprint(parent)
```

子蓝图将获得父蓝图的名称作为其前缀名称，子 URL 将以父 URL 的前缀为前缀。

```python
url_for('parent.child.create')
/parent/child/create
```

此外，子蓝图将获得其父蓝图的子域， 如果存在，则使用其子域作为前缀，即:

```python
parent = Blueprint('parent', __name__, subdomain='parent')
child = Blueprint('child', __name__, subdomain='child')
parent.register_blueprint(child)
app.register_blueprint(parent)

url_for('parent.child.create', _external=True)
"child.parent.domain.tld"
```

在请求函数等注册之前特定于蓝图的请求函数等 父级将为孩子触发。如果孩子没有错误 可以处理给定异常的处理程序，将尝试父级的处理程序。

### Blueprint 资源

蓝图也可以提供资源。有时您可能想要 仅针对其提供的资源引入蓝图。

#### Blueprint 资源文件夹

与常规应用程序一样，蓝图被视为已包含在文件夹中。虽然多个蓝图可以源自同一文件夹，通常不建议这样做。

该文件夹是从第二个参数推断出来的，该[`Blueprint`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Blueprint)参数是通常是 。此参数指定了 Python 的逻辑模块或包对应于蓝图。如果它指向实际 Python 包，该包（文件系统上的一个文件夹）是 资源文件夹。如果它是一个模块，则该模块包含在哪个包中 将是资源文件夹。您可以访问该属性 [`Blueprint.root_path`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Blueprint.root_path)以查看资源文件夹是什么：

```python
simple_page.root_path
'/Users/username/TestProject/yourapplication'
```

要从此文件夹中快速打开源代码，您可以使用以下 [`open_resource()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Blueprint.open_resource)函数：

```python
with simple_page.open_resource('static/style.css') as f:
    code = f.read()
```

#### 静态文件

一个蓝图可以通过提供文件系统中的文件夹路径来暴露一个包含静态文件的文件夹。该路径可以是绝对路径，也可以是相对于蓝图位置的相对路径：`static_folder`

```python
admin = Blueprint('admin', __name__, static_folder='static')
```

默认情况下，路径的最右边部分是在网络上暴露的位置。可以通过参数`static_url_path`来更改这一点。因为文件夹名在这里被称为`static`，所以它将在蓝图的 URL 前缀加上`/static`的路径下可用。如果蓝图有前缀`admin`，则静态文件的 URL 将是`/admin/static`。

端点命名为`blueprint_name.static`。你可以像使用应用程序的静态文件夹一样，使用`url_for()`来生成 URL：

```python
url_for('admin.static', filename='style.css')
```

然而，如果蓝图没有`url_prefix`，则无法访问蓝图的静态文件夹。这是因为在这种情况下，URL 将是`/static`，而应用程序的路由具有优先权。与模板文件夹不同，如果文件不存在于应用程序的静态文件夹中，蓝图的静态文件夹将不会被搜索。

#### 模板

如果你希望蓝图暴露模板，可以通过在 `Blueprint` 构造函数中提供参数 `template_folder` 来实现：

```python
admin = Blueprint('admin', __name__, template_folder='templates')
```

对于静态文件，路径可以是绝对路径，也可以是相对于蓝图资源文件夹的相对路径。

模板文件夹会被添加到模板的搜索路径中，但优先级低于实际应用程序的模板文件夹。这样，你可以轻松地在实际应用程序中覆盖蓝图提供的模板。这也意味着，如果你不希望蓝图模板被意外覆盖，请确保没有其他蓝图或实际应用程序模板具有相同的相对路径。当多个蓝图提供相同的相对模板路径时，第一个注册的蓝图优先于其他蓝图。

所以，如果你在文件夹 `yourapplication/admin` 中有一个蓝图，并且你希望渲染模板 `admin/index.html`，并且你已经提供了 `templates` 作为 `template_folder`，你将需要创建这样的文件：`yourapplication/admin/templates/admin/index.html`。额外文件夹的原因是为了避免我们的模板被实际应用程序模板文件夹中的名为 `index.html` 的模板覆盖。

为了进一步重申这一点：如果你有一个名为 `admin` 的蓝图，并且你希望渲染一个名为 `index.html` 的模板，该模板是特定于这个蓝图的，最好的做法是这样布局你的模板：

```
yourpackage/
    blueprints/
        admin/
            templates/
                admin/
                    index.html
            __init__.py
```

然后当你想要渲染模板时，使用 `admin/index.html` 作为查找模板的名称。如果你在加载正确的模板时遇到问题，启用配置变量 `EXPLAIN_TEMPLATE_LOADING`，这将指示 Flask 在每次调用时打印出它查找模板的步骤。

### 构建 URL

如果你希望从一个页面链接到另一个页面，可以像通常那样使用  [`url_for()`](https://flask.palletsprojects.com/en/3.0.x/api/#flask.url_for)  函数，只是需要在 URL 端点前面加上蓝图的名称和一个点（`.`）：

```python
url_for('admin.index')
```

此外，如果你在蓝图的视图函数或渲染的模板中，并且你想链接到同一蓝图的另一个端点，可以通过在端点前面只加一个点来使用相对重定向：

```python
url_for('.index')
```

例如，如果当前请求被分派到任何其他 `admin` 蓝图端点，这将链接到 `admin.index`。

### 蓝图错误处理器

蓝图支持像 Flask 应用对象一样的 `errorhandler` 装饰器，因此可以轻松地创建特定于蓝图的自定义错误页面。

以下是一个“404 页面未找到”异常的示例：

```python
@simple_page.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')
```

大多数错误处理器将按预期工作；然而，对于 404 和 405 异常的处理器，有一个警告。这些错误处理器仅在从适当的 `raise` 语句或调用 `abort` 时在蓝图的另一个视图函数中被调用；它们不会被无效 URL 访问触发。这是因为蓝图并不“拥有”特定的 URL 空间，因此应用实例无法知道在给定无效 URL 时应该运行哪个蓝图错误处理器。如果你希望根据 URL 前缀对这些错误执行不同的处理策略，可以在应用程序级别使用代理对象定义它们：

```python
@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(error=str(ex)), ex.code
    else:
        return ex
```

详见 [Handling Application Errors](https://flask.palletsprojects.com/en/2.3.x/errorhandling/).



---



## SQLAlchemy 统一教程

### 关于本文档

SQLAlchemy 统一教程整合了 SQLAlchemy 的 Core 和 ORM 组件，作为 SQLAlchemy 的整体介绍。对于在 1.x 系列中使用 SQLAlchemy 的用户，在 [2.0 风格](https://docs.sqlalchemy.org/en/20/glossary.html#term-2.0-style) 的工作中，ORM 使用 Core 风格的查询构造 [`select()`](https://docs.sqlalchemy.org/en/20/core/selectable.html#sqlalchemy.sql.expression.select)，并且 Core 连接和 OReM 会话之间的事务语义是等价的。请注意每个部分的蓝色边框样式，它会告诉您某个特定主题的 “ORM 风格” 程度！

已经熟悉 SQLAlchemy 的用户，尤其是那些希望将现有应用程序迁移到 SQLAlchemy 2.0 系列的用户，应查阅 [SQLAlchemy 2.0 - 主要迁移指南](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html) 文档。

对于新手来说，本文档有 **大量** 细节，但是到最后他们将被视为 **炼金术士**。

SQLAlchemy 提供了两个不同的 API，一个建立在另一个之上。这些 API 被称为 **Core** 和 **ORM**。

**SQLAlchemy Core** 是 SQLAlchemy 的基础架构，作为一个 “数据库工具包”。该库提供了管理数据库连接、与数据库查询和结果进行交互以及以编程方式构建 SQL 语句的工具。

**主要是 Core 的部分** 将不会提及 ORM。这些部分中使用的 SQLAlchemy 构造将从命名空间导入。作为主题分类的额外指示，它们还将包括 **右侧的深蓝色边框**。使用 ORM 时，这些概念仍然存在，但在用户代码中不太显式。ORM 用户应阅读这些部分，但不应期望直接使用这些 API 进行 ORM 中心代码。`sqlalchemy`

**SQLAlchemy ORM** 在 Core 的基础上提供了可选的 **对象关系映射** 功能。ORM 提供了一个额外的配置层，允许用户定义的 Python 类 **映射** 到数据库表和其他构造，以及称为 **Session** 的对象持久性机制。它然后扩展了 Core 级别的 SQL 表达语言，使得 SQL 查询可以用用户定义的对象来组成和调用。

**主要是 ORM 的部分** 应 **标题中包含 “ORM” 一词**，以明确这是一个与 ORM 相关的主题。这些部分中使用的 SQLAlchemy 构造将从命名空间导入。最后，作为主题分类的额外指示，它们还将包括 **左侧的浅蓝色边框**。Core 用户可以跳过这些部分。`sqlalchemy.orm`

**大多数** 教程部分讨论了 **也明确用于 ORM 的 Core 概念**。特别是 SQLAlchemy 2.0 在 ORM 中大大增加了 Core API 的使用。

对于每个这些部分，将有 **介绍性文本** 讨论 ORM 用户在多大程度上应期望使用这些编程模式。这些部分中使用的 SQLAlchemy 构造将从命名空间导入，并可能同时使用一些构造。作为主题分类的额外指示，这些部分还将包括 **左侧的较薄的浅色边框和右侧的较厚的深色边框**。Core 和 ORM 用户应同样熟悉这些部分中的概念。`sqlalchemy``sqlalchemy.orm`

### 教程概述

教程将按照自然的学习顺序介绍这两个概念，首先是主要以 Core 为中心的方法，然后扩展到更多 ORM 为中心的概念。

本教程的主要部分如下：

- [建立连接 - 引擎](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) - 所有 SQLAlchemy 应用程序都从一个 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine) 对象开始；这里是如何创建一个。
- [使用事务和 DBAPI](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#tutorial-working-with-transactions) - 介绍了 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine) 及其相关对象 [`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection) 和 [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result) 的使用 API。内容主要以 Core 为中心，但 ORM 用户需要熟悉至少 [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result) 对象。
- [使用数据库元数据](https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#tutorial-working-with-metadata) - SQLAlchemy 的 SQL 抽象以及 ORM 依赖于将数据库架构构造定义为 Python 对象的系统。本节介绍如何从 Core 和 ORM 角度做到这一点。
- [处理数据](https://docs.sqlalchemy.org/en/20/tutorial/data.html#tutorial-working-with-data) - 在这里我们学习如何在数据库中创建、选择、更新和删除数据。所谓的 [CRUD](https://docs.sqlalchemy.org/en/20/glossary.html#term-CRUD) 操作在这里以 SQLAlchemy Core 方式给出，并提供指向其 ORM 对应部分的链接。在 [使用 SELECT 语句](https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#tutorial-selecting-data) 中详细介绍的 SELECT 操作同样适用于 Core 和 ORM。
- [使用 ORM 处理数据](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#tutorial-orm-data-manipulation) 涵盖了 ORM 的持久性框架；基本上是插入、更新和删除的 ORM 中心方法，以及如何处理事务。
- [处理 ORM 相关对象](https://docs.sqlalchemy.org/en/20/tutorial/orm_related_objects.html#tutorial-orm-related-objects) 介绍了 [`relationship()`](https://docs.sqlalchemy.org/en/20/orm/relationship_api.html#sqlalchemy.orm.relationship) 构造的概念，并提供了如何使用它的简要概述，以及更深入文档的链接。
- [进一步阅读](https://docs.sqlalchemy.org/en/20/tutorial/further_reading.html#tutorial-further-reading) 列出了几个主要的顶级文档部分，这些部分全面记录了本教程中介绍的概念。

### 版本检查

本教程使用一个称为 [doctest](https://docs.python.org/3/library/doctest.html) 的系统编写。所有用  编写的代码片段实际上都是 SQLAlchemy 测试套件的一部分，读者可以在自己的 Python 解释器中实时使用给出的代码示例。`>>>`

如果要运行示例，建议读者进行快速检查，以验证我们使用的是 **SQLAlchemy 2.0 版本**：

```python
>>> import sqlalchemy
>>> sqlalchemy.__version__  
2.0.0
```

### 建立连接 - 引擎

每个连接到数据库的 SQLAlchemy 应用程序都需要使用一个 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine)。这一简短的章节适用于所有人。

任何 SQLAlchemy 应用程序的起点都是一个称为 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine) 的对象。这个对象充当与特定数据库连接的中央源，提供了一个工厂以及一个称为[连接池](https://docs.sqlalchemy.org/en/20/core/pooling.html)的持有空间来存储这些数据库连接。引擎通常是为特定数据库服务器创建的一次性全局对象，并使用一个 URL 字符串配置，该字符串将描述它应如何连接到数据库主机或后端。

在本教程中，我们将使用仅限内存的 SQLite 数据库。这是一种无需实际设置预先存在的数据库即可测试事物的简便方法。使用 [`create_engine()`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine) 函数创建 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine):

```
>>> from sqlalchemy import create_engine
>>> engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
```

传递给 [`create_engine`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine) 的主要参数是一个字符串 URL，如上所示，该字符串向 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine) 传达了三个重要信息：`"sqlite+pysqlite:///:memory:"`

1. 我们在与哪种数据库通信？这是上述部分，将 SQLAlchemy 链接到称为 [dialect](https://docs.sqlalchemy.org/en/20/glossary.html#term-dialect) 的对象。`sqlite`
2. 我们使用什么 [DBAPI](https://docs.sqlalchemy.org/en/20/glossary.html#term-DBAPI)？Python [DBAPI](https://docs.sqlalchemy.org/en/20/glossary.html#term-DBAPI) 是 SQLAlchemy 用来与特定数据库交互的第三方驱动程序。在这种情况下，我们使用的名称是，它在现代 Python 中使用的是 SQLite 的 [sqlite3](https://docs.python.org/library/sqlite3.html) 标准库接口。如果省略，SQLAlchemy 将使用为特定选择的数据库指定的默认 [DBAPI](https://docs.sqlalchemy.org/en/20/glossary.html#term-DBAPI)。`pysqlite`
3. 我们如何定位数据库？在这种情况下，我们的 URL 包含短语，这是一个指示模块我们将使用仅限内存的数据库的标记。这种数据库非常适合实验，因为它不需要任何服务器，也不需要创建新文件。`/:memory:``sqlite3`

懒连接

当 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine) 首次由 [`create_engine()`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine) 返回时，它实际上还没有尝试连接到数据库；只有当它第一次被要求执行数据库任务时才会发生这种情况。这是一种称为 [懒初始化](https://docs.sqlalchemy.org/en/20/glossary.html#term-lazy-initialization) 的软件设计模式。

我们还指定了一个参数 [`create_engine.echo`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine.params.echo)，它将指示 [`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine) 将其发出的所有 SQL 记录到一个 Python 记录器，该记录器将写入标准输出。此标志是一种更正式地设置 [Python 日志](https://docs.sqlalchemy.org/en/20/core/engines.html#dbengine-logging) 的简便方法，并且在脚本中进行实验时非常有用。许多 SQL 示例将包括此 SQL 日志输出，单击链接时将显示完整的 SQL 交互。`[SQL]`

### 处理事务和DBAPI

准备好[`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine)对象后，我们可以深入了解[`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine)的基本操作及其主要端点，即[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)和[`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result)。我们还会介绍ORM中这些对象的[外观模式](https://docs.sqlalchemy.org/en/20/glossary.html#term-facade)，即[`Session`](https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session)。

**针对ORM读者的说明**

在使用ORM时，[`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine)由[`Session`](https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session)管理。现代SQLAlchemy中的[`Session`](https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session)强调一种与下文讨论的[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)几乎相同的事务和SQL执行模式，因此尽管本小节主要讨论Core内容，但这里的所有概念对于ORM使用者也同样重要，推荐所有ORM学习者阅读。在本节末尾，我们将对比[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)和[`Session`](https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session)的执行模式。

由于我们尚未介绍SQLAlchemy的主要功能——SQLAlchemy表达式语言，我们将在此包中使用一个简单的构造[`text()`](https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.text)来编写SQL语句作为**文本SQL**。请放心，在日常SQLAlchemy使用中，文本SQL是例外而非常规，但它始终可用。

#### 获取连接

[`Engine`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine)的目的是通过提供一个[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)对象来连接数据库。在直接使用Core时，所有与数据库的交互都是通过[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)对象进行的。由于[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)会创建一个对数据库的开放资源，我们希望将其使用限制在特定的上下文中。最好的方法是使用Python的上下文管理器，也称为[with语句](https://docs.python.org/3/reference/compound_stmts.html#with)。下面我们使用一个文本SQL语句来显示“Hello World”。文本SQL是使用名为[`text()`](https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.text)的构造创建的，我们将在稍后详细讨论：

```python
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
    
BEGIN (implicit)
select 'hello world'
[...] ()
[('hello world',)]
ROLLBACK
```

在上面的例子中，上下文管理器创建了一个数据库连接并在事务中执行了操作。Python DBAPI的默认行为是始终有一个事务在进行；当连接被[释放](https://docs.sqlalchemy.org/en/20/glossary.html#term-released)时，会发出ROLLBACK来结束事务。事务**不会自动提交**；如果我们想提交数据，需要调用[`Connection.commit()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.commit)，我们将在下一节中看到。

提示

对于特殊情况，可以使用“自动提交”模式。[设置事务隔离级别包括DBAPI自动提交](https://docs.sqlalchemy.org/en/20/core/connections.html#dbapi-autocommit)部分讨论了这一点。

我们的SELECT的结果返回在一个名为[`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result)的对象中，稍后会详细讨论。现在我们建议最好在“连接”块内使用该对象，而不要在连接的作用域之外使用它。

#### 提交更改

我们刚刚了解到DBAPI连接不会自动提交。如果我们想提交一些数据怎么办？我们可以修改上面的例子来创建一个表，插入一些数据，然后在拥有[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)对象的块**内部**使用[`Connection.commit()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.commit)方法提交事务：

```python
# "commit as you go"
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()
    
BEGIN (implicit)
CREATE TABLE some_table (x int, y int)
[...] ()
<sqlalchemy.engine.cursor.CursorResult object at 0x...>
INSERT INTO some_table (x, y) VALUES (?, ?)
[...] [(1, 1), (2, 4)]
<sqlalchemy.engine.cursor.CursorResult object at 0x...>
COMMIT
```

在上面，我们执行了两个SQL语句，一个是“CREATE TABLE”语句[[1\]](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#id2)，另一个是参数化的“INSERT”语句（稍后在[发送多个参数](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#tutorial-multiple-parameters)中讨论参数化语法）。要提交我们在块内所做的工作，我们调用了[`Connection.commit()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.commit)方法，该方法提交事务。之后我们可以继续运行更多的SQL语句，并为这些语句再次调用[`Connection.commit()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.commit)。SQLAlchemy将这种风格称为**按需提交**。

还有另一种提交数据的方式。我们可以在一开始就声明我们的“连接”块是一个事务块。为此，我们使用[`Engine.begin()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine.begin)方法获取连接，而不是[`Engine.connect()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Engine.connect)方法。此方法将管理[`Connection`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection)的范围，并在整个块内包含一个事务，如果块成功结束则进行COMMIT，如果引发异常则进行ROLLBACK。这种风格称为**一次性开始**：

```python
# "begin once"
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )
    
BEGIN (implicit)
INSERT INTO some_table (x, y) VALUES (?, ?)
[...] [(6, 8), (9, 10)]
<sqlalchemy.engine.cursor.CursorResult object at 0x...>
COMMIT
```

你应该主要倾向于使用“一次性开始”风格，因为它更简洁并在一开始就显示了整个块的意图。然而，在本教程中我们将使用“按需提交”风格，因为它在演示目的上更灵活。

什么是“BEGIN (implicit)”？

你可能注意到事务块开始时的日志行“BEGIN (implicit)”。这里的“implicit”意味着SQLAlchemy**并未实际向数据库发送任何命令**；它只是认为这是DBAPI的隐式事务的开始。你可以注册[事件钩子](https://docs.sqlalchemy.org/en/20/core/events.html#core-sql-events)来拦截此事件，例如。

[[1](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#id1)]

[DDL](https://docs.sqlalchemy.org/en/20/glossary.html#term-DDL)指的是指示数据库创建、修改或删除模式级别结构（如表）的SQL子集。DDL（如“CREATE TABLE”）应在以COMMIT结尾的事务块中，因为许多数据库使用事务DDL，即模式更改在事务提交之前不会生效。然而，如我们稍后所见，我们通常让SQLAlchemy在更高级别的操作中为我们运行DDL序列，而无需担心COMMIT。

#### 语句执行的基础知识

我们已经看到了一些运行 SQL 语句的示例，这些示例利用了一个称为 [`Connection.execute()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.execute) 的方法，并结合一个称为 [`text()`](https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.text) 的对象，返回一个称为 [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result) 的对象。在本节中，我们将更详细地说明这些组件的机制和交互。

本节的大部分内容同样适用于现代 ORM 使用中的 [`Session.execute()`](https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.execute) 方法，该方法的工作方式与 [`Connection.execute()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.execute) 非常相似，包括 ORM 结果行也使用与核心相同的 [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result) 接口进行传递。

##### 获取行

我们将首先通过使用我们之前插入的行，运行一个针对我们创建的表的文本 SELECT 语句，更详细地说明 [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result) 对象：

```python
>>> with engine.connect() as conn:
...     result = conn.execute(text("SELECT x, y FROM some_table"))
...     for row in result:
...         print(f"x: {row.x}  y: {row.y}")
BEGIN (implicit)
SELECT x, y FROM some_table
[...] ()
x: 1  y: 1
x: 2  y: 4
x: 6  y: 8
x: 9  y: 10
ROLLBACK
```

上面的“SELECT”字符串选中了表中的所有行。返回的对象称为 [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result)，它表示结果行的可迭代对象。

[`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result) 有许多方法用于获取和转换行，例如前面说明的 [`Result.all()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result.all) 方法，它返回所有 [`Row`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Row) 对象的列表。它还实现了 Python 迭代器接口，因此我们可以直接迭代 [`Row`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Row) 对象的集合。

[`Row`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Row) 对象本身旨在像 Python [named tuples](https://docs.python.org/3/library/collections.html#collections.namedtuple) 一样工作。下面我们说明了访问行的各种方式。

- **元组赋值** - 这是最符合 Python 习惯的方式，即按位置分配变量：

  ```
  result = conn.execute(text("select x, y from some_table"))
  
  for x, y in result:
      ...
  ```

- **整数索引** - 元组是 Python 序列，因此常规整数访问也是可行的：

  ```
  result = conn.execute(text("select x, y from some_table"))
  
  for row in result:
      x = row[0]
  ```

- **属性名称** - 由于这些是 Python named tuples，因此元组具有与每一列的名称相匹配的动态属性名称。这些名称通常是 SQL 语句分配给每行列的名称。虽然它们通常是可以预测的，并且也可以通过标签进行控制，但在定义较少的情况下，它们可能会受到数据库特定行为的影响：

  ```
  result = conn.execute(text("select x, y from some_table"))
  
  for row in result:
      y = row.y
  
      # 使用 Python f-strings
      print(f"Row: {row.x} {y}")
  ```

- **映射访问** - 要将行接收为 Python **映射** 对象，这本质上是 Python 的 `dict` 对象的只读版本，可以使用 [`Result.mappings()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result.mappings) 修饰符将 [`Result`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result) 转换为 [`MappingResult`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.MappingResult) 对象；这是一个结果对象，返回类似字典的 [`RowMapping`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.RowMapping) 对象，而不是 [`Row`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Row) 对象：

  ```
  result = conn.execute(text("select x, y from some_table"))
  
  for dict_row in result.mappings():
      x = dict_row["x"]
      y = dict_row["y"]
  ```

##### 发送参数

通常，SQL 语句会伴随需要与语句本身一起传递的数据，如我们在之前的 INSERT 示例中所见。因此，[`Connection.execute()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.execute) 方法也接受参数，这些参数称为 [绑定参数](https://docs.sqlalchemy.org/en/20/glossary.html#term-bound-parameters)。一个简单的例子可能是，如果我们只想限制我们的 SELECT 语句到符合特定条件的行，例如“y”值大于传递给函数的某个值的行。

为了实现这一点，使 SQL 语句可以保持固定，并且驱动程序可以正确地清理值，我们向语句添加了一个 WHERE 条件，该条件命名了一个名为“y”的新参数；[`text()`](https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.text) 构造使用冒号格式“`:y`”来接受这些参数。然后，实际的“`:y`”值以字典形式作为第二个参数传递给 [`Connection.execute()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.execute)：

```
>>> with engine.connect() as conn:
...     result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2})
...     for row in result:
...         print(f"x: {row.x}  y: {row.y}")
BEGIN (implicit)
SELECT x, y FROM some_table WHERE y > ?
[...] (2,)
x: 2  y: 4
x: 6  y: 8
x: 9  y: 10
ROLLBACK
```

在记录的 SQL 输出中，我们可以看到绑定参数 `:y` 在发送到 SQLite 数据库时被转换为一个问号。这是因为 SQLite 数据库驱动程序使用一种称为“问号参数样式”的格式，这是 DBAPI 规范允许的六种不同格式之一。SQLAlchemy 将这些格式抽象为一种，即使用冒号的“命名”格式。

总是使用绑定参数

如本节开头所述，文本 SQL 不是我们使用 SQLAlchemy 的通常方式。然而，当使用文本 SQL 时，Python 字面值，即使是非字符串的整数或日期，也**绝不能直接转换为 SQL 字符串**；应**始终**使用参数。这是避免 SQL 注入攻击的最著名方法，当数据不受信任时尤其重要。此外，它还允许 SQLAlchemy 方言和/或 DBAPI 正确处理后端的输入。除纯文本 SQL 使用情况外，SQLAlchemy 的核心表达式 API 还确保 Python 字面值在适当情况下作为绑定参数传递。

##### 发送多个参数

在 [提交更改](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#tutorial-committing-data) 的示例中，我们执行了一个 INSERT 语句，看起来我们能够一次将多行插入数据库。对于 [DML](https://docs.sqlalchemy.org/en/20/glossary.html#term-DML) 语句，如“INSERT”、“UPDATE”和“DELETE”，我们可以通过传递一个字典列表而不是单个字典，向 [`Connection.execute()`](https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.execute) 方法发送**多个参数集**，这表明应该针对每个参数集多次调用单个 SQL 语句。这种执行方式称为 [executemany](https://docs.sqlalchemy.org/en/20/glossary.html#term-executemany)：

```
>>> with engine.connect() as conn:
...     conn.execute(
...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
...         [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
...     )
...     conn.commit()
BEGIN (implicit)
INSERT INTO some_table (x, y) VALUES (?, ?)
[...] [(11, 12),

 (13, 14)]
<sqlalchemy.engine.cursor.CursorResult object at 0x...>
COMMIT
```

上述操作相当于为每个参数集运行一次给定的 INSERT 语句，只不过操作会针对许多行进行优化以提高性能。

“execute”和“executemany”之间的一个关键行为差异是，后者不支持返回结果行，即使语句包括 RETURNING 子句。唯一的例外是在使用核心 [`insert()`](https://docs.sqlalchemy.org/en/20/core/dml.html#sqlalchemy.sql.expression.insert) 构造时，稍后在 [使用 INSERT 语句](https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html#tutorial-core-insert) 教程中介绍，该方法使用 [`Insert.returning()`](https://docs.sqlalchemy.org/en/20/core/dml.html#sqlalchemy.sql.expression.Insert.returning) 方法也表示 RETURNING。在这种情况下，SQLAlchemy 使用特殊逻辑重新组织 INSERT 语句，以便它可以针对许多行调用，同时仍然支持 RETURNING。

另请参见

[executemany](https://docs.sqlalchemy.org/en/20/glossary.html#term-executemany) - 在 [术语表](https://docs.sqlalchemy.org/en/20/glossary.html) 中，描述了 DBAPI 级别的 [cursor.executemany()](https://peps.python.org/pep-0249/#executemany) 方法，该方法用于大多数“executemany”执行。

[INSERT 语句的“插入多个值”行为](https://docs.sqlalchemy.org/en/20/core/connections.html#engine-insertmanyvalues) - 在 [处理引擎和连接](https://docs.sqlalchemy.org/en/20/core/connections.html) 中，描述了 [`Insert.returning()`](https://docs.sqlalchemy.org/en/20/core/dml.html#sqlalchemy.sql.expression.Insert.returning) 用于支持带有“executemany”执行的结果集的专用逻辑。









