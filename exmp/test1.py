#coding=utf-8

cmd = '/home/xw/桌面/111/exmp/test.sh'
import subprocess  
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
i=1
while i:  
    i=i-1;
    line = p.stdout.readline()  
    print line 
    if line >= '0.8':
        m=1
    else:
        m=0
    print m
