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


class register:
    def GET(self):
        data = web.input(
                        phone = '',
                        about = '', 
                        )
        return_data = { "success":0, "error_code":0}
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
            code = 201 if Trainer.isExist(username) else 0 #用户名已被注册
            if code == 201:
            	return_data["error_code"]=201
            	return json.dumps(return_data)
            else:
	            try:
	            	Trainer.register(username,password,phone,about,nickname)
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
			username = None,
			trainer_id = None, #为了兼容格源的版本
			)
		return_data = { "success":0, "error_code":0,
						"info":{}
						}
		try:
		    username = data.username
		    trainer_id = data.trainer_id
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
			if username:
			    trainer_info = Trainer.get_by_username(username)
			if trainer_id:
			    trainer_info = Trainer.get_by_id(trainer_id)
			trainer_info = {
		    			'trainer_id':trainer_info[0],
		    			"username":trainer_info[1],
		    			"phone":trainer_info[3],
		    			"about":trainer_info[4],
		    			"nickname":trainer_info[5],
		    			}
			return_data["info"]=trainer_info
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
			trainer_id = int(data.trainer_id)
			old_password = data.old_password
			new_password = data.new_password
			phone = data.phone
			about = data.about
			nickname = data.nickname
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			trainer_info = Trainer.get_by_id(trainer_id)
			if old_password and old_password != trainer_info[2]:
				return_data["error_code"] = 208
			elif new_password and not old_password:
				return_data["error_code"] = 208
			else:
				Trainer.update_info(trainer_id,new_password,phone,about,nickname)
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
		    trainer_info = Trainer.get_by_username(username)
		    if trainer_info == None:
		    	return_data["error_code"]=202
		    else:
			    if password == trainer_info[2]:
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

# class accept_student:
# 	'''
# 	教练接受学员申请：修改通知和relation的状态
# 	'''
# 	def GET(self):
# 		data = web.input()
# 		return_data = {"success":0, "error_code":0}
# 		try:
# 		    notification_id = data.notification_id
# 		except:
# 		    return_data["error_code"]=101
# 		    return json.dumps(return_data)

# 		try:
# 		    notification = Notification.get_by_id(notification_id)
# 		    if notification:
# 			    relation_id = notification[5]
# 			    Relation.update_status(relation_id)
# 			    Notification.update_status(notification_id)
# 			    return_data["success"]=1
# 		    else:
# 		    	return_data["error_code"]=802
			    
# 		except:
# 		    f=open("log.txt",'a')
# 		    traceback.print_exc(file=f)
# 		    f.flush()
# 		    f.close()
# 		    return_data["error_code"] = 102
# 		finally:
# 		    return json.dumps(return_data)


class get_student:
	'''
	获取对应班级下的学员
	'''
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0,"student_list":[]}
		try:
		    username = data.username
		    class_id = data.class_id
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
		    trainer_info = Trainer.get_by_username(username)
		    if trainer_info == None:		    	
		    	return_data["error_code"]=202
		    else:
			    trainer_id = trainer_info[0]
			    class_info = tableClass.get_by_id(class_id)
			    if class_info:
				    # return trainer_id,class_info[0]
				    relation_list = Relation.get_by_trainer_id(trainer_id,class_info[0])

				    if relation_list:
				    	for relation in relation_list:
				    		stu_id = relation[2]
				    		stu = Student.get_by_id(stu_id)
				    		username_nickname={}
				    		username_nickname['id']=stu_id
				    		username_nickname["username"]=stu[1]
				    		username_nickname["nickname"]=stu[5]
				    		return_data["student_list"].append(username_nickname)
				    return_data["success"]=1
				    # else:
				    #     return_data["error_code"]=301
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


class get_requesters:
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0,"info_of_requesters":[]}

		try:
			username = data.username
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			trainer_id = Trainer.get_by_username(username)[0]

			if trainer_id == None:		    	
				return_data["error_code"]=202
			else:
				requesters_list = Relation.get_by_trainer_id(trainer_id)

				if requesters_list:
					stu_id_list=[]

					for req in requesters_list:
						if req[2] == 0:
							stu_id_list.append(req[0])
					for stu_id in stu_id_list:
						stu_info = Student.get_by_id(stu_id)
						username_nickname = {}
						username_nickname["username"]=stu_info[1]
						username_nickname["nickname"]=stu_info[5]
						return_data["info_of_requesters"].append(username_nickname)
					return_data["success"]=1 
				else:
					return_data["error_code"]=301
	
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class grade_mission:
	'''
	教练打分，传入学员username,task_id,point，打分之后为该学员分发当前班级的下一个任务
	'''
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0,}
		try:
			username = data.username
			task_id = data.task_id
			point = data.point
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
					if History.get_by_student_task_id(student_info[0],task_id)[4] == 2: #任务处于提交状态
						History.update_info(task_id,student_info[0],point,Grade=1)
						try:
							class_id = task_info[4]
							num = task_info[5]
							next_task_id = Task.get_next_task(class_id,num)[0] #获取该班级下一个任务的task_id
							if next_task_id: 
								History.record(next_task_id,student_info[0],class_id) #分发下一个任务
								relation_info = Relation.get_by_student_id(student_info[0],task_info[4])
								
							else: #学员提交的是最后一个任务
								pass
							#删除给教练的通知
							Notification.remove_by_relation_id(relation_info[0][0])
							return_data["success"]=1
						except:
							f=open("log.txt",'a')
							traceback.print_exc(file=f)
							f.flush()
							f.close()
							return_data['error_code']=503
							
					else:
						return_data['error_code']=502
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

