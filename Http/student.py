#-*-coding:utf-8-*- 
import web
import traceback, json
import MySQL.tableStudent as Student
import MySQL.tableTrainer as Trainer
import MySQL.tableRelation as Relation
import MySQL.tableHistory as History
import MySQL.tableTask as Task
import MySQL.tableClass as tableClass
import MySQL.tableNotification as Notification
import MySQL.tableQuestion as Question
import logging
import time

import sys 
sys.path.append("..")
import setting

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
module_logger = logging.getLogger("main.student")

class register:
    def GET(self):
        data = web.input(
                        phone = None,
                        about = None, 
                        )
        return_data = { "success":0, "error_code":0 }
        try:
            username = data.username
            password = data.password
            phone = data.phone
            about = data.about
            nickname = data.nickname
           
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            code = 201 if Student.isExist(username) else 0 #用户名已被注册
            if code == 201:
            	return_data["error_code"]=201
            	return json.dumps(return_data)
            else:
	            try:
	            	Student.register(username,password,phone,about,nickname)
	            	return_data["success"]=1
	            except:
	                f=open("log.txt",'a')
	                traceback.print_exc(file=f)
	                f.flush()
	                f.close()
	                return_data["error_code"] = 103
	            finally:
	                return json.dumps(return_data)         
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

class get_info:

	def GET(self):
		data = web.input(
			username = None, #为了兼容格源的版本
			student_id = None,
			)
		return_data = { "success":0, "error_code":0,
						"info":{}, "trainers":[],
						}
		try:
		    username = data.username  
		    student_id = data.student_id
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
			if username:
				student_info = Student.get_by_username(username)
			if student_id:
				student_info = Student.get_by_id(student_id)
			stu_info = {"username":student_info[1],
		    			"phone":student_info[3],
		    			"about":student_info[4],
		    			"nickname":student_info[5],
		    			"student_id":student_info[0],
		    			
		    			}
			relation_list = Relation.get_by_student(student_info[0])
			for key in relation_list:
				trainer_info = {}
				trainer_info["trainer_id"] = key[1]
				trainer_info["class_id"] = key[3]
				trainer_info["trainer_name"] = Trainer.get_by_id(key[1])[5]
				return_data["trainers"].append(trainer_info)
		 
			return_data["info"]=stu_info
			return_data["success"]=1
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class update_info:

	def GET(self):
		data = web.input( old_password=None,
						  new_password=None,
						  phone=None,
						  about=None,
						  nickname=None,
			)
		return_data = { "success":0, "error_code":0	}

		try:
			student_id = int(data.student_id)
			old_password = data.old_password
			new_password = data.new_password
			phone = data.phone
			about = data.about
			nickname = data.nickname
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			student_info = Student.get_by_id(student_id)
			if old_password and old_password != student_info[2]:
				return_data["error_code"] = 208
			elif new_password and not old_password:
				return_data["error_code"] = 208
			else:
				Student.update_info(student_id,new_password,phone,about,nickname)
				return_data["success"] = 1
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class auth:
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,}
		try:
		    username = data.username
		    password = data.password
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
		    student_info = Student.get_by_username(username)
		    if student_info == None:
		    	return_data["error_code"]=202
		    else:
			    if password == student_info[2]:
			    	return_data["success"]=1
			    else:
			    	return_data["error_code"]=203
			    	return_data["success"]=0
		except:
		    f=open("log.txt",'a')
		    traceback.print_exc(file=f)
		    f.flush()
		    f.close()
		    return_data["error_code"] = 102
		finally:
		    return json.dumps(return_data)

class ask_for_trainer:
	'''
	申请教练：传入学员用户名，教练用户名，班级id
	记录到relation表，状态置0；并设置通知，对象为该教练
	'''
	def GET(self):
		data = web.input(reason='',
						 about='',
						)
		return_data = {"success":0, "error_code":0}
		try:
		    stu_username = data.stu_username
		    tra_username = data.tra_username
		    class_id = data.class_id
		    reason = data.reason
		    about = data.about

		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
		    student_info = Student.get_by_username(stu_username)
		    trainer_info = Trainer.get_by_username(tra_username)
		    class_info = tableClass.get_by_id(class_id)
		    if class_info:

			    if student_info == None or trainer_info==None:		    	
			        return_data["error_code"]=202
			    else:
				    Relation.record(trainer_info[0],student_info[0], class_id)
				    relation_info = Relation.get_by_three_id(trainer_info[0],student_info[0],class_id)
				    relation_id = relation_info[0]
				    if relation_info[4]==1: #status 为1 ，关系已建立 
				    	return_data['error_code']=206
				    else:

					    if relation_id:
						    noti_string = "学员：" + str(student_info[5]) + "\n"
						    noti_string += "班级：" + class_info[2] + '\n'
						    noti_string += "申请理由：" + reason + '\n'
						    noti_string += "自我介绍：" + about +'\n'
						    #设置通知，通知类型为1（学员申请）
						    Notification.set_notification(2,trainer_info[0],noti_string,relation_id,msg_type=1)
						    return_data["success"]=1
					    else:
							return_data['error_code']=102
		    else:
			    return_data['error_code'] = 701
			    
		except:
		    f=open("log.txt",'a')
		    traceback.print_exc(file=f)
		    f.flush()
		    f.close()
		    return_data["error_code"] = 102
		finally:
		    return json.dumps(return_data)

