from task import Task
def convert_document_to_task(document):
    task = Task(document["title"], document["description"], document["due_date"], document["priority"], document["status"])
    task.id = str(document["_id"])
    task.creation_time = document["creation_time"]
    return task