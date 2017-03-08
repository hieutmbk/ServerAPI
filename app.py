from flask import Flask
import mlab
from models.task import Task
from flask_restful import Api
from resources.task_resource import *

mlab.connect()
app = Flask(__name__)
api = Api(app)

# all_task = Task.objects()
# for task in all_task:
#     print(mlab.item2json(task))

# my_task = Task.objects(name="HuyMad_Quan xinh gai,ot cong").first()
# print(mlab.item2json(my_task))
#
# my_task.delete()

api.add_resource(TaskListRes,"/tasks")
api.add_resource(TaskRes,"/tasks/<task_id>")

if __name__ == '__main__':
    app.run()
