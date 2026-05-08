import tkinter as tk
from tkinter import messagebox


class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("现代计算器")
        self.root.geometry("360x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#17181A")

        self.expression = ""

        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display_frame = tk.Frame(
            self.root,
            bg="#17181A"
        )
        self.display_frame.pack(fill="both", padx=20, pady=(30, 10))

        self.expression_label = tk.Label(
            self.display_frame,
            text="",
            anchor="e",
            bg="#17181A",
            fg="#8A8F98",
            font=("Arial", 16)
        )
        self.expression_label.pack(fill="both", pady=(0, 8))

        self.result_entry = tk.Entry(
            self.display_frame,
            font=("Arial", 34, "bold"),
            justify="right",
            bg="#17181A",
            fg="#FFFFFF",
            bd=0,
            insertbackground="#FFFFFF"
        )
        self.result_entry.pack(fill="both", ipady=12)

    def create_buttons(self):
        self.button_frame = tk.Frame(
            self.root,
            bg="#17181A"
        )
        self.button_frame.pack(expand=True, fill="both", padx=18, pady=18)

        buttons = [
            ["C", "←", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for row_index, row in enumerate(buttons):
            for col_index, text in enumerate(row):
                if text == "0":
                    button = self.make_button(text)
                    button.grid(
                        row=row_index,
                        column=col_index,
                        columnspan=2,
                        sticky="nsew",
                        padx=6,
                        pady=6
                    )
                elif row_index == 4 and text in [".", "="]:
                    button = self.make_button(text)
                    button.grid(
                        row=row_index,
                        column=col_index + 1,
                        sticky="nsew",
                        padx=6,
                        pady=6
                    )
                else:
                    button = self.make_button(text)
                    button.grid(
                        row=row_index,
                        column=col_index,
                        sticky="nsew",
                        padx=6,
                        pady=6
                    )

        for i in range(5):
            self.button_frame.rowconfigure(i, weight=1)

        for i in range(4):
            self.button_frame.columnconfigure(i, weight=1)

    def make_button(self, text):
        bg_color = "#2E3035"
        fg_color = "#FFFFFF"
        active_bg = "#3A3D44"

        if text in ["C", "←", "%"]:
            bg_color = "#4E5057"
            active_bg = "#62656E"

        if text in ["÷", "×", "-", "+", "="]:
            bg_color = "#FF9500"
            active_bg = "#FFB143"
            fg_color = "#FFFFFF"

        button = tk.Button(
            self.button_frame,
            text=text,
            font=("Arial", 20, "bold"),
            bg=bg_color,
            fg=fg_color,
            activebackground=active_bg,
            activeforeground="#FFFFFF",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda value=text: self.click(value)
        )

        return button

    def click(self, value):
        if value == "C":
            self.expression = ""
            self.update_display()

        elif value == "←":
            self.expression = self.expression[:-1]
            self.update_display()

        elif value == "=":
            self.calculate()

        else:
            value = self.convert_operator(value)
            self.expression += value
            self.update_display()

    def convert_operator(self, value):
        if value == "÷":
            return "/"
        if value == "×":
            return "*"
        return value

    def update_display(self):
        self.expression_label.config(text=self.expression)

        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(tk.END, self.expression)

    def calculate(self):
        try:
            if not self.expression:
                return

            result = eval(self.expression)

            self.expression_label.config(text=self.expression)
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(tk.END, str(result))

            self.expression = str(result)

        except ZeroDivisionError:
            messagebox.showerror("错误", "除数不能为 0")
            self.expression = ""
            self.update_display()

        except Exception:
            messagebox.showerror("错误", "表达式不合法")
            self.expression = ""
            self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()