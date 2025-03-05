class Calculator:
    def init(self):
        self.history = []

    def calculate(self, expression: str):
        try:
            result = eval(expression)
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            return f"Ошибка: {e}"

    def show_history(self):
        if self.history:
            print("История расчетов:")
            for entry in self.history:
                print(entry)
        else:
            print("История пуста.")