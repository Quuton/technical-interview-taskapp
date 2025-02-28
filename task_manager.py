import config
from util import convert_document_to_task
from task import Task
class TaskManager:
    def __init__(self, database_manager):
        self.database_manager = database_manager
        self.collection = self.database_manager.database[config.TASK_COLLECTION_NAME]

    def add_task(self, task:Task):
        """
        This function communicates with the Database to add a task object, it also returns the newly created task.

        Arguments:
            task:Task

        Returns:
            Task
        """
        data = {
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "priority": task.priority,
            "status": task.status,
            "creation_time": task.creation_time
        }
        result = self.collection.insert_one(data)
        task.id = result.inserted_id
        return task

    def find_task(self, task_id:str):
        """
        This function communicates with the Database to find a task object, it returns the result or None if it does not exist.

        Arguments:
            task:Task

        Returns:
            Task | None
        """
        task = self.collection.find_one({"_id": task_id})
        if task != None:
            return task
        else:
            return None

    def list_tasks(self, filter = None, value = None):
        """
        This function takes a filter string, and a value. It finds records where a field matching the filter also matches the value.

        Arguments:
            filter:str
            value:str

        Returns:
            List[Task]
        """
        if filter and value:
            documents = self.collection.find({filter: value})
        else:
            documents = self.collection.find()
        return [convert_document_to_task(document) for document in documents]

    def list_all_task_ids(self):
        """
        This function simply returns all documents's ids. This is for a dropdown feature in the interface.

        Arguments:
            Nothing

        Returns:
            List[str]
        """
        documents = self.collection.find()
        return [str(document["_id"]) for document in documents]

    def update_task(self, task:Task):
        if task.task_id == None:
            return
        data = {
            "title": task.title,
            "description": task.description,
            "due_date" : task.due_date,
            "priority": task.priority,
            "status": task.status,
        }
        self.collection.update_one({"_id": task_id}, {"$set": data})

    def mark_completed(self, task_id:str):
        self.collection.update_one({"_id": task_id}, {"$set": {"status":Task.STATUS_COMPLETED}})

    def delete_task(self, task_id:str):
        self.collection.delete_one({"_id": task_id})