from flask import Blueprint

from app.ext import cache
from flask import render_template

cache_blue = Blueprint('cache', __name__, template_folder='templates')


@cache_blue.route('/1/')
@cache.cached(timeout=60, key_prefix='')
def test():
    print('hello')
    return '111'


@cache_blue.route('/2/<name>/')
@cache.memoize(timeout=60 * 60)
def test2(name):
    print(name)
    return '2222'


@cache_blue.route('/3/')
def test3():
    return render_template('cache1.html', msg='111')
