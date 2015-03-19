#utf-8
import serial
import time
import MySQLdb

class control:
    t = serial.Serial('/dev/ttyS3',9600)
    while True:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='test',port=3306)
        cur=conn.cursor()
        count=cur.execute('select * from haha where id=1')
        result=cur.fetchone() # huoqu yihang shuju
        rr=str(result[1])
        t.write(rr)
        time.sleep(1)
        print rr   
    cur.close()
    conn.close()
    t.close()

