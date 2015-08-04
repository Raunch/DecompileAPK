'''
Created on 2015-8-3

@author: songshunzhang
'''
#!/usr/bin/python  
# -*- coding=utf-8 -*-
import os
import threading
def batchapk(input, output, type):
    for root, dirs, files in os.walk(input):
        for filename in files:
            if str(filename).endswith("apk"):
                filepath = os.path.join(root, filename)
                print filepath
                py_file = "/Volumes/Macintosh_HD_E/ref-code/DecompileAPK/src/com/chukong/decomplie/main.py"
                os.system("python " + py_file + " " + filepath + " " + output + " " + type)
                print filepath + " OK"
                

if __name__ == '__main__':
    inputfolder = os.sys.argv[1]
    outputfolder = os.sys.argv[2]    
    outputtype = os.sys.argv[3]
    batchapk(inputfolder, outputfolder, outputtype)
    pass