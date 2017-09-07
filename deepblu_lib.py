# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 下午2:19
# @Author  : Yuhsuan
# @File    : deepblu_lib.py
# @Software: PyCharm Community Edition

import datetime
import os
import logging
from logging.handlers import RotatingFileHandler
import logging.handlers

# def log(output):
#     now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
#
#     print(now, output)
#     with open("log.txt", "a") as myfile:
#         myfile.write(now+" "+output+"\n")

# 設定log輸出的路徑
dir = '%s/' % os.getcwd()
dir = dir +'AndroidAppTest/'+ datetime.datetime.now().strftime("%Y%m%d")
if not os.path.exists(dir):
    os.makedirs(dir)
now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
file_path = dir + "/" + now + ".log"

# 控制console輸出的等級, 預設為DEBUG以上
# format: 2017-04-26 18:19:42 D Starting new HTTP connection (1): test.tritondive.co
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    )
logging.addLevelName(0, "N")
logging.addLevelName(10, "D")
logging.addLevelName(20, "I")
logging.addLevelName(30, "W")
logging.addLevelName(40, "E")
logging.addLevelName(50, "C")

# 控制Log輸出文檔, 單檔5MB, 最多五個檔案Rotate, 預設為INFO以上
logfile = logging.handlers.RotatingFileHandler(file_path,mode='a',maxBytes=5000000,backupCount=5)
#logfile = RotatingFileHandler(file_path, maxBytes=5000000,backupCount=5)
logfile.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s',"%Y-%m-%d %H:%M:%S"))
logfile.setLevel(logging.INFO)

# 如果只使用logging.getLogger()會將其他import的lib log也印出來
logger = logging.getLogger(__name__)
logger.addHandler(logfile)

d = ["d", "D", "debug", "DEBUG", "Debug"]
i = ["i","I","info","INFO","Info"]
w = ["w","W","warning","WARNING","Warning"]
e = ["e","E","error","ERROR","Error"]
c = ["c","C","critical","CRITICAL","Critical"]

def log(output,lvl=None):
    if lvl in d:
        logger.debug(output)
    elif lvl in i:
        logger.info(output)
    elif lvl in w:
        logger.warning(output)
    elif lvl in e:
        logger.error(output)
    elif lvl in c:
        logger.critical(output)
    else:
        logger.info(output)