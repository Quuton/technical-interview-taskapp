from task_manager import TaskManager
from database import MongoDatabase
import gradio as gr
from task import Task
database = MongoDatabase()
task_manager = TaskManager(database)
existing_ids_list = task_manager.list_all_task_ids()

def add_new_task(title, description, due_date, priority, status):
    task = Task(title, description, due_date, priority, status)
    task_manager.add_task(task)
    print(f"DEBUG: TASK ADDED!")
    existing_ids_list = task_manager.list_all_task_ids()

def list_all_tasks(filter_field, key_value):
    task_manager.list_tasks(filter = filter_field, value = key_value)


def update_task(task_id, title, description, due_date, priority, status):
    task = Task(title, description, due_date, priority, status)
    task.task_id = task_id
    task_manager.update_task(task)

def mark_completed(task_id:str):
    task_manager.mark_completed(task_id)

def delete_task(task_id:str):
    task_manager.delete_task(task_id)
    existing_ids_list = task_manager.list_all_task_ids()

if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("### Task Management Application")
        
        with gr.Tab("Add Task"):
            with gr.Row():
                title = gr.Textbox(label = "Task Title")
                description = gr.Textbox(label = "Task Description")
                priority = gr.Dropdown(choices = [Task.PRIORITY_LOW, Task.PRIORITY_MEDIUM, Task.PRIORITY_HIGH], label = "Priority")
                status = gr.Dropdown(choices = [Task.STATUS_PENDING, Task.STATUS_INPROGRESS, Task.STATUS_COMPLETED], label = "Status")
                due_date = gr.DateTime(label = "Due Date")
            submit_button = gr.Button("Add Task")
            submit_button.click(add_new_task, inputs = [title, description, due_date, priority, status])
        
        with gr.Tab("List Tasks"):
            with gr.Row():
                filter_field = gr.Dropdown(choices = ["title", "description", "priority", "status"], label = "Filter field")
                key_value = gr.Textbox(label="Value")
            list_button = gr.Button("List Tasks")
            list_button.click(list_all_tasks, inputs=[filter_field, key_value])

        with gr.Tab("Update Task"):
            with gr.Row():
                task_id = gr.Textbox(label = "Task ID")
                title = gr.Textbox(label = "New Title")
                description = gr.Textbox(label = "New Description")
                priority = gr.Dropdown(choices = [Task.PRIORITY_LOW, Task.PRIORITY_MEDIUM, Task.PRIORITY_HIGH], label = "New Priority")
                status = gr.Dropdown(choices = [Task.STATUS_PENDING, Task.STATUS_INPROGRESS, Task.STATUS_COMPLETED], label = "New Status")
                due_date = gr.DateTime(label = "New Due Date")
            update_button = gr.Button("Update Task")
            update_button.click(update_task, inputs = [task_id, title, description, due_date, priority, status])
        
        with gr.Tab("Complete Task"):
            task_id = gr.Dropdown(choices = existing_ids_list)
            complete_button = gr.Button("Complete Task")
            complete_button.click(mark_completed, inputs=[task_id])
        
        with gr.Tab("Delete Task"):
            task_id = gr.Dropdown(choices = existing_ids_list)
            delete_button = gr.Button("Delete Task")
            delete_button.click(delete_task, inputs=[task_id])

    demo.launch()

    