#!/usr/bin/python
# coding: utf8
import os, time

# guruplugからの定期httpリクエストで更新されるファイル
PCIPADDR_FILE = '/home/kihara/var/guruplug/temper.rrd'
# PCIPADDR_FILEの最終更新日時が、この秒数より古い場合、PC電源断と判定
OFFLINE_SECS = 11 * 60 # 11min

def get_current_stat():
    if not os.path.exists(PCIPADDR_FILE):
        return 'offline'
    # PCIPADDR_FILEの最終更新日時が、11分以上昔の場合、PC電源断と判定
    lastmodified = os.path.getmtime(PCIPADDR_FILE)
    now = time.time()
    if now - lastmodified > OFFLINE_SECS:
        return 'offline'
    else:
        return 'online'

def main():
    print "Content-Type: text/plain"
    print
    print get_current_stat()

if __name__ == "__main__":
    main()
