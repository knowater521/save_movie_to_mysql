# -*- coding: utf-8 -*-
import MySQLdb
from globe_var import *
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def save_to_mysql(tag, movie_name, rate, people_num, movie_url):
    conn = MySQLdb.connect(host=mysql_info['host'], user=mysql_info['user'], passwd=mysql_info['passwd'], db=mysql_info[
        'db'], port=int(mysql_info['port']), charset='utf8')
    cur = conn.cursor()
    sql = 'insert into `movie_info`  (movie_name, movie_type, movie_score, people_num, movie_url) VALUES ("%s", "%s", "%s", "%s", "%s")'\
          % (movie_name, tag, rate, people_num, movie_url)
    cur.execute(sql)
    conn.cursor().close()
    conn.close()
