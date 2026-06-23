"""
架构与逻辑问题测试文件
"""

import time
from typing import Any


# 1. 循环依赖风险 — 模块顶层直接相互引用
# 如果在 module_a.py 中 import module_b，module_b 又 import module_a，会出问题


# 2. 上帝类 — 单一类承担过多职责
class UserManager:
    def create_user(self, name: str, email: str): ...
    def delete_user(self, user_id: int): ...
    def send_email(self, to: str, subject: str, body: str): ...
    def generate_report(self, start_date: str, end_date: str): ...
    def connect_database(self, connection_string: str): ...
    def encrypt_data(self, data: bytes): ...
    def log_activity(self, message: str): ...
    def process_payment(self, amount: float, user_id: int): ...
    def render_html_template(self, template_path: str, context: dict): ...
    def manage_cache(self, key: str, value: Any = None): ...


# 3. 函数过长、圈复杂度过高
def process_order(order_data: dict) -> dict:
    result = {}
    # 假设这个函数有几百行，包含大量嵌套 if-else、循环和重复逻辑
    if order_data.get("type") == "physical":
        if order_data.get("weight", 0) > 10:
            if order_data.get("international"):
                if order_data.get("customs_required"):
                    result["shipping"] = "international_customs_heavy"
                else:
                    result["shipping"] = "international_heavy"
            else:
                result["shipping"] = "domestic_heavy"
        else:
            if order_data.get("international"):
                if order_data.get("customs_required"):
                    result["shipping"] = "international_customs_light"
                else:
                    result["shipping"] = "international_light"
            else:
                result["shipping"] = "domestic_light"
    elif order_data.get("type") == "digital":
        if order_data.get("license_type") == "perpetual":
            result["shipping"] = "digital_perpetual"
        elif order_data.get("license_type") == "subscription":
            result["shipping"] = "digital_subscription"
        else:
            result["shipping"] = "digital_standard"
    else:
        result["shipping"] = "unknown"
    return result


# 4. 重复代码
def validate_email_v1(email: str) -> bool:
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if len(email) > 254:
        return False
    return True

def validate_email_v2(email: str) -> bool:
    # validate_email_v1 几乎完全相同的逻辑
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if len(email) > 254:
        return False
    return True


# 5. 不必要的空列表作为默认参数（可变默认参数）
class DataProcessor:
    def __init__(self, items: list = []):
        self.items = items  # 所有实例共享同一个默认列表

    def add_item(self, item):
        self.items.append(item)
        return self.items


# 6. 异常被吞没 — 静默失败
def read_config_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception:
        pass  # 失败了不报错，调用方不知道出了问题
