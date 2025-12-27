class Node:
    def __init__(self, task):
        self.task = task
        self.next = None    
class ToDoList:
    def __init__(self):
        self.head = None
        

    def add_task(self, task):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node
    def show_tasks(self):
        current = self.head
        
        while current:
            print(current.task)
            current = current.next
todo=ToDoList()
todo.add_task("Buy groceries")
todo.add_task("Walk the dog")
todo.add_task("Read a book")
print("The Todo list of a student in learning are")
todo.show_tasks()
      

       