
import serial  
import time  
import MySQLdb

class temperature:  
    t = serial.Serial('/dev/ttyUSB0',9600) 
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='test',port=3306)
    cur=conn.cursor()
    cur.execute('drop table if exists wendu')
    cur.execute('create table if not exists wendu(id int(9) auto_increment not null primary key,wendu varchar(255) not null,time datetime)')
    print t.portstr   

    for m in range(200):
        z=range(10)
        t.write('0')
        time.sleep(0.1)
        shiwei=t.read(1)
        gewei=t.read(1)
        xiaoshu=t.read(1)
        wenduzhi=shiwei+gewei+'.'+xiaoshu+'C'
        print 'wendu:'+wenduzhi
        for i in z:
            conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='test',port=3306)
            cur=conn.cursor()
            cur.execute("insert into wendu values('',%s,now())",wenduzhi)
            #sql="update wendu SET wendu=%s WHERE id=1"
            #cur.execute("update wendu SET wendu=%s WHERE id=1",wenduzhi)
            result=cur.fetchone() # huoqu yihang shuju
            conn.commit()
            cur.close()
            conn.close()
            i=i+1
    t.close()
