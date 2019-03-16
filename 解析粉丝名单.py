
import pickle
import pandas as pd

with open('iseeisee.csv', 'rb') as f:
    all_data=pickle.load(f)
data = all_data
#print(all_data)

name = [] #用户名
url_token = [] #用户名
gender = [] #性别
answer_count = [] #回答问题数
follower_count = [] #粉丝数量
headline = [] #简介


for i in data:

    name.append(i) #i就是用户名
    url_token.append(data[i][4])
    headline.append(data[i][1].encode('UTF-8', 'ignore').decode('UTF-8'))  # 处理特殊字符，否则无法存入excel

    if data[i][0] == 0:  # 这一段代码是将性别从0，1，-1转为直观
        gender.append('女')
    if data[i][0] == 1:
        gender.append('男')
    if data[i][0] == -1:
        gender.append('未显示')

    answer_count.append(data[i][2])
    follower_count.append(data[i][3])

    #print(url_token+gender+headline+answer_count+follower_count)

result={'用户名':name,'url_token':url_token,'简介':headline,'性别':gender,'回答问题数':answer_count,'粉丝数':follower_count}
results=pd.DataFrame(result) #存为数据框
results.info()

results.to_excel('粉丝名单解析.xlsx', index=False, header=True) #存为excel
results.to_csv('粉丝名单解析.csv', index=False, header=False) #存为csv