'''
Created on 2015-8-4

@author: songshunzhang
'''

#!/usr/bin/python  
# -*- coding=utf-8 -*-
import os
import threading
def batchapk(input, filter, delete):
    for root, dirs, files in os.walk(input):
        for filename in files:
            if str(filename).endswith(filter):
                filepath = os.path.join(root, filename)
                print filepath
                cmd = "zip -d " + filepath + " " + delete
                result = os.popen(cmd).readlines()
                print result
                

if __name__ == '__main__':
    inputfolder = os.sys.argv[1]
    filter = os.sys.argv[2]    
    delete = os.sys.argv[3]
    batchapk(inputfolder, filter, delete)
    pass