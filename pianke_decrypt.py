import requests
import hashlib
import base64
import time
import json
import pymysql


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
LOGIN_URL = 'http://pianke.me/version5.0/user/login.php'
USER_INFO_URL = 'http://pianke.me/version5.0/space/info.php'

conn = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= 'wangchao123', db= 'spider')


def insert_pianke_user(user):
	cursor = conn.cursor()
	count_sql = "select count(1) from pianke_user where id = %d;" %(user['uid'])
	cursor.execute(count_sql)
	count = cursor.fetchone()[0]
	if count == 0:
		insert_sql = "insert pianke_user VALUES (%d, '%s', '%s', %d, '%s', %d, %d, %d);" %(user['uid'], pymysql.escape_string(user['uname']), user['city'], user['client'], pymysql.escape_string(user['desc']), user['from'], user['gender'], user['addtime'])
		print(insert_sql)
		cursor.execute(insert_sql)
	conn.commit()
	cursor.close()


def generate_authorization_and_sign():
	timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
	authorization = str(base64.b64encode((':' + timestamp).encode('utf-8')), 'utf-8')
	md5 = hashlib.md5()
	md5.update(('0' + timestamp).encode('utf-8'))
	sign = md5.hexdigest().upper()
	return {'authorization': authorization, 'sign': sign}


def login_pianke(mobile, pwd):
	authorization_sign = generate_authorization_and_sign()
	headers = {
		'Authorization': authorization_sign['authorization']
	}
	login_params = {
		'mobile': mobile,
		'pwd': pwd,
		'sig': authorization_sign['sign']
	}
	res = requests.get(LOGIN_URL, params= login_params, headers= headers)
	print(res.json())
	if res.json()['code'] is 0:
		return True
	else:
		return False


def get_one_user_info(user_id):
	authorization_sign = generate_authorization_and_sign()
	headers = {
		'Authorization': authorization_sign['authorization'],
		'User-Agent': USER_AGENT
	}
	params = {
		'uid': user_id,
		'sig': authorization_sign['sign']
	}
	res = requests.get(USER_INFO_URL, params= params, headers= headers)
	try:
		result = res.json()
	except Exception as e:
		return None
	if result['code'] == 0:
		if 'userinfo' in result['data']:
			return result['data']['userinfo']
		else:
			return None
	else:
		return None

def user_info_spider():
	cursor = conn.cursor()
	max_sql = "select max(id) from pianke_user;"
	cursor.execute(max_sql)
	max_id = cursor.fetchone()[0] + 1
	cursor.close()
	for x in range(max_id, max_id + 10000):
		user = get_one_user_info(x)
		if user != None:
			insert_pianke_user(user)


user_info_spider()
