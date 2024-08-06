from flask import Flask, render_template, request, abort

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('page.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'zhangsan' and password == '123456':
            return 'login sucess'
        else:
            # abort的用法类似于python中的raise，在网页中主动抛出错误
            abort(404)
            return None


# 自定义错误处理方法,将404这个error与Python函数绑定
# 当需要抛出404error时，将会访问下面的代码
@app.errorhandler(404)
def handle_404_error(err):
    # return "发生了错误，错误情况是：%s"%err
    # 自定义一个界面
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
