import customtkinter as ctk
from src.quick_calc.controller import CalculatorController


class CalculatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.display = None

        self.title("Quick-Calc")
        self.geometry("300x400")

        self.controller = CalculatorController()
        self.current_input = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = ctk.CTkEntry(self, width=260, height=40)
        self.display.pack(pady=20)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]

        frame = ctk.CTkFrame(self)
        frame.pack()

        row = 0
        col = 0

        for btn in buttons:
            button = ctk.CTkButton(
                frame,
                text=btn,
                width=60,
                command=lambda b=btn: self.on_button_click(b)
            )
            button.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, value):
        result_text = self.controller.press(value)
        self.display.delete(0, "end")
        self.display.insert(0, result_text)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()