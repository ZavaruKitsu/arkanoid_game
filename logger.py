import ctypes
import datetime
import enum
import os
import threading
from ctypes import ArgumentError

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

FILE = open('logger.log', 'a')
pid = str(os.getpid()).ljust(5)

RESET_COLOR = '\033[0m'

DEBUG_COLOR = '\033[36m'
INFO_COLOR = '\033[32m'
WARNING_COLOR = '\033[33m'
ERROR_COLOR = '\033[31m'

LOCK = threading.Lock()


class LEVEL(enum.IntEnum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3


__console_level__ = LEVEL.INFO
__file_level__ = LEVEL.DEBUG


class logger:
    @staticmethod
    def prefix(level: str):
        level = level.ljust(7)
        return f"[{datetime.datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')}] [{__name__} {pid}] [{level}]"

    @staticmethod
    def set_console_level(level: LEVEL):
        if type(level) is LEVEL:
            global __console_level__
            __console_level__ = level
        else:
            raise ArgumentError()

    @staticmethod
    def set_file_level(level: LEVEL):
        if type(level) is LEVEL:
            global __file_level__
            __file_level__ = level
        else:
            raise ArgumentError()

    @staticmethod
    def log(color: str, level: LEVEL, level_str: str, *args, **kwargs):

        if level.value >= __console_level__:
            LOCK.acquire()

            try:
                print(' ' + color + logger.prefix(level_str) + ' ', end='')
                print(*args, **kwargs)
                print(RESET_COLOR, end='')
            except:
                pass

            LOCK.release()

        if level.value >= __file_level__:
            try:
                print(logger.prefix(level_str) + ' ', end='', file=FILE)
                print(*args, **kwargs, file=FILE)
            except:
                print('!!! FAILED TO LOG DATA !!!', file=FILE)

    @staticmethod
    def debug(*args, **kwargs):

        logger.log(DEBUG_COLOR, LEVEL.DEBUG, 'DEBUG', *args, **kwargs)

    @staticmethod
    def info(*args, **kwargs):

        logger.log(INFO_COLOR, LEVEL.INFO, 'INFO', *args, **kwargs)

    @staticmethod
    def warning(*args, **kwargs):

        logger.log(WARNING_COLOR, LEVEL.WARNING,
                   'WARNING', *args, **kwargs)

    @staticmethod
    def error(*args, **kwargs):

        logger.log(ERROR_COLOR, LEVEL.ERROR, 'ERROR', *args, **kwargs)

    @staticmethod
    def _input(*args, **kwargs):

        return ' ' + input(logger.prefix('INPUT') + ' [you]') + ' \n'

    @staticmethod
    def _output(*args, **kwargs):

        return ' ' + input(logger.prefix('OUTPUT')) + ' '
