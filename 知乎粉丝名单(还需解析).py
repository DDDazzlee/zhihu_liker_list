# 知乎用户粉丝信息爬虫

import os
import json
import time
import pickle
import requests
from fake_useragent import UserAgent
ua = UserAgent()


# 知乎用户粉丝信息爬虫
class zhihu():
	def __init__(self):
		self.headers = {
						'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
						'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
						}
		self.include = 'include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'
		self.followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?{include}'
	# 外部调用
	def get(self, user, savepath='./results', savename='data.pkl'):
		data = {}
		i = -1
		flag = True
		while flag:
			i += 1
			print('[INFO]:Start to get data in page %d...' % (i+1))
			include = self.include.format(i*20)
			res = requests.get(self.followers_url.format(user=user, include=include), headers=self.headers, timeout=30)
			self.headers['user-agent'] = ua.random
			res_json = json.loads(res.text)
			followers_data = res_json['data']
			for follower_data in followers_data:
				# 昵称
				name = self.__read_data_from_dict(follower_data, 'name')
				# 性别(1=男, 0=女, -1=未知)
				gender = self.__read_data_from_dict(follower_data, 'gender')
				# 标题
				headline = self.__read_data_from_dict(follower_data, 'headline')
				# 回答数量
				answer_count = self.__read_data_from_dict(follower_data, 'answer_count')
				# url_token
				url_token = self.__read_data_from_dict(follower_data, 'url_token')
				# 该用户的粉丝数量
				follower_count = self.__read_data_from_dict(follower_data, 'follower_count')
				# 整合数据
				while name in data:
					name += '0'
				data[name] = [gender, headline, answer_count, follower_count, url_token]
			if res_json['paging']['is_end']:
				flag = False
		print('[INFO]: Start to save data...')
		self.__save_data(data, savepath, savename)
		print('[INFO]: All done...')
	# 创建会话
	def __create_session(self):
		session = requests.Session()
		adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100, max_retries=3)
		session.mount('https://', adapter)
		session.mount('http://', adapter)
		return session
	# 从字典dict中根据key值读取数据
	def __read_data_from_dict(self, dictionary, key):
		value = dictionary.get(key)
		return value if value is not None else 'unknow'
	# 保存爬取到的数据
	def __save_data(self, data, savepath, savename):
		if not os.path.exists(savepath):
			os.mkdir(savepath)
		with open(os.path.join(savepath, savename), 'wb') as f:
			pickle.dump(data, f)


if __name__ == '__main__':
	zhihu().get(user='iseeisee', savename='iseeisee.csv')