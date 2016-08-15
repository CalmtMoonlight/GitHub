# -*- coding: utf-8 -*-
import datetime
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, TEXT, DateTime,CLOB,Text
from sqlalchemy.dialects.mysql import LONGTEXT
from baidu.settings import DATABASE
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import CLOB

Base = declarative_base()

def db_connect():

    return create_engine(URL(**DATABASE))

def create_news_table(engine):

    Base.metadata.create_all(engine)

def _get_date():
    return datetime.datetime.now()

class News(Base):
    """定义新闻实体"""
    __tablename__ = "baidu"
    # 主键
    id = Column(Integer, primary_key=True)
    # 爬虫key
    # crawlkey = Column('crawlkey', String(30), nullable=True)
    url = Column('url', String(500), nullable=True)
    # time = Column('time', DateTime, default=_get_date)
    html = Column('html', LONGTEXT, nullable=True)