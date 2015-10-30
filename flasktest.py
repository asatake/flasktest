#! /usr/bin/python
# ! -*- coding: utf-8 -*-
__author__ = 'asatake'

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.navigation import Navigation
import datetime
import os

app = Flask(__name__)
nav = Navigation()
nav.init_app(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('About', 'about'),
    nav.Item('Link', 'link'),
])


# return my age
def old():
    d1 = datetime.date.today()
    d2 = datetime.date(1994, 2, 11)
    comp = (d1 - d2)
    s = str(comp).split()[0]
    return int(s) // 365


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name, title='Top')


@app.route('/about')
def about():
    return render_template('about.html', title='About', howold=old())


@app.route('/link')
def link():
    return render_template('link.html', title='Link')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port)
