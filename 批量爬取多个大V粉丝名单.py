# -*- coding: utf-8 -*-
#批量爬取大V粉丝名单

import ListOfFansNeedDecode as li
import pandas as pd
BigV = pd.read_excel('BigV.xlsx') #先获取大V名单，这里自定义粉丝数超过3900
BigV_list = BigV['token']

ji = 1
for i in BigV_list:
    user='{}'.format(i)
    savename='{}.csv'.format(i)
    li.zhihu().get(user=user, savename=savename)
    print('正在爬取第'+str(ji)+'个/347个 大V的粉丝名单')
    ji += 1






