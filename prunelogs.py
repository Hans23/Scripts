#!/usr/bin/python
#
# This script is for pruning the log files on a daily basis. 
# Last 100 lines of the logs are saved. This script is run 
# via a cron job once a day.
#

import os

# Get a list of all the files in /home/builder/PushLogs folder
folder = "/<path>/Logs/"
file_list = os.listdir(folder)

for file in file_list:
    fi = open(folder+file,"r")
    lines = fi.readlines()
    fi.close()
    print("Pruning "+ file + "--" + str(len(lines)))
    if len(lines) > 100:
       fo = open(folder+file,"w")
       fo.writelines(lines[len(lines)-100:])
       fo.close()
