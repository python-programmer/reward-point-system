from django.db import connection
from django.conf import settings
import os


def terminal_width():
    width = 0
    try:
        import struct, fcntl, termios
        s = struct.pack('HHHH', 0, 0, 0, 0)
        x = fcntl.ioctl(1, termios.TIOCGWINSZ, s)
        width = struct.unpack('HHHH', x)[1]
    except:
        pass
    if width <= 0:
        try:
            width = int(os.environ['COLUMNS'])
        except:
            pass
    if width <= 0:
        width = 80
    return width


class SQLLoggerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        indentation = 2
        if len(connection.queries) > 0 and settings.DEBUG:
            width = terminal_width()
            total_time = 0.0
            for query in connection.queries:
                nice_sql = query['sql'].replace('"', '').replace(',', ', ')
                sql = "\033[1;31m[%s]\033[0m %s" % (query['time'], nice_sql)
                total_time = total_time + float(query['time'])
                while len(sql) > width - indentation:
                    print("%s%s" % (" " * indentation, sql[:width - indentation]))
                    sql = sql[width - indentation:]
                print("%s%s\n" % (" " * indentation, sql))
            replace_tuple = (" " * indentation, str(total_time))
            print("%s\033[1;32m[TOTAL TIME: %s seconds]\033[0m" % replace_tuple)
        return response