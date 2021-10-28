import math


class Equation:
    def __init__(self, input_string):
        self.input = input_string
        self.format = "ax^2+bx+c"
        self.values = {}
        self.x1 = 0
        self.x2 = 0

    def recognize(self):
        reference = []
        current = ""
        i = self.input
        for token in self.format:
            if token in i:
                if token != "+":
                    current += token
            else:
                if current != "":
                    reference.append(current)
                    i = i.replace(current, "")
                    current = ""

        f_pend_index = 0
        i_pend_index = 0

        for token in reference:
            f_start_index = self.format[f_pend_index:].find(token)+f_pend_index
            fend_index = f_start_index + len(token)
            dict_key = self.format[f_pend_index:f_start_index]
            dict_key = dict_key.replace("+", "")
            f_pend_index = fend_index

            i_start_index = self.input[i_pend_index:].find(token)+i_pend_index
            i_end_index = i_start_index + len(token)
            dict_value = self.input[i_pend_index:i_start_index]
            dict_value = dict_value.replace("+", "")
            i_pend_index = i_end_index

            dict_value = int(dict_value)
            self.values.update({dict_key: dict_value})

        dict_key = self.format[f_pend_index:]
        dict_key = dict_key.replace("+", "")

        dict_value = self.input[i_pend_index:]
        dict_value = dict_value.replace("+", "")

        dict_value = int(dict_value)
        self.values.update({dict_key: dict_value})

    def calculate(self):
        a = self.values.get("a", 0)
        b = self.values.get("b", 0)
        c = self.values.get("c", 0)

        d = (b**2)-(4*a*c)
        if d > 0:
            self.x1 = (-b + math.sqrt(d)) / (2*a)
            self.x2 = (-b - math.sqrt(d)) / (2*a)

    def display(self):
        print(self.x1)
        print(self.x2)

    def set_display(self, form):
        self.format = form


if __name__ == "__main__":
    e = Equation("12x^2-34x+6")
    e.recognize()
    e.calculate()
    e.display()
