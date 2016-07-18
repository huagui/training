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
# import MySQL.tableMessage as Message
import MySQL.tableComment as Comment

class write_comment:
	'''
	发送评论、记录studen_id,trainer_id,content
	'''
	def GET(self):
		data = web.input()
		return_data = {"success":0, "error_code":0}
		try:
			student_id = data.student_id
			trainer_id = data.trainer_id
			content = data.content
			class_id = data.class_id
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			if Relation.get_by_three_id(trainer_id,student_id, class_id):
				Comment.write_comment(student_id,trainer_id,content,class_id)
				return_data['success']=1
			else:
				return_data['error_code']=209
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)


class get_comment:
	'''
	获取教练对应的评论
	'''
	def GET(self):
		data = web.input(num=50)
		return_data = {"success":0, "error_code":0, "comment_list":[]}
		try:
			trainer_id = data.trainer_id
			num = int(data.num)
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			if Trainer.get_by_id(trainer_id):
				comment_list = Comment.get_by_trainer_id(trainer_id,num)
				for key in comment_list:
					comment_info = {}
					comment_info['id'] = key[0]
					comment_info['content'] = key[1]
					comment_info['student_id'] = key[2]
					comment_info['trainer_id'] = key[3]
					comment_info['pubish_time'] = key[4].strftime(Comment.TIMEFORMAT)
					comment_info['class_id'] = key[5]
					return_data['comment_list'].append(comment_info)
				return_data['success']=1
			else:
				return_data['error_code']=202
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)