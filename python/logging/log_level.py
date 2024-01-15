""" Shows how to set log levels. """
import logging
from sys import argv

# Calling logging.* acts on the root logger
# Aka global logger

lvl = "debug"
if len(argv) == 2:
    lvl = argv[1]


def map_lvl(lvl: str) -> int:
    match lvl.lower():
        case "debug":
            return logging.DEBUG
        case "info":
            return logging.INFO
        case "warning":
            return logging.WARNING
        case "error":
            return logging.ERROR
        case "critical":
            return logging.CRITICAL
        case _ as l:
            raise TypeError(f"log lvl {l} not supported")


try:
    logging.getLogger().setLevel(map_lvl(lvl))
except TypeError as e:
    print(e)

print(f"lvl in use for the root logger: {lvl}\n")

foo = Exception("foo")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.exception(foo)
logging.critical("critical")