class send_mission:
        def GET(self):
                data = web.input()
                return_data = {"success":0, "error_code":0}
                try:
                        stu_username = data.stu_username
                        task_title = data.task_title
                except:
                        return_data["error_code"]=101
                        return json.dumps(return_data)

                try:
                        student_id = Student.get_by_username(stu_username)[0]
                        
                        if student_id != None and task_title != None:
                                task_id = Task.get_by_title(task_title)[0]
                                History.record(task_id, student_id)
                                return_data["success"]=1
                        elif student_id == None:
                                return_data["error_code"]=202
                except:
                        f=open("log.txt",'a')
                        traceback.print_exc(file=f)
                        f.flush()
                        f.close()
                        return_data["error_code"] = 102
                finally:
                        return json.dumps(return_data)


class get_unsent_mission:
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0,"unsent_task":[]}
		try:
		    stu_username = data.stu_username
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
		    student_info = Student.get_by_username(stu_username)
		    if student_info == None:		    	
		    	return_data["error_code"]=202
		    else:
		    	history_list = History.get_by_student_id(student_info[0])
		    	all_task_info = Task.get_all()
		    	
		    	sent_task_id =[] #历史记录中发送过给学员的任务
		    	for i in history_list:
		    		sent_task_id.append(i[1])

		    	all_task_id = [] #所有任务，即任务表中的任务
		    	for i in all_task_info:
		    		all_task_id.append(i[0])

		    	unsent_task_id =[] #尚未发送给学员的任务
		    	for i in all_task_id:
		    		if i not in sent_task_id:
		    			unsent_task_id.append(i)


		    	for uid in unsent_task_id:
		    		try:
		    			task_info =  Task.get_by_id(uid)
		    		except: pass 
		    		item={}
		    		item["task_id"]=task_info[0]
		    		item["task_title"]=str(task_info[1])
		    		item["content"]=str(task_info[2])
		    		item["cost"]=str(task_info[3])
		    		return_data["unsent_task"].append(item)
		    	

		    	return_data["success"]=1
		    return json.dumps(return_data)
		except:
		    f=open("log.txt",'a')
		    traceback.print_exc(file=f)
		    f.flush()
		    f.close()
		    return_data["error_code"] = 102
		# finally:
		#     return json.dumps(return_data)


class get_class:
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						"class":[]
						}
		try:
		    trainer_id = data.trainer_id  
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
			# relation_list = Relation.get_by_trainer(trainer_id)

			# class_id_list = []
			# for key in relation_list:
			# 	class_id_list.append(key[3])
			# class_id_list = list(set(class_id_list))
			# for id in class_id_list:

			# 	class_info = tableClass.get_by_id(id)
			# 	class_id_name = {}
			# 	class_id_name["class_id"] = id
			# 	class_id_name['class_name'] = class_info[2]
			# 	return_data['class'].append(class_id_name)
			trainer_info = Trainer.get_by_id(trainer_id)
			if trainer_info:
				class_id_list = Trainer.dbInit.get_id_list(trainer_info[6])
				for key in class_id_list:
					class_info = tableClass.get_by_id(key)
					class_id_name = {}
					class_id_name["class_id"] = key
					class_id_name['class_name'] = class_info[2]
					return_data['class'].append(class_id_name)
				return_data['success']=1
			else:
				return_data['error_code']=202
			


		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
			# return json.dumps(return_data)
		finally:
			return json.dumps(return_data)


class join_class:
	'''
	教练任教班级，传入教练id，班级id，添加班级id，
	'''
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						}
		try:
		    trainer_id = data.trainer_id
		    class_id = data.class_id
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
			if tableClass.get_by_id(class_id):
				Trainer.add_class_by_id(class_id,trainer_id)
				return_data['success']=1
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