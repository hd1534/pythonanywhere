# from . import DB as db
import os

# from datetime import datetime
# from sqlalchemy.sql import expression
# from enum import Enum

'''
class Test(db.Model):
    __tablename__ = 'test'
    idx = db.Column(db.Integer,
                    primary_key=True,
                    nullable=False,
                    autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


def add_test(name):
    db.session.add(Test(name=name))


def get_test(idx):
    return db.session.query.filter_by(idx=idx)


def get_all_test():
    return Test.query.all()


def delete_test(idx):
    db.session.delete(Test.query.filter_by(idx=idx).first())
'''


def write(data):
    f = open(os.environ['DAPP_UPLOAD_FILE'], 'w')
    f.write(data)
    f.close()


def read():
    f = open(os.environ['DAPP_UPLOAD_FILE'], 'r')
    return f.readlines()
