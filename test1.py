#coding=utf-8
from camera import camera 
cmd = '/home/xw/桌面/all/test.sh'
import subprocess  
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
i=1
while i:  
    i=i-1;
    line = p.stdout.readline()  
    print line 
    if line >= '0.65':
        m=1
    else:
        m=0
    print m
