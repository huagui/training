#-*-coding:utf-8-*- 
import web
import traceback, json
import MySQL.tableStudent as Student
import MySQL.tableTrainer as Trainer
import MySQL.tableRelation as Relation
# import MySQL.tableHistory as History
# import MySQL.tableTask as Task
# import MySQL.tableClass as tableClass
# import MySQL.tableNotification as Notification
import MySQL.tableMessage as Message


class send_message:
	'''
	发送留言、通过studen_id,trainer_id,class_id获取relation_id,发送留言
	'''
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0}
		try:
			student_id = data.student_id
			trainer_id = data.trainer_id
			class_id = data .class_id
			content = data.content
			from_stu = data.from_stu
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			if from_stu == "1" or from_stu == "0":
				relation_info = Relation.get_by_three_id(trainer_id,student_id,class_id)
				if relation_info:
					Message.send_message(relation_info[0],from_stu,content)
					return_data['success']=1
				else:
					return_data["error_code"]=207
			else:
				return_data["error_code"]=101
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)

class get_message:
	'''
	获取留言、通过studen_id,trainer_id,class_id,from_stu获取对应留言
	'''
	def GET(self):
		data = web.input(num=None)
		return_data = {"success":0, "error_code":0, "message":[]}
		try:
			student_id = data.student_id
			trainer_id = data.trainer_id
			class_id = data .class_id
			num = int(data.num)
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			relation_info = Relation.get_by_three_id(trainer_id,student_id,class_id)
			if relation_info:
				message_list = Message.get_by_relation_id(relation_info[0],num)
				for item in message_list:
					message_info = {}
					message_info['from_stu'] = item[2]
					message_info['publish_time'] = "0000-00-00 00:00:00" if item[3]==None else item[3].strftime(Message.TIMEFORMAT)					
					message_info['content'] = item[4]
					return_data['message'].append(message_info)
				return_data['success']=1
			else:
				return_data["error_code"]=207
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)