# -*- coding: utf-8 -*-
from baidu.models import News, db_connect, create_news_table
from sqlalchemy.orm import *        #sessionmaker

import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item


class NewsDatabasePipeline(object):
    """保存新闻到数据库"""

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_news_table(engine)
        # 初始化对象属性Session为可调用对象
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        self.recent_links = []
        self.nowtime = datetime.datetime.now()

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        # _log.info('open_spider[%s]....' % spider.name)
        # session = self.Session()
        # recent_news = session.query(News).filter(
        #     News.crawlkey == spider.name,
        #     self.nowtime - News.pubdate <= datetime.timedelta(days=30)).all()
        # self.recent_links = [t.link for t in recent_news]
        # _log.info(self.recent_links)
        pass

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        # 每次获取到Item调用这个callable，获得一个新的session
        # _log.info('mysql->%s' % item['link'])
        if item['url'] not in self.recent_links:
            # with scoped_session(self.Session) as session:
            #     news = News(**item)
            #     session.add(news)
            #     session.commit()
            #     self.recent_links.append(item['url'])

            session= scoped_session(self.Session)
            news = News(**item)
            session.add(news)
            session.commit()
            self.recent_links.append(item['url'])
        # news = News(**item)
        # self.session.add(news)
        # self.session.commit()
        return item

    def close_spider(self, spider):
        pass