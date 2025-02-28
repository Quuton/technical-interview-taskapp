from datetime import datetime
from exceptions import InvalidPriorityException, InvalidStatusException

class Task:
    PRIORITY_LOW = "low"
    PRIORITY_MEDIUM = "medium"
    PRIORITY_HIGH = "high"
    STATUS_PENDING = "pending"
    STATUS_INPROGRESS = "inprogress"
    STATUS_COMPLETED = "completed"

    def __init__(self, title:str, description:str, due_date:datetime, priority:str, status:str):
        self.task_id = None
        self.title = title
        self.description = description
        self.due_date = due_date
        self.set_priority(priority)
        self.set_status(status)
        self.creation_time = datetime.now()

    def update_details(self, title:str, description:str, due_date:datetime, priority:str, status:str):
        """
        This function allows setting priority for this class. It makes sure that the values are valid.

        Arguments:
            priority:str

        Returns:
            Nothing
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.set_priority(priority)
        self.set_status(status)

    def set_priority(self, priority:str):
        """
        This function allows setting priority for this class. It makes sure that the values are valid.

        Arguments:
            priority:str

        Returns:
            Nothing
        """
        priority = priority.lower()
        if priority != Task.PRIORITY_LOW and priority != Task.PRIORITY_MEDIUM and priority != Task.PRIORITY_HIGH:
            raise InvalidPriorityException
        self.priority = priority

    def set_status(self, status:str):
        """
        This function allows setting status for this class. It also makes sure that the values are valid.

        Arguments:
            status:str

        Returns:
            Nothing
        """
        status = status.lower()
        if status != Task.STATUS_PENDING and status != Task.STATUS_INPROGRESS and status != Task.STATUS_COMPLETED:
            raise InvalidStatusException
        self.status = status