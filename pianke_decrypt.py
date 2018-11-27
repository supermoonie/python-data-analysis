import requests
import hashlib
import base64
import time
import json


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
LOGIN_URL = 'http://pianke.me/version5.0/user/login.php'
USER_INFO_URL = 'http://pianke.me/version5.0/space/info.php'



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
	print(res.json())

for x in range(100000,100010):
	get_one_user_info(x)
