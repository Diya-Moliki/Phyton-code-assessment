our previous Python 3 content is preserved below:
# 
# def say_hello():
#     print('Hello, World')
# 
# for i in range(5):
#     say_hello()
# 
# 
# # 
# # Your previous Python 2 content is preserved below:
# # 
# # # The Problem:
# # 
# # # We have a list of tasks. Each task can depend on other tasks. 
# # # For example if task A depends on task B then B should run before A.
# #  
# # # Implement the "get_task_with_dependencies" method such that it returns a list of task names in the correct order.
# #  
# # # For example if I want to execute task "application A", the method should return a list with "storage,mongo,application A".
# # 
# # # List of Tasks:
# # 
# # #   - name: application A
# # #     dependsOn:
# # #       - mongo
# # 
# # #   - name: storage
# # 
# # #   - name: mongo
# # #     dependsOn:
# # #       - storage
# # 
# # #   - name: memcache
# # 
# # #   - name: application B
# # #     dependsOn:
# # #       - memcache
# # 
# # # The python program is expected to be executed succesfully.
# # 
import unittest

class Task():
    def _init_(self, name, dependsOn=[]):
        self.name = name
        self.dependsOn = dependsOn
        
class TaskList():
    def get_tasks(self):
        return [
           Task("application A", ["mongo"]),
           Task("storage"),
           Task("mongo", ["storage"]),
           Task("memcache"),
           Task("application B", ["memcache"]),
        ]

class Solution(unittest.TestCase):
    def get_task_with_dependencies(self, tasks, dependsOn):
        resultString=""
        task=[]
        
        for i in range(len(tasks)):
            name=tasks[i].name
            if(dependsOn==name):
                task=tasks[i]
                break
                
        if (task.dependsOn != [] ):
            for newDependsOn in task.dependsOn:
                    res = self.get_task_with_dependencies(tasks, newDependsOn)
                    for ele in res :
                        resultString+=(ele+',');
        
        resultString+=dependsOn;
        return resultString.split(",");
        
    
    def test_get_task_dependencies_for_application_A(self):
        self.assertEqual(
            self.get_task_with_dependencies(TaskList().get_tasks(), "application A"),
            ["storage", "mongo", "application A"]
        )

unittest.main(exit=False)
 
#
