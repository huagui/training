#-*-coding:utf-8-*- 
import MySQLdb
import dbInit
import time

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"

def set_question(content, publish_time, relation_id=0, stu_name=None, phone=None, qq=None, flower_num=10):  
	'''
	
	'''
	
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = """insert into question (relation_id, stu_name, qq, content, flower_num, publish_time, phone)""" \
		+ """values(%s,%s,%s,%s,%s,%s,%s)"""
	value = [relation_id, stu_name, qq, content, flower_num, publish_time, phone]

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

	sql = '''delete  from  question   WHERE  relation_id=%s'''
	value = [relation_id]
	try:
		cur.execute(sql,value)
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	conn.commit()
	cur.close()
	conn.close()

def update_by_relation_id(relation_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = '''update   question set   trainer_verify=1  WHERE  relation_id=%s'''
    value = [relation_id]
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def get_by_relation_id(relation_id):

	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from question WHERE relation_id  = %s'
	value=[relation_id]

	try:
		cur.execute(sql,value)
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	conn.commit()
	result = cur.fetchone()
	cur.close()
	conn.close()
	return result

def remove_by_relation_id(relation_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = '''delete  from  question   WHERE  relation_id=%s'''
    value = [relation_id]
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
	# set_question('这个问题不懂',2)
	# print get_by_relation_id(1)

    update_by_relation_id(1)
	# remove_by_relation_id(2)
    pass