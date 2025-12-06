# 导包
import logging.handlers

class GetLogger:
    logger=None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取 日志器
            cls.logger=logging.getLogger()
            # 设置 日志器 级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器 控制台
            sh=logging.StreamHandler()
            # 获取处理器 文件-以时间分隔
            th=logging.handlers.TimedRotatingFileHandler(filename="../log/log01.log",
                                                         when="midnight",
                                                         interval=1,
                                                         backupCount=30,
                                                         encoding="utf-8")
            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm=logging.Formatter(fmt)
            # 将格式器添加到 处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到 处理器 文件
            th.setFormatter(fm)
            # 将处理器添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger
# 测试代码
if __name__ == "__main__":
    logger = GetLogger.get_logger()
    logger.debug("这是一个debug级别的日志")
    logger.info("这是一个info级别的日志")
    logger.warning("这是一个warning级别的日志")
    logger.error("这是一个error级别的日志")