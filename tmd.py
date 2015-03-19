#coding:utf-8
import pygame
import subprocess
import serial
import pygame.camera
import time
import MySQLdb
from pygame.locals import *

def camera():                                         #camera
    pygame.init()
    pygame.camera.init()
    cam=pygame.camera.Camera("/dev/video0",(320,240))
    li=range(1)
    i=1
    cam.start()
    for i in li:
	image = cam.get_image()
	#pygame.image.save(image,str(i)+".jpg")
        pygame.image.save(image,'/var/www/html/1.jpg')
        time.sleep(2)
    cam.stop()

def temperature():                                    #temperature
    t = serial.Serial('/dev/ttyS1',9600) 
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='data',port=3306)
    cur=conn.cursor()
    cur.execute('drop table if exists wendu')
    cur.execute('create table if not exists wendu(id int(9) auto_increment not null primary key,wendu varchar(255) not null,time datetime)')
    print t.portstr   

    for m in range(1):
        z=range(1)
        t.write('9')       #just a date for get temperature
        time.sleep(0.1)
        shiwei=t.read(1)
        gewei=t.read(1)
        xiaoshu=t.read(1)
        wenduzhi=shiwei+gewei+'.'+xiaoshu+'C'
        print 'wendu:'+wenduzhi
        for i in z:
            conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='data',port=3306)
            cur=conn.cursor()
            cur.execute("insert into wendu values('',%s,now())",wenduzhi)
            #sql="update wendu SET wendu=%s WHERE id=1"
            cur.execute("update wendu SET wendu=%s WHERE id=1",wenduzhi)
            #result3=cur.fetchone() # huoqu yihang shuju
            conn.commit()
            cur.close()
            conn.close()
            i=i+1
    t.close()

def control():                                    #control
    t = serial.Serial('/dev/ttyS1',9600)
    for m in range(1):
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='data',port=3306)
        cur=conn.cursor()
        count1=cur.execute('select * from data1 where id=1')
        result1=cur.fetchone() # huoqu yihang shuju
        rr=str(result1[1])
        t.write(rr)
        time.sleep(1)
        print 'rr'+rr   
    t.close()

def access():                                            #access
    t = serial.Serial('/dev/ttyS1',9600)
    pygame.init()    
    pygame.camera.init()
    cam=pygame.camera.Camera("/dev/video0",(320,240))
    cam.start()
    image = cam.get_image()
    pygame.image.save(image,'1.jpg')
    cam.stop()
    i = 1
    while i:  
        i=i-1;
        cmd = '/home/xw/桌面/最新程序/all2/test.sh' 
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        line = p.stdout.readline()  
        print line 
        if line >= '0.6':
            m=1
            t.write('4')
        else:
            m=0
            t.write('5')
        print m

if __name__ == '__main__':
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='data',port=3306)
    cur=conn.cursor()
    count2 = cur.execute('select * from data2 where id=1')
    while True:
        temperature()
        control()
        camera()
        access()

