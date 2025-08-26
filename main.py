import tkinter as tk
LIGHTPINK = "#FFB6C1"
LIGHTORANGE = "#F99747"
WHITE = "#FFF4E9"
FUSHIA = "#F04D86"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x700")
        self.window.title("Simple Calculator")
        self.window.resizable(0, 0)
        self.current_expression = ""
        self.total_expression= ""
        self.display_frame=self.create_display_frame()
        self.current_label, self.total_label = self.create_display_labels()
        self.button_digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)}
        self.operators = {
            "/": "/", "*":"*",  "-":"-", "+":"+"}
        self.button_operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.button_clear = "CE"
        self.button_equals = "="
        self.button_square = "x²"  
        self.button_square_root = "√"
        self.button_plus_minus = "+/-"
        self.buttons_frame=self.create_buttons_frame()
        for x in range(1,5):
            self.buttons_frame.grid_rowconfigure(x, weight=1)
            self.buttons_frame.grid_columnconfigure(x, weight=1)
        self.create_digit_buttons=self.digit_buttons()
        self.create_operation_buttons=self.operation_buttons()
        self.create_clear_button=self.clear_button()
        self.create_equals_button=self.equals_button()
        self.create_square_button=self.square_button()
        self.create_square_root_button=self.square_root_button()
        self.create_plus_minus_button=self.plus_minus_button()
        self.bind_key=self.find_key()


    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()


    def plus_minus(self):
        self.current_expression = str(float(self.current_expression) * -1) if self.current_expression else ""
        self.update_current_label()


    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression += "="
            self.update_total_label()
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_current_label()


    def square(self):
        self.current_expression = str(float(self.current_expression) ** 2)
        self.update_current_label()
   
    def square_root(self):
        self.current_expression = str(float(self.current_expression) ** 0.5)
        self.update_current_label()


    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, padx=24, font=("Monoid", 16), bg=WHITE, fg=LIGHTPINK)
        total_label.pack(expand=True, fill=tk.BOTH)
        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, padx=24, font=("Monoid", 40), bg=WHITE, fg=LIGHTPINK)
        current_label.pack(expand=True, fill=tk.BOTH)
        return current_label, total_label
   
    def create_display_frame(self):
        display_frame = tk.Frame(self.window, height=175, bg="LIGHTPINK")
        display_frame.pack(expand=True, fill=tk.BOTH)
        return display_frame
   
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_current_label()


    def find_key(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.button_digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.button_operators:
            self.window.bind(key, lambda event, operator=self.operators[key]: self.operation_appender(operator))


    def operation_appender(self, operator):
            self.total_expression += self.current_expression
            self.total_expression += operator
            self.current_expression = ""
            self.update_total_label()
            self.update_current_label()
   
    def operation_buttons(self):
        r=0
        for operator, grid_value in self.button_operators.items():
            button = tk.Button(self.buttons_frame, text=str(grid_value),
            font=("Monoid", 43), bg=LIGHTORANGE, fg=WHITE, borderwidth=0,
            command=lambda x=operator: self.operation_appender(x))
            button.grid(row=r, column=4, sticky=tk.NSEW)
            r += 1


    def digit_buttons(self):
        for digit, grid_value in self.button_digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), font=("Monoid", 43),
            bg=LIGHTORANGE, fg=WHITE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)



    def clear_button(self):
        button = tk.Button(self.buttons_frame, text=self.button_clear, font=("Monoid", 43), bg=LIGHTORANGE, fg=WHITE, borderwidth=0)
        button.grid(row=0, column=1, sticky=tk.NSEW)
        button.config(command=self.clear)
   
    def equals_button(self):
        button = tk.Button(self.buttons_frame, text=self.button_equals, font=("Monoid", 43), bg=FUSHIA, fg=WHITE, borderwidth=0)
        button.grid(row=4, column=4, columnspan=1, sticky=tk.NSEW)
        button.config(command=self.evaluate)
   
    def square_button(self):
        button = tk.Button(self.buttons_frame, text=self.button_square, font=("Monoid", 43), bg=LIGHTORANGE, fg=WHITE, borderwidth=0)
        button.grid(row=0, column=2, columnspan=1, sticky=tk.NSEW)
        button.config(command=self.square)


    def square_root_button(self):
        button = tk.Button(self.buttons_frame, text=self.button_square_root, font=("Monoid", 43), bg=LIGHTORANGE, fg=WHITE, borderwidth=0)
        button.grid(row=0, column=3, columnspan=1, sticky=tk.NSEW)
        button.config(command=self.square_root)
   
    def plus_minus_button(self):
        button = tk.Button(self.buttons_frame, text=self.button_plus_minus, font=("Monoid", 43), bg=LIGHTORANGE, fg=WHITE, borderwidth=0)
        button.grid(row=4, column=3, columnspan=1, sticky=tk.NSEW)
        button.config(command=self.plus_minus)
   
    def create_buttons_frame(self):      
        button_frame = tk.Frame(self.window, height=475, bg=LIGHTORANGE)
        button_frame.pack(expand=True, fill=tk.BOTH)
        return button_frame
   
    def update_current_label(self):
        self.current_label.config(text=self.current_expression [:10])


    def update_total_label(self):
        expression=self.total_expression
        for operator, symbol in self.button_operators.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)
   




    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()



