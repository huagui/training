#-*-coding:utf-8-*- 
import MySQLdb
import dbInit
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


def record(Trainer_id, Student_id, Class_id):  
    '''学员申请教练时置标记为0  状态标记 0：学生申请了该教练  1:教练接受该学员申请'''

    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = """insert into relation (student_id, trainer_id, class_id)""" \
        + """values(%s,%s,%s)"""

    value = [Student_id, Trainer_id, Class_id]     
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

# def update_status(Trainer_id, Student_id, Class_id):  
#     '''教练接受学员的申请时置标记为1  状态标记 0：学生申请了该教练  1:教练接受该学员申请'''
#     conn = dbInit.connect_mysql()
#     cur = conn.cursor()

#     sql = '''update  relation set status=1   WHERE  trainer_id=%s and student_id=%s and class_id=%s'''
#     value = [Trainer_id, Student_id, Class_id]
#     try:
#         cur.execute(sql,value)
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#     conn.commit()
#     cur.close()
#     conn.close()

def update_status(id):  
    '''教练接受学员的申请时置标记为1  状态标记 0：学生申请了该教练  1:教练接受该学员申请'''
    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = '''update  relation set status=1   WHERE  id=%s'''
    value = [id]
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def get_by_trainer_id(trainer_id, class_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from relation '+ 'WHERE trainer_id=%s and class_id=%s and status=1'
    value=[trainer_id, class_id]

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

def get_by_trainer(trainer_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from relation '+ 'WHERE trainer_id=%s and status=1'
    value=[trainer_id]

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

def get_by_student_id(student_id, class_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from relation '+ 'WHERE student_id=%s and class_id=%s and status=1'
    value=[student_id, class_id]

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

def get_by_student(student_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from relation '+ 'WHERE student_id=%s and status=1'
    value=[student_id]

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

def get_by_three_id(trainer_id,student_id, class_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from relation '+ 'WHERE trainer_id=%s and student_id=%s and class_id=%s'
    value=[trainer_id, student_id, class_id]

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

def get_by_id(id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from relation '+ 'WHERE id=%s '
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

def remove_by_id(id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'delete  from relation WHERE id=%s and status=0'
    value=[id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def isExist(student_id):
    if get_by_student_id(student_id) == None:
        return False
    else:
        return True
 
if __name__ == "__main__":
    # record(2,1,1)
    # update_status(2,1,1)
    # print get_by_student_id(2,1)
    # print get_by_three_id(2,8,2)
    # print get_by_trainer_id(2,2)
    # print get_by_trainer(2)
    remove_by_id(48)
    pass
	# update_info("tom","to1","1234770123",Nickname="雷")
	# update_info("test",Password="fdaf")