#-*-coding:utf-8-*- 
import MySQLdb
import dbInit

def register(Username, Password,
    Phone, About, Nickname):  
    '''
    trainer_id和class_id字段默认值为0，学员注册时，自动置零
    '''
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = """insert into student (username, password, phone,
             about, nickname)""" \
        + """values(%s,%s,%s,%s,%s)"""

    value = [Username, Password, Phone, About, Nickname]
     
    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def get_by_username(Username):
	conn = dbInit.connect_mysql()
	cur = conn.cursor()
	sql = 'select * from student '+ 'WHERE username=%s'
	value=[Username]

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

def update_info(id, Password=None,
    Phone=None, About=None, Nickname=None, Trainer_id=None):  

    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = 'update student set'

    if Password != None:
    	sql += ''' password="%s",'''%Password
    if Phone != None:
    	sql += ''' phone="%s",'''%Phone
    if About != None:
    	sql += ''' about="%s",'''%About
    if Nickname != None:
    	sql += ''' nickname="%s",'''%Nickname
    # if Trainer_id != None:
    # 	sql += ''' trainer_id="%s",'''%Trainer_id

    sql = sql[:-1] + ''' where id="%d"'''%id

    try:
        cur.execute(sql)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def get_by_trainer_id(trainer_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from student '+ 'WHERE trainer_id & %s = %s'
    value=[2**trainer_id,2**trainer_id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def add_trainer_by_id(trainer_id,student_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'update student set trainer_id = trainer_id '+ ' | %s where id = %s'
    value=[2**trainer_id,student_id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def remove_trainer_by_id(trainer_id,student_id):
    '''
    若该学生有对应教练、则删除
    '''
    result = get_by_trainer_id(trainer_id)
    for stu in result:
        if int(stu[0]) == student_id: 
            conn = dbInit.connect_mysql()
            cur = conn.cursor()
            sql = 'update student set trainer_id = trainer_id '+ ' ^ %s where id = %s'
            value=[2**trainer_id,student_id]

            try:
                cur.execute(sql,value)
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            conn.commit()
            cur.close()
            conn.close()


def add_class_by_id(class_id,student_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'update student set class_id = class_id '+ ' | %s where id = %s'
    value=[2**int(class_id),student_id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()


def get_by_class_id(class_id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from student '+ 'WHERE class_id & %s = %s'
    value=[2**int(class_id),2**int(class_id)]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def remove_class_by_id(class_id,student_id):
    '''
    若该学生有对应班级、则删除
    '''
    result = get_by_class_id(class_id)
    for stu in result:
        if int(stu[0]) == student_id: 
            conn = dbInit.connect_mysql()
            cur = conn.cursor()
            sql = 'update student set class_id = class_id '+ ' ^ %s where id = %s'
            value=[2**class_id,student_id]

            try:
                cur.execute(sql,value)
            except MySQLdb.Error,e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            conn.commit()
            cur.close()
            conn.close()

def get_by_id(id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from student '+ 'WHERE id=%s'
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

def isExist(username):
	if get_by_username(username) == None:
		return False
	else:
		return True

def change_flower_num(action,id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'update student set flower_num = flower_num {0} where id = {1}'.format(action,id)
    # value=[action,id]
    try:
        # cur.execute(sql,value)
        cur.execute(sql)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    # register("test11","abc","110","哈哈",Nickname="测试")
    change_flower_num("+1",1)
    # update_info("test",Password="fdaf")
    # print get_by_trainer_id(2)
    # print get_by_id(1)
    # print get_by_trainer_id(3)
    # add_trainer_by_id(3,1)
    # remove_trainer_by_id(3,1)
    # add_class_by_id(2,1)
    # remove_class_by_id(2,1)
    # print get_by_class_id(2)
    pass