#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

for arg in sys.argv[1:]:
    if arg == '-cli':
        os.system("redis-cli")
        sys.exit(0)

port = 6379
conf_file = './redis.conf'
pid_file = '/var/run/redis/redis-server.pid'
log_file = '/var/log/redis/redis-server.log'

os.system("sudo redis-server %s" % conf_file)
pid = os.popen("cat %s" % pid_file).read().strip()
if len(pid) != 0:
    print("(PID: %s) Redis server listening on port %d." % (pid, port))
    print("Log file: %s" % log_file)
else:
    print("Starting redis server failed.")
