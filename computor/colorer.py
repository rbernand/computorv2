import logging


def add_coloring(func):
    # add methods we need to the class
    def new(handler, record):
        levelno = record.levelno
        if levelno >= 50:
            color = '\x1b[31m'  # red
        elif levelno >= 40:
            color = '\x1b[31m'  # red
        elif levelno >= 30:
            color = '\x1b[33m'  # yellow
        elif levelno >= 20:
            color = '\x1b[32m'  # green
        elif levelno >= 10:
            color = '\x1b[35m'  # pink
        else:
            color = '\x1b[0m'  # normal
        record.msg = color + record.msg + '\x1b[0m'  # normal
        # print "after"
        return func(handler, record)
    return new

logging.StreamHandler.emit = add_coloring(logging.StreamHandler.emit)
