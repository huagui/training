#-*-coding:utf-8-*- 
import MySQLdb
import dbInit
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


def write_comment(student_id,trainer_id,content,class_id):
	'''
	写评论
	'''
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	#按时间倒序
	sql = 'insert into comment (student_id,trainer_id,content,publish_time,class_id)'\
			+ 'value(%s,%s,%s,%s,%s)'
	publish_time = time.strftime(TIMEFORMAT, time.localtime())
	value=[student_id,trainer_id,content,publish_time,class_id]

	try:
		cur.execute(sql,value)
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	conn.commit()
	# result = cur.fetchall()
	# result = cur.fetchone()
	cur.close()
	conn.close()
	# return result

def get_by_trainer_id(trainer_id,num=None):
	'''
	
	'''
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	#按时间倒序
	sql = 'select * from comment '+ 'WHERE trainer_id=%s order by publish_time desc '
	value=[trainer_id]
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
	# write_comment(1,1,'good')
	print get_by_trainer_id(1,1)
	pass