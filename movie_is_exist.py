# -*- coding:utf-8 -*-
import MySQLdb
from globe_var import *
import sys


reload(sys)
sys.setdefaultencoding('utf8')


def movie_is_exist(movie_name):
    conn = MySQLdb.connect(host=mysql_info['host'], user=mysql_info['user'], passwd=mysql_info['passwd'],
                           db=mysql_info['db'], port=int(mysql_info['port']), charset='utf8')
    cur = conn.cursor()
    sql = 'select count(1) from movie_info where movie_name="%s"' % movie_name
    cur.execute(sql)
    result = cur.fetchone()
    conn.cursor().close()
    conn.close()
    if int(result[0]) > 0:
        return True
    else:
        return False
