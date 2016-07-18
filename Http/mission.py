#-*-coding:utf-8-*- 
import web
import traceback, json
# import MySQL.tableStudent as Student
# import MySQL.tableTrainer as Trainer
# import MySQL.tableRelation as Relation
# import MySQL.tableHistory as History
import MySQL.tableTask as Task


class get_info:
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						"info":{}
						}
		try:
		    task_id = data.task_id  
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
		    task_info = Task.get_by_id(task_id)
		    if task_info != None:
			    t_info = {"task_id":task_id,
			    			"title":task_info[1],
			    			"content":task_info[2],
			    			"cost":task_info[3],
			    			"materials":task_info[6],
			    			"guide":task_info[7],
			    			"guide_num":task_info[8],
			    			"required_hour":task_info[9],

			    			}
			    return_data["info"]=t_info
			    return_data["success"]=1
			    # return json.dumps(return_data)
		    else:
			    return_data["error_code"]=401
		except:
		    f=open("log.txt",'a')
		    traceback.print_exc(file=f)
		    f.flush()
		    f.close()
		    return_data["error_code"] = 102
		    # return json.dumps(return_data)
		finally:
		    return json.dumps(return_data)