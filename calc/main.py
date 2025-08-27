import customtkinter as ctk
from core import calculate

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Калькулятор")
        self.geometry("300x400")

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)

        self.display = ctk.CTkEntry(self, font=("Arial", 24), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            ctk.CTkButton(self, text=button, font=("Arial", 18), command=action).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        clear_button = ctk.CTkButton(self, text="C", font=("Arial", 18), command=self.clear_display)
        clear_button.grid(row=row_val, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        delete_button = ctk.CTkButton(self, text="⌫", font=("Arial", 18), command=self.delete_last_char)
        delete_button.grid(row=row_val, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.display.get()
                result = calculate(expression)
                self.display.delete(0, "end")
                self.display.insert("end", str(result))
            except Exception as e:
                self.display.delete(0, "end")
                self.display.insert("end", "Ошибка")
        else:
            self.display.insert("end", char)

    def clear_display(self):
        self.display.delete(0, "end")
        
    def delete_last_char(self):
        current_text = self.display.get()
        self.display.delete(len(current_text)-1)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()