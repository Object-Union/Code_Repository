"""
综合问题测试文件 — 同时包含安全、风格、逻辑等多种问题
"""

import os
import subprocess
import hashlib
import pickle
from typing import Optional

# ---- 安全 + 风格 ----
HARDCODED_PASSWORD = "P@ssw0rd123"   # 硬编码凭证 + 行尾空格
API_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"

# 未使用的 import：os, subprocess, hashlib, pickle, Optional 中的 Optional

def runCommand( cmd: str ):
    # 命名不规范 (应为 run_command)、subprocess + shell=True + 除零风险
    output = subprocess.check_output( cmd, shell=True, text=True )
    count = 0
    avg = 100 / count    # ZeroDivisionError
    return output

def process_user( userdata: bytes ):
    # pickle.loads 不安全
    user = pickle.loads( userdata )

    # eval 不安全
    role = eval( user.get( "role", "guest" ) )

    # SQL 注入
    sql = "SELECT * FROM users WHERE role = '" + role + "';"

    # MD5 弱哈希
    token = hashlib.md5( role.encode() ).hexdigest()

    return { "user": user, "sql": sql, "token": token }

def writeFile( path ):
    # 路径遍历
    f = open( "/tmp/" + path, "w" )
    f.write( "data" )
    f.close()

# ---- 风格 ----
UnusedGlobalVariable = 42

# 空行过多（连续 4+ 行）




# 超长行
this_variable_has_an_extraordinarily_long_name = "and the string assigned to it is also very long and should definitely trigger line-length linting rules in style checkers"

def badly_formatted_func( x,y,z ):
    result=x+y+z
    if result==None:
        return 0
    return result



# ---- 逻辑 ----
class BadClass:
    shared_data = []   # 类级别的可变共享状态

    def __init__( self, name ):
        self.name = name

    def add( self, item ):
        self.shared_data.append( item )   # 影响所有实例

def divide( a, b ):
    return a / b    # 没有除零检查
