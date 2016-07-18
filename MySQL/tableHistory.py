#-*-coding:utf-8-*- 
import MySQLdb
import dbInit
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


def record(Task_id, Student_id, Class_id):  
    '''分发任务时，添加记录，置状态标志为1  1：进行中，2：学员提交，等待教练评分，3：已完成'''

    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = """insert into history (task_id, student_id, class_id)""" \
        + """values(%s,%s,%s)"""
    value = [Task_id, Student_id, Class_id]
     
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def get_by_task_id(Task_id):
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from history '+ 'WHERE task_id=%s'
	value=[Task_id]

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

def update_info(Task_id, Student_id,Point=0,
    Grade=0, Finish=0):  

    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = 'update history set'

    current_time = time.strftime(TIMEFORMAT, time.localtime())

    if Finish == 1: #学员提交任务，置标志为2
    	sql += ''' finish_time="%s",'''%current_time
        sql += ''' status="2",'''
    if Grade == 1: #教练评分后，置标志为3
        sql += ''' point="%s",'''%Point
        sql += ''' status="3",'''


    sql = sql [:-1] + '''WHERE  (task_id, student_id) in((%s,%s))'''
    
     
    value = [Task_id,Student_id]
    print sql
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def get_by_student_class_id(Student_id, Class_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql =  'SELECT * FROM history WHERE student_id=%s and class_id=%s'
    value=[Student_id,Class_id]

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

def get_by_student_task_id(Student_id, Task_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql =  'SELECT * FROM history WHERE student_id=%s and task_id=%s'
    value=[Student_id,Task_id]

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
    # record(2,2,2)
    # print get_by_student_id(1)
    # print get_by_task_id(2)
    # update_info(2,2,Grade=1)
    print get_by_student_and_class_id(2,2)
    # update_info("tom","to1","1234770123",Nickname="雷")
    # update_info("test",Password="fdaf")
    pass