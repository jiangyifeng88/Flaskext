"""
1. 登录注销功能
2. 限制用户的权限
3. 记住密码
4. 对session进行保护
"""
from flask import Blueprint
from flask_login import login_user
from requirements import User, request, render_template, redirect

from app.ext import login_manager

user_blue = Blueprint('user', __name__, template_folde='templates')


@login_manager.user_loder()
def init_user(uid):
    user = User.query.get(uid)
    return user


@user_blue.route('/login/', methods=['POST', 'GET'])
def login():
    msg = None
    if request.method == 'get':
        return render_template('login.html')
    elif request.method == 'post':
        username = request.values.get('uname')
        password = request.values.get('pwd')
        if username and password:
            try:
                user = User.query.filter(User.username == username).first()
                if user:
                    if user.password == password:
                        login_user(user)
                        return redirect('/index/')
                    else:
                        msg = '密码错误'
                else:
                    msg = '账号不存在'
            except Exception as e:
                print(e)
                msg = '网络异常'
    else:
        msg = '不支持的请求方式'
    return render_template('login.html', msg)
