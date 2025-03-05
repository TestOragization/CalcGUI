import pyodbc
from datetime import datetime


class Calculator:
    def __init__(self):
        self.history = []
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=CalculatorApp;Trusted_Connection=yes'
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def calculate(self, expression: str):
        try:
            result = eval(expression)
            self.add_to_history(expression, result)
            self.user_logs(expression, result)
            return result

        except Exception as e:
            return f"Ошибка: {e}"

    def user_logs(self, action, result):
        query = "INSERT INTO UserLogs (Action, Result) VALUES (?, ?)"
        self.cursor.execute(query, (action, str(result)))
        self.conn.commit()

    def add_to_history(self, expression, result):
        query = "INSERT INTO History (Expression, Result, TimeOfAction) VALUES (?, ?, ?)"
        self.cursor.execute(query, (expression, str(result), datetime.now()))
        self.conn.commit()

    def show_user_logs(self):
        query = "SELECT Action, Result FROM UserLogs"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if rows:
            print("Логи пользователя:")
            for row in rows:
                print(f"Action: {row.Action} | Result: {row.Result}")
        else:
            print("Empty")

    def show_history(self):
        query = "SELECT Expression, Result, TimeOfAction FROM History"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if rows:
            print("История расчетов:")
            for row in rows:
                print(f"{row.Expression} = {row.Result} at {row.TimeOfAction}")
        else:
            print("История пуста.")

    def close(self):
        self.conn.close()