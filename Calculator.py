# Calculator

# Import the tkinter module for creating the desktop based GUI applications
import tkinter


class Calculator:
    # Initialize the methods
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title(string="Calculator")
        self.window.geometry(newGeometry="375x667")
        # self.window.resizable(width=0, height=0)

        self.digit_buttons = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 1), ".": (4, 0)
        }

        self.operator_buttons = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.total_expression = ""
        self.result_expression = ""

        self.label_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        for x in range(0, 4):
            self.button_frame.rowconfigure(index=x, weight=3)
            self.button_frame.columnconfigure(index=x, weight=3)

        self.total_expression_label, self.result_expression_label = self.create_display_label()

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        # self.create_clear_button()
        # self.create_equals_button()
        self.create_square_button()
        self.create_square_root_button()
        self.bind_keys()

    def create_display_label(self):
        total_expression_label = tkinter.Label(master=self.label_frame, text=self.total_expression, anchor=tkinter.E, bg="light gray", fg="black", padx=24, font=("Arial", 16))
        total_expression_label.pack(expand=True, fill=tkinter.BOTH)

        result_expression_label = tkinter.Label(master=self.label_frame, text=self.result_expression, anchor=tkinter.E,
                                               bg="light gray", fg="black", padx=24, font=("Arial", 40, 'bold'))
        result_expression_label.pack(expand=True, fill=tkinter.BOTH)

        return total_expression_label, result_expression_label

    def add_to_expression(self, value):
        self.result_expression += str(value)
        self.update_result_expression_label()

    def append_operator(self, operator):
        self.result_expression += operator
        self.total_expression += self.result_expression
        self.result_expression = ''

        self.update_total_expression_label()
        self.update_result_expression_label()

    def update_total_expression_label(self):
        expression = self.total_expression
        for operator, symbol in self.operator_buttons.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_expression_label.config(text=expression)

    def update_result_expression_label(self):
        self.result_expression_label.config(text=self.result_expression)

    def create_digit_buttons(self):
        for digit, position in self.digit_buttons.items():
            digit_button = tkinter.Button(master=self.button_frame, text=digit, bg="white", fg="black",
                                          font=("Arial", 24, 'bold'), borderwidth=0, command=lambda x=digit : self.add_to_expression(value=x))

            digit_button.grid(row=position[0], column=position[1], columnspan=1, sticky=tkinter.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operators, symbols in self.operator_buttons.items():
            operator_button = tkinter.Button(master=self.button_frame, text=symbols, bg="white", fg="blue",
                                             font=("Arial", 24, "bold"), borderwidth=0, command=lambda x=operators : self.append_operator(operator=x))
            operator_button.grid(row=i, column=3, sticky=tkinter.NSEW)
            i += 1

    def create_special_buttons(self):
        self.create_clear_button() ; self.create_equals_button()

    def clear_function(self):
        self.total_expression = ''
        self.result_expression = ''

        self.update_total_expression_label()
        self.update_result_expression_label()

    def equals_function(self):
        self.total_expression += self.result_expression
        self.update_total_expression_label()

        try:
            self.result_expression = str(eval(self.total_expression))
            self.total_expression = ''
        except Exception:
            self.result_expression = "Error"
        finally:
            self.update_result_expression_label()

    def square_function(self):
        self.result_expression = str(eval(f'{self.result_expression}') ** 2)
        self.update_total_expression_label()
        self.update_result_expression_label()

    def square_root_function(self):
        self.result_expression = str(eval(f'{self.result_expression}') ** 0.5)
        self.update_total_expression_label()
        self.update_result_expression_label()

    def create_clear_button(self):
        clear_button = tkinter.Button(master=self.button_frame, text="C", bg="white", fg="red",
                                    font=("Arial", 24, "bold"), borderwidth=0, command=self.clear_function)
        clear_button.grid(row=0, column=0, sticky=tkinter.NSEW)

    def create_equals_button(self):
        equals_button = tkinter.Button(master=self.button_frame, text="=", bg="white", fg="green",
                                       font=("Arial", 24, "bold"), borderwidth=0, command=self.equals_function)
        equals_button.grid(row=4, column=2, sticky=tkinter.NSEW, columnspan=2)

    def create_square_button(self):
        square_button = tkinter.Button(master=self.button_frame, text='x\u00b2', bg="white", fg="blue",
                                       font=("Arial", 24, "bold"), borderwidth=0, command=self.square_function)
        square_button.grid(row=0, column=1, sticky=tkinter.NSEW)

    def create_square_root_button(self):
        square_root_button = tkinter.Button(master=self.button_frame, text='\u221ax', bg="white", fg="blue",
                                            font=("Arial", 24, 'bold'), borderwidth=0, command=self.square_root_function)
        square_root_button.grid(row=0, column=2, sticky=tkinter.NSEW)

    def create_display_frame(self):
        frame = tkinter.Frame(master=self.window, height=221, bg="light gray")
        frame.pack(expand=True, fill=tkinter.BOTH)
        return frame

    def create_button_frame(self):
        frame = tkinter.Frame(master=self.window)
        frame.pack(expand=True, fill=tkinter.BOTH)
        return frame

    def bind_keys(self):
        self.window.bind(sequence="<Return>", func=lambda event: self.equals_function())
        self.window.bind(sequence="<.>", func=lambda event : self.add_to_expression())

        for key in self.digit_buttons:
            self.window.bind(sequence=key, func=lambda event, digit=key : self.add_to_expression(value=digit))

        for key in self.operator_buttons:
            self.window.bind(sequence=key, func=lambda event, operator=key : self.add_to_expression(value=operator))

    def start(self):
        self.window.mainloop()


if __name__ == "__main__": 
    calculator = Calculator()
    calculator.start()

