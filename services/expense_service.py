from models.expense import Expense
from datetime import datetime


def create_expense(data):
    description = data["description"]
    value = data["value"]
    date_time = datetime.fromisoformat(data["date_time"].replace("Z", ""))

    expense = Expense(description=description, value=value, date_time=date_time)
    expense.create()

    return {"message": "Despesa adicionada com sucesso!"}


def list_expenses():
    expenses = Expense.get_all()
    return expenses


def total_expenses():
    total = Expense.get_total()
    return {"total": total}
