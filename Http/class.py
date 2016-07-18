#-*-coding:utf-8-*- 
import web
import traceback, json
# import MySQL.tableStudent as Student
import MySQL.tableTrainer as Trainer
# import MySQL.tableRelation as Relation
# import MySQL.tableHistory as History
import MySQL.tableTask as Task
import MySQL.tableClass as tableClass


class show_trainers:
	'''return  trainer of  class  '''
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0,"info_of_trainer":[]}
		try:
			class_id = data.class_id
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			trainer_list = Trainer.get_by_class_id(class_id)
			if trainer_list:
				for trainer_info in trainer_list:
					username_nickname = {}
					username_nickname['trainer_id']=trainer_info[0]
					username_nickname["username"]=trainer_info[1]
					username_nickname["nickname"]=trainer_info[5]
					return_data["info_of_trainer"].append(username_nickname)
				return_data["success"]=1
			else:
				return_data['error_code']=701
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class get_info:
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						"class_info":{}
						}
		try:
		    class_id = data.class_id  
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
		    result = tableClass.get_by_id(class_id)
		    if result:
		    	class_info = {}
		    	class_info['cate_id'] = result[1]
		    	class_info['class_name'] = result[2]
		    	class_info['detail'] = result[3]
		    	class_info['target'] = result[4]
		    	class_info['basis'] = result[5]
		    	class_info['project'] = result[6]
		    	class_info['goal'] = result[7]
		    	class_info['plan'] = result[8]
		    	class_info['charge'] = result[9]
		    	class_info['idea'] = result[10]
		    	class_info['practice_plan'] = result[11]
		    	class_info['teaching_demand'] = result[12]
		    	return_data['class_info'] = class_info
		    	return_data['success'] = 1
		    else:
			    return_data["error_code"]=701
		except:
		    f=open("log.txt",'a')
		    traceback.print_exc(file=f)
		    f.flush()
		    f.close()
		    return_data["error_code"] = 102
		    # return json.dumps(return_data)
		finally:
		    return json.dumps(return_data)


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