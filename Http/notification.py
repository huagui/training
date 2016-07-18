#-*-coding:utf-8-*- 
import web
import traceback, json
import MySQL.tableStudent as Student
import MySQL.tableTrainer as Trainer
import MySQL.tableRelation as Relation
# import MySQL.tableHistory as History
# import MySQL.tableTask as Task
# import MySQL.tableClass as tableClass
import MySQL.tableNotification as Notification
import MySQL.tableQuestion as Question



class get_info:
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						"notification_list":[]
						}
		try:
			user_type = data.user_type
			target_id = data.target_id
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			notification_list = Notification.get_by_target_id(user_type,target_id)
			if notification_list:
				for key in notification_list:
					notification_info = {}
					notification_info['id']=key[0]
					notification_info['content'] = key[3]

					return_data['notification_list'].append(notification_info)
			return_data['success'] = 1
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
			# return json.dumps(return_data)
		finally:
			return json.dumps(return_data)

class handle:
	def GET(self):
		data = web.input(agreement=2,
						 reply=None,
			)
		return_data = {"success":0, "error_code":0}
		try:
			notification_id = data.notification_id
			agreement = int(data.agreement)
			reply = data.reply
		except:
			return_data["error_code"]=101
			return json.dumps(return_data)

		try:
			notification = Notification.get_by_id(notification_id)
			if notification:
				relation_id = notification[5]
				relation_info = Relation.get_by_id(relation_id)
				
				if notification[6]==1: #通知类型为学员申请,教练接受学员申请：修改通知和relation的状态
					
					if agreement==1:
						Relation.update_status(relation_id)
						# Notification.update_status(notification_id)
						Notification.remove_notification(notification_id)
						
						#设置回复信息，对象为学员
						Notification.set_notification(1,relation_info[2],reply,relation_id,3,agreement)
						return_data["success"]=1
					elif agreement==0:
						# Relation.remove_by_id(relation_id)
						Notification.remove_notification(notification_id)
						Notification.set_notification(1,relation_info[2],reply,relation_id,3,agreement)
						return_data["success"]=1

					else:
						return_data["error_code"]=101

				if notification[6]==5: #通知类型为指导通知,教练确认完成指导：修改question表的教练确认字段，发送通知给学员，删除通知
					if agreement==1:
						Question.update_by_relation_id(relation_id)
						reply = "教练确认已完成了对您的手把手的指导，请您确认并给予这次指导的评价。如果教练未完成指导，请点击投诉，教练缘平台会联系教练并及时给您答复。"
						Notification.set_notification(1,relation_info[2],reply,relation_id,6)
						Notification.remove_notification(notification_id)
						return_data["success"]=1
				
				if notification[6]==6: #通知类型为指导通知,学员确认完成指导：删除question表记录，发送鲜花给教练，并评论教练，删除通知
					if agreement==1:
						question_info = Question.get_by_relation_id(relation_id)
						flower_num = question_info[7]
						Question.remove_by_relation_id(relation_id)
						exchange_flower(flower_num,relation_info[2],relation_info[1])
						Notification.remove_notification(notification_id)
						return_data["success"]=1
			else:
				return_data["error_code"]=802
		except:
			f=open("log.txt",'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
			return_data["error_code"] = 102
		finally:
			return json.dumps(return_data)



def exchange_flower(flower_num,student_id,trainer_id):
	Student.change_flower_num('-'+str(flower_num) , student_id)
	Trainer.change_flower_num('+'+str(flower_num), trainer_id)