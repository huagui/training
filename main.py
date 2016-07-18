#-*-coding:utf-8-*- 
import web
import time
import datetime
# import MySQL.tableStudent
import traceback
import Http.student
import Http.trainer
import Http.mission
import Http.notification
import Http.message
import logging


# create logger with 'spam_application'
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('hg.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -\n %(message)s \n')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# urls about student
urls = (
        '/student/register','Http.student.register',
        '/student/get_info','Http.student.get_info',
        '/student/auth','Http.student.auth',
        # '/student/get_trainer','Http.student.get_trainer',
        '/student/update_info','Http.student.update_info',
        # '/student/accept_mission','Http.student.accept_mission',
        '/student/finish_mission','Http.student.finish_mission',
        '/student/ask_for_trainer', 'Http.student.ask_for_trainer',
        '/student/get_history', 'Http.student.get_history',
        '/student/get_class','Http.student.get_class',
        '/student/ask_question','Http.student.ask_question',
        # '/student/join_class','Http.student.join_class',
        )

# urls about trainer
urls += (
        '/trainer/register','Http.trainer.register',
        '/trainer/get_info','Http.trainer.get_info',
        '/trainer/auth','Http.trainer.auth',
        # '/trainer/accept_student', 'Http.trainer.accept_student',
        '/trainer/get_student','Http.trainer.get_student',
        # '/trainer/get_requesters','Http.trainer.get_requesters',
        '/trainer/grade_mission','Http.trainer.grade_mission',
        '/trainer/send_mission','Http.trainer.send_mission',
        '/trainer/update_info','Http.trainer.update_info',
        # '/trainer/get_unsent_mission','Http.trainer.get_unsent_mission',
        '/trainer/get_class','Http.trainer.get_class',
        '/trainer/join_class','Http.trainer.join_class',
        
        )

# urls about category
urls += (
        '/category/get_all_categories', "Http.category.get_all_categories",
        '/category/get_class','Http.category.get_class',

  )

# urls about mission
urls += (
        '/mission/get_info','Http.mission.get_info',
       )

# urls about class
urls += (
        '/class/get_info','Http.class.get_info',
        '/class/show_trainers','Http.class.show_trainers',

  )

# urls about notification
urls += (
        '/notification/get_info','Http.notification.get_info',
        '/notification/handle','Http.notification.handle',
  )

# urls about comment
urls += (
         '/comment/write_comment','Http.comment.write_comment',
         '/comment/get_comment','Http.comment.get_comment',

)

# urls about message
urls += (
          '/message/send_message','Http.message.send_message',
        '/message/get_message','Http.message.get_message',

)
      
web.webapi.internalerror = web.debugerror #show debug info
if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
  
