import tkinter as tk
from random import randint
from collections import deque

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        self.master.configure(bg="#333333")

        self.fifo_numbers = deque(maxlen=10)
        self.lifo_numbers = deque(maxlen=10)
        self.fifo_running = False
        self.lifo_running = False

        self.frame = tk.Frame(self.master, bg="#333333")
        self.frame.pack(padx=20, pady=20)

        self.generate_button = tk.Button(self.frame, text="Generar Procesos", command=self.generate_numbers, bg="#444444", fg="#ffffff")
        self.generate_button.grid(row=0, column=0, columnspan=2, padx=(5, 2), pady=5, sticky="ew")

        self.fifo_button = tk.Button(self.frame, text="FIFO", command=self.toggle_fifo, bg="#444444", fg="#ffffff")
        self.fifo_button.grid(row=0, column=2, padx=(2, 5), pady=5, sticky="ew")

        self.lifo_button = tk.Button(self.frame, text="LIFO", command=self.toggle_lifo, bg="#444444", fg="#ffffff")
        self.lifo_button.grid(row=0, column=3, padx=(5, 2), pady=5, sticky="ew")

        self.stop_button = tk.Button(self.frame, text="Detener", command=self.stop_processes, bg="#444444", fg="#ffffff")
        self.stop_button.grid(row=0, column=4, padx=2, pady=5, sticky="ew")

        self.analysis_button = tk.Button(self.frame, text="Análisis", command=self.analyze_lists, bg="#444444", fg="#ffffff")
        self.analysis_button.grid(row=0, column=5, columnspan=2, padx=(2, 5), pady=5, sticky="ew")

        self.fifo_label = tk.Label(self.frame, text="FIFO", bg="#333333", fg="#ffffff")
        self.fifo_label.grid(row=1, column=0, padx=(5, 2), pady=5, sticky="ew")

        self.lifo_label = tk.Label(self.frame, text="LIFO", bg="#333333", fg="#ffffff")
        self.lifo_label.grid(row=1, column=2, padx=(2, 5), pady=5, sticky="ew")

        self.output_label = tk.Label(self.frame, text="", bg="#333333", fg="#ff0000", anchor="se")
        self.output_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="sew")

        self.fifo_number_labels = []
        self.lifo_number_labels = []
        self.update_number_labels()

    def generate_numbers(self):
        fifo_numbers = [randint(1, 100) for _ in range(10)]
        lifo_numbers = [randint(1, 100) for _ in range(10)]

        self.fifo_numbers = deque(fifo_numbers)
        self.lifo_numbers = deque(reversed(lifo_numbers))

        self.update_number_labels()

    def analyze_lists(self):
        fifo_list = [randint(1, 100) for _ in range(10)]
        lifo_list = [randint(1, 100) for _ in range(10)]

        self.fifo_numbers = deque(fifo_list)
        self.lifo_numbers = deque(reversed(lifo_list))

        self.update_number_labels()

        self.fifo_running = True
        self.lifo_running = True

        self.show_fifo_order()
        self.show_lifo_order()

    def show_fifo_order(self):
        if self.fifo_running and self.fifo_numbers:
            self.fifo_numbers.popleft()
            self.fifo_numbers.append(None)
            self.update_number_labels()
            self.master.after(1000, self.show_fifo_order)

    def show_lifo_order(self):
        if self.lifo_running and self.lifo_numbers:
            self.lifo_numbers.pop()
            self.lifo_numbers.appendleft(None)
            self.update_number_labels()
            self.master.after(1000, self.show_lifo_order)

    def toggle_fifo(self):
        self.fifo_running = not self.fifo_running
        if self.fifo_running:
            self.show_fifo_order()

    def toggle_lifo(self):
        self.lifo_running = not self.lifo_running
        if self.lifo_running:
            self.show_lifo_order()

    def stop_processes(self):
        self.fifo_running = False
        self.lifo_running = False

    def update_number_labels(self):
        # Clear labels
        for label in self.fifo_number_labels:
            label.grid_forget()
        for label in self.lifo_number_labels:
            label.grid_forget()

        # Create FIFO number labels
        self.fifo_number_labels.clear()
        for i, number in enumerate(self.fifo_numbers):
            label = tk.Label(self.frame, text=str(number) if number is not None else " ", bg="#444444", fg="#ffffff", relief="raised")
            label.grid(row=i + 2, column=0, padx=(5, 2), pady=5, sticky="ew")
            self.fifo_number_labels.append(label)

        # Create LIFO number labels
        self.lifo_number_labels.clear()
        for i, number in enumerate(self.lifo_numbers):
            label = tk.Label(self.frame, text=str(number) if number is not None else " ", bg="#444444", fg="#ffffff", relief="raised")
            label.grid(row=i + 2, column=2, padx=(2, 5), pady=5, sticky="ew")
            self.lifo_number_labels.append(label)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
