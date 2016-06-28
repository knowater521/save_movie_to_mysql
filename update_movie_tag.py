# -*- coding: utf-8 -*-
import MySQLdb
from globe_var import *
import sys


reload(sys)
sys.setdefaultencoding('utf8')


def update_movie_tag(movie_name, tag):
    conn = MySQLdb.connect(host=mysql_info['host'], user=mysql_info['user'], passwd=mysql_info['passwd'], db=mysql_info
    ['db'], port=int(mysql_info['port']), charset='utf8')
    cur = conn.cursor()
    sql = 'select movie_type from movie_info where movie_name="%s"' % movie_name
    cur.execute(sql)
    sql_result = cur.fetchone()
    result = sql_result[0] #获取这个电影的类型
    if tag in result:
        print('已存在这个类型，不需要更新数据库')
        conn.cursor().close()
        conn.close()
        return True
    else:
        print('不存在这个类型，将存入数据库，类型用"|"分隔')
        tags = [result, tag]
        link = '|'
        new_tag = link.join(tags)
        print(new_tag)
        sql = 'update movie_info set movie_type="%s" where movie_name="%s"' % (new_tag, movie_name)
        cur.execute(sql)
        conn.cursor().close()
        conn.close()
        return True

