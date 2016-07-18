#-*-coding:utf-8-*- 
import MySQLdb
import dbInit


def set_notification(user_type, target_id, content, relation_id=None, msg_type=None, agreement=2,):  
    '''
    设置通知。user_type： 1为学员
    '''
    if relation_id==None:
    	relation_id="0"
    if msg_type==None:
    	msg_type="0"
    

    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = """insert into notification (user_type, target_id, content, relation_id, msg_type, agreement)""" \
        + """values(%s,%s,%s,%s,%s,%s)"""
    value = [user_type, target_id, content, relation_id, msg_type, agreement]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()


def get_by_target_id(user_type,target_id):
	'''
	查询未被用户处理的通知
	'''
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from notification '+ 'WHERE user_type=%s and target_id=%s and is_handled=0'
	value=[user_type, target_id]

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
	'''

	'''
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from notification '+ 'WHERE id=%s and is_handled=0'
	value=[id]

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

def update_status(id):  
    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = '''update  notification set is_handled=1   WHERE  id=%s'''
    value = [id]
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def remove_notification(id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = '''delete  from  notification   WHERE  id=%s'''
    value = [id]
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def remove_by_relation_id(relation_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = '''delete  from  notification   WHERE  relation_id=%s'''
    value = [relation_id]
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
	# set_notification(1,1,"haha",25)
	# remove_notification(11)
	remove_by_relation_id(48)
	# print get_by_target_id(2,2)
	pass

	