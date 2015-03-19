#coding=utf-8
import MySQLdb
import subprocess 
m = 0
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='test',port=3306)
cur=conn.cursor()
cur.execute('drop table if exists data')
cur.execute('create table if not exists data(id int(9) auto_increment not null primary key,data varchar(255) not null)')

print "please input:"
var = input()
#count=cur.execute('select * from haha where id=%d' var)
if var == 1:
    cur.execute("insert into data values('1',%s)",var)
    conn.commit() 
    from camera import camera   
elif var == 2:
    cur.execute("insert into data values('2',%s)",var)
    conn.commit()
    from temperature import temperature
elif var == 3:
    cur.execute("insert into data values('3',%s)",var)
    conn.commit()
    from control import control
elif var == 4:
    cur.execute("insert into data values('3',%s)",var)
    conn.commit()
    from camera import camera
    cmd = '/home/xw/桌面/all/test.sh' 
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
conn.commit()
cur.close()
conn.close()
    
