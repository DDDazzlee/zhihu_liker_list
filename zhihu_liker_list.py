# -*- coding: utf-8 -*-
import random
import time
from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless")#开启无界面模式
driver=webdriver.Chrome(chrome_options=options)

#这部分不加也没关系
# headers = {
#     'Host': 'www.zhihu.com',
#     'Connection': 'keep-alive',
#     'Origin': 'https://zhuanlan.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#     'DNT': '1',
#     'Accept': '*/*',
#     'Referer': 'https://zhuanlan.zhihu.com/p/25715712?group_id=825721343365492736',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9'}
#
# #记得加cookie
# cookies = ' '

false = 'false'
true = 'true'

url = 'https://www.zhihu.com/api/v4/articles/25715712/likers?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cfollower_count%2Cgender%2Cis_followed%2Cis_following%2Cbadge&limit=10&offset={}'
#这个url是通过fiddler抓包获取（往下滑滚轮看更多点赞人信息时）
#将limit=10改为20是因为碰巧发现每页的点赞人数和这个数一样，于是就想着改一下这个数
# 改成过40、100、1000，发现都只能是每页20个点赞人信息，所以就改成20吧
#但是改成20又有重复的（每十个）

name = [] #用户名
url_token = [] #用户名
gender = [] #性别
answer_count = [] #回答问题数
follower_count = [] #粉丝数量
headline = []
ji = 1

for i in range(0,2152): #这里就用来不断翻页 如果每页翻20，1075.95/  先爬取1/3  1074/3= 358   2152
    value=10*i
    url_range=url.format(value)

    driver.get(url_range)
    s=driver.find_element_by_xpath("/html/body/pre").text #获取点赞页面的文本
    #print(s)
    s=eval(s) #将.text转为字典类型
    q=s['data']
    print('正在爬取第' + str(i) + '0/21510条记录')

    for i in q:  #获取每一条记录的我们需要的点赞人信息，其他信息不要

        if 'headline' in i: #这条判断是因为有的记录中没有headline

            name.append(i['name'])
            url_token.append(i['url_token'])

            headline.append(i['headline'].encode('UTF-8', 'ignore').decode('UTF-8'))#处理特殊字符，否则无法存入excel

            if i['gender'] == 0: #这一段代码是将性别从0，1，-1转为直观
                i['gender']='女'
                gender.append(i['gender'])
            if i['gender'] == 1:
                i['gender']='男'
                gender.append(i['gender'])
            if i['gender'] == -1:
                i['gender']='未显示'
                gender.append(i['gender'])

            answer_count.append(i['answer_count'])
            follower_count.append(i['follower_count'])
        else:
            # print(i['name'] + '  ' + str(i['url_token']) + '  ' +str('无') + '  ' + str(i['gender']) + '  '
            #       + str(i['answer_count']) + '  ' + str(i['follower_count']))
            name.append(i['name'])
            url_token.append(i['url_token'])
            headline.append('无')

            if i['gender'] == 0:
                i['gender']='女'
                gender.append(i['gender'])
            if i['gender'] == 1:
                i['gender']='男'
                gender.append(i['gender'])
            if i['gender'] == -1:
                i['gender']='未显示'
                gender.append(i['gender'])

            answer_count.append(i['answer_count'])
            follower_count.append(i['follower_count'])


        #time.sleep(random.random())#暂停随机时间，爬取进度会变慢，但是以模拟更像人以防被反爬



result={'用户名':name,'url_token':url_token,'简介':headline,'性别':gender,'回答问题数':answer_count,'粉丝数':follower_count}
results=pd.DataFrame(result) #存为数据框
results.info()


results.to_excel('点赞名单全部.xlsx', index=False, header=True) #存为excel
#results.to_csv('点赞名单全部.csv', index=False, header=True)

#接下来爬取粉丝人数较多的前几位的粉丝名单信息












