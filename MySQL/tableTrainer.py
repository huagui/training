#-*-coding:utf-8-*- 
import MySQLdb
import dbInit

def register(Username, Password,
    Phone, About, Nickname):  

    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = """insert into trainer (username, password, phone,
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
	sql = 'select * from trainer '+ 'WHERE username=%s'
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
    Phone=None, About=None, Nickname=None):  

    conn = dbInit.connect_mysql()
    cur = conn.cursor()

    sql = 'update trainer set'

    if Password != None:
    	sql += ''' password="%s",'''%Password
    if Phone != None:
    	sql += ''' phone="%s",'''%Phone
    if About != None:
    	sql += ''' about="%s",'''%About
    if Nickname != None:
    	sql += ''' nickname="%s",'''%Nickname


    sql = sql[:-1] + ''' where id="%s"'''%id
     
    try:
        cur.execute(sql)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()

def isExist(username):
    if get_by_username(username) == None:
        return False
    else:
        return True


def add_class_by_id(class_id,trainer_id):
    class_id = int(class_id)
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'update trainer set class_id = class_id '+ ' | %s where id = %s'
    value=[2**class_id,trainer_id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    cur.close()
    conn.close()


def get_by_class_id(class_id):
    try:
        class_id = int(class_id)
    except:
        class_id = 0
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'select * from trainer '+ 'WHERE class_id & %s = %s'
    value=[2**class_id,2**class_id]

    try:
        cur.execute(sql,value)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def remove_class_by_id(class_id,trainer_id):
    '''
    若该教练有对应班级、则删除
    '''
    result = get_by_class_id(class_id)
    for trainer in result:
        if int(trainer[0]) == trainer_id: 
            conn = dbInit.connect_mysql()
            cur = conn.cursor()
            sql = 'update trainer set class_id = class_id '+ ' ^ %s where id = %s'
            value=[2**class_id,trainer_id]

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
    sql = 'select * from trainer '+ 'WHERE id=%s'
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
    sql = 'select * from trainer '
    
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

def change_flower_num(action,id):
    conn = dbInit.connect_mysql()
    cur = conn.cursor()
    sql = 'update trainer set flower_num = flower_num {0} where id = {1}'.format(action,id)
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
    # pass
    # print get_all()
    # remove_class_by_id(2,2)
    print get_by_class_id(3)
    # get_by_id(1)
	# update_info("tom","to1","1234770123",Nickname="雷")
	# update_info("test",Password="fdaf")
    pass