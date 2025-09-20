import os
import time
import schedule
from dotenv import load_dotenv
from logger_config import setup_logger

from login import auto_login

# 初始化日志
logger = setup_logger()

def check_login():
    """检查网络并尝试登录"""
    try:
        load_dotenv()  # 加载环境变量

        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        if not username or not password:
            logger.error("未找到用户名或密码，请检查 .env 文件。")
            return

        try:
            auto_login(username, password)
        except Exception as e:
            logger.error(f"登录过程中发生异常: {e}")
    except Exception as e:
        logger.error(f"检查网络时发生未知错误: {e}")

if __name__ == "__main__":
    # 立即执行一次
    logger.info("=== 网络自动登录守护程序启动 ===")
    check_login()

    # 每 30 秒执行一次
    schedule.every(30).seconds.do(check_login)

    logger.info("已设置定时任务：每 30 s 检查一次网络状态...")

    # 保持程序运行
    while True:
        schedule.run_pending()
        time.sleep(1)