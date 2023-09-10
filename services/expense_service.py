from models.expense import Expense


def create_expense(data):
    expense = Expense(
        description=data["description"],
        value=data["value"],
        date_time=data["date_time"],
    )
    expense.create()
    return {"message": "Despesa adicionada com sucesso!"}


def list_expenses():
    expenses = Expense.get_all()
    return expenses


def total_expenses():
    total = Expense.get_total()
    return {"total": total}
