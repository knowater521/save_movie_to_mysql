# -*- coding: utf-8 -*-
import urllib
import urllib2
from lxml import etree
import sys


reload(sys)
sys.setdefaultencoding('utf8')

def get_tags():
    tags = []
    tag_url = 'http://movie.douban.com/tag/'
    try:
            request = urllib2.Request(tag_url, headers={
                'Connection': 'keep-alive',
                'Accept': 'image/webp,image/*,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
                'Referer': tag_url
            })
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            html_content = etree.HTML(content)

            for i in range(1, 10):
                for j in range(1, 5):
                    tag_path = '//*[@id="content"]/div/div[1]/table[1]/tbody/tr['+str(i)+']/td['+str(j)+']/a/text()'
                    tag = html_content.xpath(tag_path)
                    tags.append(tag[0])
            print("tag has got")
            return tags
    except urllib2.HTTPError, e:
            print e.code
    except urllib2.URLError, e:
            print e.reason





