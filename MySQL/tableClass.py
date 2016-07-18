#-*-coding:utf-8-*- 
import MySQLdb
import dbInit

def get_by_name(Name):
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from class '+ 'WHERE name=%s'
	value=[Name]

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
    sql = 'select * from class '+ 'WHERE id=%s'
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

def get_by_cate_id(cate_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from class '+ 'WHERE cate_id=%s'
    value=[cate_id]

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

if __name__ == '__main__':
	# print get_by_id(1)
	print get_by_cate_id(1)
	# print get_by_name("PHP中级")
	pass