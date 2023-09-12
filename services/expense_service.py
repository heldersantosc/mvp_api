import logging
from models.expense import Expense
from sqlalchemy.exc import IntegrityError


def create_expense(data):
    try:
        expense = Expense(
            description=data["description"],
            value=data["value"],
            date_time=data["date_time"],
        )
        expense.create()
        return {"message": "Despesa adicionada com sucesso!"}
    except IntegrityError as error:
        logging.error(error.args)
        raise ValueError("Erro ao cadastrar no banco de dados")


def list_expenses():
    expenses = Expense.get_all()
    return expenses


def total_expenses():
    total = Expense.get_total()
    return {"total": total}
