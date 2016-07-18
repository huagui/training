import web
import json
import traceback, json
import MySQL.tableStudent as Student
# import MySQL.tableTrainer as Trainer
# import MySQL.tableRelation as Relation
import MySQL.tableHistory as History
import MySQL.tableTask as Task

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
                        # return student_id
                        # student_id = Student.get_by_username(stu_username)[0]
                        return Student.get_by_username(stu_username)
                        if student_id != None and task_title != None:
                                task_id = Task.get_by_title(task_title)
                                return task_id,student_id
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