import logging
import inspect
import os

# handler = logging.StreamHandler()
# https://qiita.com/hubuzo/items/27156a470105bb07bfc4
class Logger():
    """
    ログ出力用クラス
    """
    def __init__(self,name):
        self.logger = logging.getLogger(name)
        # ハンドラ作成
        stream_handler = logging.StreamHandler()
        # フォーマッタを作成
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(filename)s | %(module)s | %(lineno)d | %(process)d')
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        # self.o.addHandler(.setL)
        # self.handler.setLevel(logging.debug)
    
    def debug(self):
        self.logger.debug("DEBUG")
        
    def info(self):
        self.logger.info("INFO")
        
    def warning(self):
        self.logger.warning("WARNING")
    
    def error(self):
        self.logger.error("ERROR")
    
#     def __init__(self):
#         self.logger = logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")

#     def debug(self, execution_location, log_message):
#         self.logger = logging.getLogger(execution_location)
#         self.logger.debug(log_message)

#     def info(self, execution_location, log_message):
#         self.logger = logging.getLogger(execution_location)
#         self.logger.info(log_message)

#     def warning(self, execution_location, log_message):
#         self.logger = logging.getLogger(execution_location)
#         self.logger.warning(log_message)

#     def error(self, execution_location, log_message):
#         self.logger = logging.getLogger(execution_location)
#         self.logger.error(log_message)

# class Trace():
#     """
#     ログ出力とセットで使う処理をまとめたクラス
#     """
#     @classmethod
#     def execution_location(self):
#         """
#         処理の実行場所を出力する。[ファイル名: 行番号  メソッド名]
#         """
#         frame = inspect.currentframe().f_back
#         return "{}:{} {}".format(os.path.basename(frame.f_code.co_filename), frame.f_lineno, frame.f_code.co_name)

# def test_method():
#     log = Logger()
#     log.debug(Trace.execution_location(), 'debug test')

# test_method()
