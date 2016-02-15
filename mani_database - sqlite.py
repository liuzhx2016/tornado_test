#*-* coding=utf8 *-*
import sqlite3 as sq

database = sq.connect(".\\mydata.db")

# 我们需要使用游标对象SQL语句查询数据库，获得查询对象。 通过以下方法来定义一个游标。
# cu=cx.cursor()
# 游标对象有以下的操作：
# execute()--执行sql语句   
# executemany--执行多条sql语句   
# close()--关闭游标   
# fetchone()--从结果中取一条记录，并将游标指向下一条记录   
# fetchmany()--从结果中取多条记录   
# fetchall()--从结果中取出所有记录   
# scroll()--游标滚动  

# create catalog/ table
#database.execute('create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE)')

# insert elements , we can use cursor to execute sql setence
# database.execute("insert into catalog values(0, 0, \"LIUZHX\" )")
# database.execute("insert into catalog values(1, 0, \"nihao\" )")
#cu = database.cursor()
#cu.execute("insert into catalog values(12, 32, \"Ldsfd\" )")

#find element
cu = database.cursor()
cu.execute("select * from catalog")
buf = cu.fetchall()
print buf

#change element
cu1 = database.cursor()
cu1.executemany("update catalog set name=? where id=1",u"你好阿道夫")  ##有问题？？？？


database.commit()
database.close()