class ask_question:
	def GET(self):
		data = web.input(flower_num=10)
		return_data = { "success":0, "error_code":0	}

		try:
			student_id = int(data.student_id)
			trainer_id = int(data.trainer_id)
			class_id = int(data.class_id)
			task_id = int(data.task_id)
			content = data.content
			flower_num = int(data.flower_num)
			stu_name = data.stu_name
			phone = int(data.phone)
			qq = int(data.qq)
		except:
			return_data["error_code"] = 101
			return json.dumps(return_data)

		try:
			relation_info = Relation.get_by_three_id(trainer_id,student_id,class_id)
			if relation_info:
				current_time = time.strftime(TIMEFORMAT, time.localtime())
				Question.set_question(content,current_time,relation_info[0],stu_name,phone,qq,flower_num)

				noti_string = "班级：" + tableClass.get_by_id(class_id)[2] + '\n'
				noti_string += "学员：" + Student.get_by_id(student_id)[5] + '\n'
				noti_string += "真实姓名：" + stu_name + '\n'
				noti_string += "项目名称：" + Task.get_by_id(task_id)[1] + '\n'
				noti_string += "赠送鲜花：" + str(flower_num) + "支\n"
				noti_string += "问题概述：" + content +'\n'
				noti_string += "联系电话：" + str(phone) + "\n"
				noti_string += "QQ：" + str(qq) + '\n'
				noti_string += "申请时间：" + current_time + '\n'
				noti_string += "要求：请在24小时内对学员手把手指导\n" 
				Notification.set_notification(2,trainer_id,noti_string,relation_info[0],msg_type=5)

				return_data['success']=1
			else:
				return_data['error_code'] = 209
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class get_history:
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0,"task_history":[]}
		try:
		    username = data.username
		    class_id = data.class_id
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
		    student_info = Student.get_by_username(username)
		    if student_info == None:		    	
		    	return_data["error_code"]=202
		    else:
		    	history_list = History.get_by_student_class_id(student_info[0],class_id)
		    	return_data["nickname"]=student_info[5]
		    	for history in history_list:
		    		try:
		    			title =  Task.get_by_id(history[1])[1]
		    		except: pass 
		    		item={}
		    		item["task_title"]=str(title)
		    		# date_time.strftime('%Y-%m-%d')
		    		item["task_id"] = history[1]
		    		if history[3]==None:
		    			item["finish_time"]="000-00-00 00:00:00"
		    		else:
		    			item["finish_time"]=history[3].strftime(TIMEFORMAT)
		    		item["status"]=history[4]
		    		return_data["task_history"].append(item)
		    	return_data["success"]=1
		    # return json.dumps(return_data)
		except:
		    f=open("log.txt",'a')
		    traceback.print_exc(file=f)
		    f.flush()
		    f.close()
		    return_data["error_code"] = 102
		finally:
		    return json.dumps(return_data)

class finish_mission:
	'''
	学员提交任务，传入username,task_id
	修改 history 表的状态，设置通知，对象为教练
	'''
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0,}
		try:
			username = data.username
			task_id = data.task_id
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			student_info = Student.get_by_username(username)
			task_info = Task.get_by_id(task_id)
			if task_info:
				if student_info == None:
					return_data["error_code"]=202
				else:
					#更新任务状态
					History.update_info(task_id,student_info[0],Finish=1)
					relation_info = Relation.get_by_student_id(student_info[0],task_info[4])
					# return student_info[0], task_info[4]
					relation_id = relation_info[0][0]
					noti_string = "学员：" + str(student_info[5]) + "\n"
					noti_string += "完成任务：" + task_info[2] + '\n'
					#设置通知，通知类型为2（学员提交任务）
					# return relation_info
					Notification.set_notification(2,relation_info[0][1],noti_string,relation_id,msg_type=2)
					return_data["success"]=1
			else:
				return_data["error_code"]=401
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class get_class:
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						"class":[]
						}
		try:
		    student_id = data.student_id  
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
			student_info = Student.get_by_id(student_id)
			if student_info:
				
				class_list = Relation.get_by_student(student_info[0])
				for key in class_list:
					class_id_name = {}
					class_id_name["class_id"] = key[3]
					class_id_name['class_name'] = tableClass.get_by_id(key[3])[2]
					return_data['class'].append(class_id_name)
				return_data['success']=1
			else:
				return_data["error_code"]=202

		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class join_class:
	'''
	学员加入班级，传入学员id，班级id，建立学员与班级的对应关系，
	并分发该班级中对应的第一个任务给该学员
	'''
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						}
		try:
		    student_id = data.student_id
		    class_id = data.class_id
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
			Student.add_class_by_id(class_id,student_id)
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102

		try:
			task_list = Task.get_by_class_id(class_id) #获取对应班级中的所有任务
			task_id = 0
			for task in task_list: #获取序号为1的任务的任务id
				if task[5]==1:
					task_id = task[5]
			History.record(task_id,student_id,class_id) #分发任务，即添加到history表
			return_data["success"]=1
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)
