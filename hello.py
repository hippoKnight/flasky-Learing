#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'TDSS'
__mtime__ = '2017/5/10'
# code is far away from bugs with the god animal protecting
    One should love animals, they are so tasty!
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   ☃   ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃神兽保佑 ┣┓
              ┃永无BUG！ ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


# 定义一个表 tablename表名，不定义的话SQLALCHEMY会使用一个默认的名字。
# 名字是原名的小写，camelCamel->camel_camel
# 各属性是Column类的实例
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # add property 'role' for class 'User'
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

admin_role = Role(name='rAdmin')
mod_role = Role(name='rModerator')
user_role = Role(name='rUser')

user_john = User(username='John', role=admin_role)
user_susan = User(username='Susan', role=mod_role)
user_david = User(username='David', role=user_role)
