# 删除数据库中的已注册测试数据
import pymysql
from tpshop_auto_test.config import DB_CONFIG

class TPshopDB:
    def __init__(self):
        self.db_config = DB_CONFIG  # 从配置文件导入数据库信息
    def delete_user_by_tel(self, tel):
        """根据手机号删除tp_users表中的用户（TPshop用户表固定为tp_users，手机号字段为mobile）"""
        conn = None
        cursor = None
        try:
            # 1. 连接数据库
            conn = pymysql.connect(** self.db_config)
            cursor = conn.cursor()

            # 2. 先查询用户是否存在（用于日志提示）
            cursor.execute("SELECT user_id FROM tp_users WHERE mobile = %s", (tel,))
            user = cursor.fetchone()
            if not user:
                print(f"[数据库操作] 手机号{tel}不存在，无需删除")
                return

            # 3. 执行删除（核心操作）
            delete_sql = "DELETE FROM tp_users WHERE mobile = %s"
            cursor.execute(delete_sql, (tel,))
            conn.commit()
            print(f"[数据库操作] 已删除手机号{tel}的用户（ID：{user[0]}）")

        except Exception as e:
            if conn:
                conn.rollback()  # 出错时回滚事务
            print(f"[数据库操作] 删除失败：{str(e)}")
        finally:
            # 4. 关闭连接（必须执行，避免资源泄露）
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    def delete_user_by_email(self, email):
        """根据邮箱删除tp_users表中的用户（TPshop用户表固定为tp_users，邮箱字段为email）"""
        conn = None
        cursor = None
        try:
            # 1. 连接数据库
            conn = pymysql.connect(** self.db_config)
            cursor = conn.cursor()

            # 2. 先查询用户是否存在（用于日志提示）
            cursor.execute("SELECT user_id FROM tp_users WHERE email = %s", (email,))
            user = cursor.fetchone()
            if not user:
                print(f"[数据库操作] 邮箱{email}不存在，无需删除")
                return

            # 3. 执行删除（核心操作）
            delete_sql = "DELETE FROM tp_users WHERE email = %s"
            cursor.execute(delete_sql, (email,))
            conn.commit()
            print(f"[数据库操作] 已删除邮箱{email}的用户（ID：{user[0]}）")

        except Exception as e:
            if conn:
                conn.rollback()  # 出错时回滚事务
            print(f"[数据库操作] 删除失败：{str(e)}")
        finally:
            # 4. 关闭连接（必须执行，避免资源泄露）
            if cursor:
                cursor.close()
            if conn:
                conn.close()