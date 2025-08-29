import sys
import logging

APP_NAME = "Currency Converter"
APP_VERSION = "0.0.1"
DEBUG = True

DEFAULT_CACHE_TTL = 3600


formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
stream_handler.setFormatter(formatter)

logging.basicConfig(
    handlers=[stream_handler], level=logging.DEBUG if DEBUG else logging.INFO
)
