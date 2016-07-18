#-*-coding:utf-8-*- 
import MySQLdb
import dbInit


def get_all_cate():
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from category'

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

def get_by_parent_id(P_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from category '+ 'WHERE parent_id=%s'
    value=[P_id]

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

def get_by_id(id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from category '+ 'WHERE id=%s'
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

if __name__ == '__main__':
	# print get_all_cate()
	print get_by_parent_id(0)
	pass