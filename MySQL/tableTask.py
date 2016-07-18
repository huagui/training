#-*-coding:utf-8-*- 
import MySQLdb
import dbInit
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"

def get_by_title(Title):
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from task '+ 'WHERE title=%s'
	value=[Title]

	try:
		cur.execute(sql,value)
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	conn.commit()
    #result = cur.fetchall()
	result = cur.fetchone()
	cur.close()
	conn.close()
	return result

def get_by_id(id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from task '+ 'WHERE id=%s'
    value=[id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    #result = cur.fetchall()
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def get_all():
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from task '
    

    try:
        cur.execute(sql)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    result = cur.fetchall()
    # result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def get_by_class_id(class_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from task '+ 'WHERE class_id=%s'
    value=[class_id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    result = cur.fetchall()
    # result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def get_next_task(class_id,num):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from task '+ 'WHERE class_id=%s and num = %s + 1'
    value=[class_id,num]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    # result = cur.fetchall()
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result
 
if __name__ == "__main__":
    # record(2,1)
    # print get_by_title("task1")
    # print get_by_class_id(2) 
    print get_next_task(2,6)
    pass
	# update_info("tom","to1","1234770123",Nickname="雷")
	# update_info("test",Password="fdaf")