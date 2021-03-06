# -*- coding: utf-8 -*-

import subprocess
import re
import time
from configure.conf import configuration

class appium_controller():
    # 自動執行Appium並根據configuration來設定儲存路徑
    def start(self):
        # cmd = "appium --session-override --command-timeout 72000000 --log /Users/yuhsuan/Desktop/appium.log"

        logpath = configuration['appium_log_save_path']
        cmd = "appium --session-override --command-timeout 72000000 --log "+logpath
        p = subprocess.Popen(cmd,shell=True)
        time.sleep(10)

    # 尋找關鍵字將Appium給關閉
    def end(self):
        time.sleep(10)
        pid=""

        cmd = "ps -A | grep 'appium'"
        p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
        res=str(p.communicate()[0],'utf-8')

        res = res.split('\n')
        for i in res:
            if 'appium --session' in i:
                print('i',i)
                m = re.match('.*\d+',i)
                pid = m.group(0)
                print('pid'+pid)

        cmd = "kill "+pid
        print(cmd)
        p =subprocess.call(cmd,shell=True)