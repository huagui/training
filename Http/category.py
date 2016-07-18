#-*-coding:utf-8-*- 
import web
import traceback, json
# import MySQL.tableStudent as Student
# import MySQL.tableTrainer as Trainer
# import MySQL.tableRelation as Relation
# import MySQL.tableHistory as History
import MySQL.tableCategory as Category
import MySQL.tableClass as tableClass
import MySQL.tableTask as Task


class get_all_categories:
	def GET(self):
		return_data = { "success":0, "error_code":0,
						"categories":[]
						}


		try:
		    categories = Category.get_all_cate()
		    for cate in categories:
		    	cate_info = {}
		    	cate_info['cate_id'] = cate[0]
		    	cate_info['cate_name'] = cate[1]
		    	cate_info['cate_detail'] = cate[2]
		    	return_data['categories'].append(cate_info)
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

class get_class:
	def GET(self):
		data = web.input()
		return_data = { "success":0, "error_code":0,
						"class":[]
						}
		try:
		    cate_id = data.cate_id
		except:
		    return_data["error_code"]=101
		    return json.dumps(return_data)

		try:
			if Category.get_by_id(cate_id):
			    classes = tableClass.get_by_cate_id(cate_id)
			    for key in classes:
			    	class_info = {}
			    	class_info['class_id'] = key[0]
			    	class_info['class_name'] = key[2]
			    	class_info['class_detail'] = key[3]
			    	return_data['class'].append(class_info)
			    return_data['success'] = 1
			else:
				return_data['error_code'] = 601
		except:
		    f=open("log.txt",'a')
		    traceback.print_exc(file=f)
		    f.flush()
		    f.close()
		    return_data["error_code"] = 102
		    # return json.dumps(return_data)
		finally:
		    return json.dumps(return_data)