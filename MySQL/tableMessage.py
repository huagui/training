#-*-coding:utf-8-*- 
import MySQLdb
import dbInit
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"

def send_message(relation_id, from_stu, content):  
    '''
    设置message
    '''
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    current_time = time.strftime(TIMEFORMAT, time.localtime())

    sql = """insert into message (relation_id, from_stu, content, publish_time)""" \
        + """values(%s,%s,%s,%s)"""
    value = [relation_id, from_stu, content, current_time]
     
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def get_by_relation_id(relation_id,num=None):
	'''
	
	'''
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	#按时间倒序
	sql = 'select * from message '+ 'WHERE relation_id=%s order by publish_time desc '
	value=[relation_id]
	if num:
		sql += 'limit 0,%s'
		value.append(num)

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
	# set_message(1,1,"aaaaa")
	# print type(get_by_relation_id(1))
	print get_by_relation_id(48,1)
	# print get_by_relation_id(1)
	pass