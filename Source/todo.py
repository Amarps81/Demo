from enum import Enum
from datetime import date

class Todo:
    class Status(Enum):
        OPEN = 1
        IN_PROGRESS = 2
        DONE = 3

    class Priority(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
    
    def __init__(self, title, description, status, priority, due_date=None):
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        return f"{self.title} | {self.description} | {self.status} | {self.priority} | {self.due_date}"

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)
    
    def remove(self, index):
        self.todos.pop(index)

class App:
    def __init__(self):
        self.todo_list = TodoList()
    
    def get_status(self):
        choice = None
        while choice not in ["1", "2", "3"]:
            print("1. Open")
            print("2. In Progress")
            print("3. Done")
            choice = input("Status: ")
            if choice not in ["1", "2", "3"]:
                print("Invalid choice!")
        if choice == "1":
            return Todo.Status.OPEN
        elif choice == "2":
            return Todo.Status.IN_PROGRESS
        elif choice == "3":
            return Todo.Status.DONE
        
    def get_priority(self):
        choice = None
        while choice not in ["1", "2", "3"]:
            print("1. Low")
            print("2. Medium")
            print("3. High")
            choice = input("Priority: ")
            if choice not in ["1", "2", "3"]:
                print("Invalid choice!")
        if choice == "1":
            return Todo.Priority.LOW
        elif choice == "2":
            return Todo.Priority.MEDIUM
        elif choice == "3":
            return Todo.Priority.HIGH
        
    def get_due_date(self):
        """Get a due date from the user.
           Due date must be a valid date.
        """
        due_date = None
        while not due_date:
            due_date_str = input("Due Date (YYYY-MM-DD): ")
            try:
                due_date = date.fromisoformat(due_date_str)
            except ValueError:
                print("Invalid date!")
        return due_date

    def add_todo(self):
        title = input("Title: ")
        description = input("Description: ")
        status = self.get_status()
        priority = self.get_priority()
        due_date = self.get_due_date()
        todo = Todo(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date
        )
        self.todo_list.add(todo)

    def _sorted(self, sort_by):
        if sort_by == "title":
            return sorted(self.todo_list.todos, key=lambda todo: todo.title)
        elif sort_by == "status":
            return sorted(self.todo_list.todos, key=lambda todo: todo.status.value)
        elif sort_by == "priority":
            return sorted(self.todo_list.todos, key=lambda todo: todo.priority.value)
        elif sort_by == "due_date":
            return sorted(self.todo_list.todos, key=lambda todo: todo.due_date)
        else:
            return self.todo_list.todos

    def list_todos(self, sort_by=None):
        choice = None
        while choice != "5":
            print()
            print("Todos")
            print("-----")
            print("Sorted by:", sort_by or "None")
            todos = self._sorted(sort_by)
            for todo in todos:
                print(todo)
            print()
            print("1. Sort by Title")
            print("2. Sort by Status")
            print("3. Sort by Priority")
            print("4. Sort by Due Date")
            print("5. Back")
            choice = input("How would you like to sort? ")
            if choice == "1":
                sort_by = "title"
            elif choice == "2":
                sort_by = "status"
            elif choice == "3":
                sort_by = "priority"
            elif choice == "4":
                sort_by = "due_date"
            elif choice == "5":
                return
            else:
                print("Invalid choice!")
        

    def remove_todo(self):
        for i, todo in enumerate(self.todo_list.todos):
            print(f"{i+1}. {todo.title}")
        choice = None
        while not choice:
            choice_str = input("Which todo would you like to remove or go (b)ack? ")
            if choice_str == "b":
                return
            try:
                choice = int(choice_str)
                self.todo_list.remove(choice-1)
            except ValueError:
                print("Invalid choice!")
            except IndexError:
                print("Invalid choice!")

    def edit_todo(self):
        for i, todo in enumerate(self.todo_list.todos):
            print(f"{i+1}. {todo.title}")
        choice = None
        while not choice:
            choice_str = input("Which todo would you like to edit or go (b)ack? ")
            if choice_str == "b":
                return
            try:
                choice = int(choice_str)
                todo = self.todo_list.todos[choice-1]
                self.edit_todo_menu(todo)
            except ValueError:
                print("Invalid choice!")
            except IndexError:
                print("Invalid choice!")    

    def edit_todo_menu(self, todo):
        print("1. Title")
        print("2. Description")
        print("3. Status")
        print("4. Priority")
        print("5. Due Date")
        print("6. Back")
        choice = None
        while not choice:
            choice = input("What would you like to edit? ")
            if choice == "1":
                todo.title = input("Title: ")
            elif choice == "2":
                todo.description = input("Description: ")
            elif choice == "3":
                todo.status = self.get_status()
            elif choice == "4":
                todo.priority = self.get_priority()
            elif choice == "5":
                todo.due_date = self.get_due_date()
            elif choice == "6":
                return
            else:
                print("Invalid choice!")
            choice = None

    def main_menu(self):
        print()
        print("1. Add Todo")
        print("2. List Todos")
        print("3. Remove Todo")
        print("4. Edit Todo")
        print("5. Exit")
        choice = input("What would you like to do? ")
        if choice == "1":
            self.add_todo()
        elif choice == "2":
            self.list_todos()
        elif choice == "3":
            self.remove_todo()
        elif choice == "4":
            self.edit_todo()
        elif choice == "5":
            exit()
        else:
            print("Invalid choice!")

    def run(self):
        print("Welcome to the Todo App!")
        while True:
            self.main_menu()

if __name__ == "__main__":
    app = App()
    app.run()
