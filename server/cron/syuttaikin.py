#!/usr/bin/python
# coding: utf8
import os, time, datetime, urllib, urllib2

VARDIR = os.path.join(os.environ['HOME'], 'var')
# guruplugからの定期httpリクエストで更新されるファイル
PCIPADDR_FILE = os.path.join(VARDIR, 'guruplug/ip')
# PCIPADDR_FILEの最終更新日時が、この秒数より古い場合、PC電源断と判定
OFFLINE_SECS = 11 * 60 # 11min

SYUTTAIKIN_IPADDR_FILE = os.path.join(VARDIR, 'syuttaikin/ip')

def get_current_stat():
    # PCIPADDR_FILEの最終更新日時が、11分以上昔の場合、PC電源断と判定
    lastmodified = os.path.getmtime(PCIPADDR_FILE)
    now = time.time()
    if now - lastmodified > OFFLINE_SECS:
        return 'offline'
    else:
        return 'online'

def change_syuttaikin(url, cur):
    params = {'syuttaikin': '0'}
    if cur == 'online':
        params['syuttaikin'] = '1'
    data = urllib.urlencode(params)
    try:
        resp = urllib2.urlopen(url, data)
        print resp.read()
    finally:
        resp.close()

def make_syuttaikin_url():
    with open(SYUTTAIKIN_IPADDR_FILE, 'r') as f:
        ipaddr = f.read()
        return 'http://' + ipaddr.rstrip() + '/cgi-bin/syuttaikin.py'

# 前回の状態から変化した場合、サーボモータ位置変更
def main():
    url = make_syuttaikin_url()
    change_syuttaikin(url, get_current_stat())

if __name__ == "__main__":
    main()
