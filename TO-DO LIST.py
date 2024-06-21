import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        # Title label
        self.title_label = tk.Label(root, text="ALL TASK", font=("Arial", 16), fg="white", bg="#2c3e50")
        self.title_label.pack(fill=tk.X)
        
        # Frame for input and add button
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 14))
        self.task_entry.pack(side=tk.LEFT, padx=10)
        
        self.add_button = tk.Button(self.input_frame, text="ADD", width=10, font=("Arial", 14), command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        # Task listbox
        self.task_listbox = tk.Listbox(root, width=45, height=10, font=("Arial", 12), bg="#2c3e50", fg="white", selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)
        
        # Frame for update and delete buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.update_button = tk.Button(self.button_frame, text="UPDATE", width=10, font=("Arial", 14), command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(self.button_frame, text="DELETE", width=10, font=("Arial", 14), command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)
        
        # Clear all button
        self.clear_button = tk.Button(root, text="CLEAR ALL", width=10, font=("Arial", 14), bg="#e74c3c", fg="white", command=self.clear_tasks)
        self.clear_button.pack(pady=10)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            # Number the task
            task_number = self.task_listbox.size() + 1
            task_with_number = f"{task_number}. {task}"
            self.task_listbox.insert(tk.END, task_with_number)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)
            task_number, current_task = selected_task.split('. ', 1)
            
            new_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=current_task)
            if new_task:
                new_task_with_number = f"{task_number}. {new_task}"
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task_with_number)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            # Re-number tasks after deletion
            self.renumber_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
    
    def renumber_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(tasks, 1):
            task_text = task.split('. ', 1)[1]
            renumbered_task = f"{i}. {task_text}"
            self.task_listbox.insert(tk.END, renumbered_task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
