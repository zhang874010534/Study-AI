import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("计算器")
        self.root.geometry("320x420")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.result = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 14), padding=10)
        
        self.display = tk.Entry(self.root, font=('Arial', 24), justify='right', 
                                bd=10, bg='#f0f0f0', relief='sunken')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew')
        self.display.insert(0, '0')
        
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('%', 5, 3),
        ]
        
        for text, row, col in buttons:
            btn = ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, text):
        if text == 'C':
            self.expression = ""
            self.result = ""
            self.display.delete(0, tk.END)
            self.display.insert(0, '0')
        elif text == '=':
            try:
                if self.expression:
                    self.result = str(eval(self.expression))
                    self.display.delete(0, tk.END)
                    self.display.insert(0, self.result)
                    self.expression = self.result
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
                self.expression = ""
        elif text == '%':
            try:
                if self.expression:
                    self.result = str(eval(self.expression) / 100)
                    self.display.delete(0, tk.END)
                    self.display.insert(0, self.result)
                    self.expression = self.result
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
                self.expression = ""
        else:
            if self.display.get() == '0' or self.display.get() == 'Error':
                self.display.delete(0, tk.END)
            self.expression += text
            self.display.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()