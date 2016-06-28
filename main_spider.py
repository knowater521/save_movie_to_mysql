# -*- coding: utf-8 -*-
from get_tags import *
from get_info import *
import sys


reload(sys)
sys.setdefaultencoding('utf8')


tags = get_tags() #获取电影标签
if tags:
    # build_excel(dirs, tags) #根据标签建立相应的Excel文件
    get_info(tags)#获取评分>7 并且人数>2w的电影信息，并保存到Excel
else:
    print("mission failed")  #如果被屏蔽 拿不到tag 则任务失败




