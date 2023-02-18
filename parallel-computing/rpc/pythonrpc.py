import rpyc

conn = rpyc.classic.connect("localhost")
conn.execute('import math')
conn.execute('import time')
conn.execute('print(\'asdasdasd\')')
