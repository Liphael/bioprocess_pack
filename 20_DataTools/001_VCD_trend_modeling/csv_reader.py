import os
import re
import time
import numpy as np
import pandas as pd

# record setting
# 日志记录，记录程序运行状态
rec = "Start recording:"

# seeking path of csv files
# 定义path为根目录，原始根目录为当前目录；定义dic为绝对路径根目录下的所有文件
path = ""
dic = os.listdir(
    os.path.abspath(
        "."
    )
)

# file sequence initialize
# 日志文件序号，跟踪文件的处理批和处理进度
fseq = 1

# dataframe construction
# 定义临时变量f，遍历dic中的文件名
for f in dic:
    if "res" in f and f.endswith(".csv"):
        fpath = f