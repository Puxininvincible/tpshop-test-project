# 1. 公共依赖的已注册用户（不删除）
PUBLIC_TELS = ["13811112222"]# 推荐人、重复注册测试用的固定手机号
PUBLIC_EMAIL=["12345@qq.com"]# 重复注册测试用的固定邮箱
#已注册用户密码都为123456
# 其余测试未注册手机号为13812345678未注册邮箱为12344@qq.com
# 2. 数据库连接信息
DB_CONFIG = {
    "host": "localhost",    # 数据库地址
    "user": "root",         # 数据库账号
    "password": "root",   # 数据库密码
    "database": "tpshop3.0",   # TPshop默认数据库名
    "charset": "utf8"
}