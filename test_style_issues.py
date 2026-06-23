"""
代码风格问题测试文件 —— 应被 check_style 检测到的问题
"""

# 未使用的 import
import json
import os
import sys
import datetime
from typing import List, Dict, Optional, Any
from collections import defaultdict

# 未使用的变量
unused_global = "这个变量从未被使用"

# 超长行
long_line = "这是一行非常非常长的代码，它超过了 PEP8 推荐的 88 字符限制，也超过了传统的 79 字符限制，甚至比 120 字符还要长得多得多得多得多得多得多得多得多得多得多得多得多得多得多得多，应该会触发 E501 错误"

# 未使用的函数
def never_called_function():
    return "这个函数从未被调用"


def function_with_style_issues( x,y,z ):
    # 函数括号内有空格，参数逗号后无空格
    result=x+y+z
    # 操作符周围缺少空格
    if result==0:
        # 使用了 == None 而非 is None
        return None

    # 行尾空格（注意下面这行末尾有空格）
    something = "有尾随空格"

    # 使用 is 比较字面量
    if something is "":
        return "空字符串"
    if something is True:
        return "True"

    # 裸 except
    try:
        int("abc")
    except:
        pass

    return result


class myCamelClass:  # 类名不符合 PascalCase
    def __init__(self,value):
        self.value=value

    def getValue(self):
        # 比较 None 使用 ==
        if self.value == None:
            return 0
        return self.value

    def do_something( self ):
        # 方法括号内有空格
        pass


# 多个空行

# 模块级别代码（应在 if __name__ == "__main__" 中）
print("模块被加载时执行")
