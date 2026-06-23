"""
安全漏洞测试文件 —— 应被 security_scan 检测到的问题
"""

import os
import pickle
import subprocess
import hashlib
import random
import base64


# 1. 硬编码敏感凭证
API_KEY = "sk-proj-abc123def456ghi789jkl"
DATABASE_URL = "postgresql://admin:SuperSecret@123@localhost:5432/production"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
JWT_SECRET = "my_jwt_secret_do_not_use_in_prod"

# 2. 不安全的密码哈希
def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def hash_password_sha1(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest()


# 3. eval — 任意代码执行
def calculate_expression(expr: str):
    return eval(expr)


# 4. exec — 任意代码执行
def run_user_code(code: str):
    exec(code)


# 5. pickle 不安全反序列化
def load_user_session(data: bytes):
    return pickle.loads(data)


# 6. subprocess shell=True 命令注入
def ping_host(address: str):
    cmd = f"ping -c 4 {address}"
    return subprocess.check_output(cmd, shell=True)

def delete_files(path: str):
    subprocess.call(f"rm -rf {path}", shell=True)


# 7. SQL 注入 — 字符串拼接
def get_user(username: str):
    query = "SELECT * FROM users WHERE username = '%s'" % username
    return query

def get_user_by_id(user_id: str):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def search_users(keyword: str):
    return f"SELECT * FROM users WHERE name LIKE '%{keyword}%'"


# 8. 硬编码临时密码
def create_default_admin():
    default_password = "admin123"
    return {"username": "admin", "password": default_password}


# 9. assert 用于权限检查（生产环境 -O 会跳过 assert）
def delete_user(requester_role: str, user_id: int):
    assert requester_role == "admin"
    print(f"Deleting user {user_id}...")


# 10. yaml.load 不安全
def load_yaml_config(yaml_str: str):
    import yaml
    return yaml.load(yaml_str)


# 11. 随机数不安全
def generate_reset_token():
    return str(random.randint(100000, 999999))

def generate_api_key():
    return base64.b64encode(os.urandom(16)).decode()


# 12. 路径遍历
def read_file(filename: str):
    with open(f"/var/data/{filename}", "r") as f:
        return f.read()

def delete_user_file(filename: str):
    os.remove(f"/tmp/uploads/{filename}")


# 13. 硬编码加密密钥
ENCRYPTION_KEY = b"1234567890123456"  # 弱密钥
IV = b"1234567890123456"


# 14. 不安全的 SSL
import ssl
def create_unverified_context():
    return ssl._create_unverified_context()


# 15. 异常信息暴露
def login(username: str, password: str):
    try:
        # ... 登录逻辑
        raise ValueError("Invalid credentials")
    except Exception as e:
        return str(e)  # 暴露内部错误信息给用户
