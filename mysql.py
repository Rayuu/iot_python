import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='madong',db='test',port=3306)
cur=conn.cursor()
cur.execute('drop table if exists data')
cur.execute('create table if not exists data(id int(9) auto_increment not null primary key,data varchar(255) not null)')
cur.execute('select * from haha where id=1')
