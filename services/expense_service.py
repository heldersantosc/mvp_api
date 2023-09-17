import logging
from models.expense import Expense
from sqlalchemy.exc import IntegrityError
from exceptions import ValidationError
from schemas.expense_schema import *


def create_expense(data):
    try:
        if data.value <= 0:
            error = CreateNewExpenseValidationResponse().error
            raise ValidationError(error)

        expense = Expense(
            description=data.description,
            value=data.value,
            date_time=data.date_time,
        )
        expense.create()
    except IntegrityError as error:
        logging.error(error.args)
        raise ValueError("Erro ao criar despesa")


def list_expenses():
    try:
        expenses = Expense.get_all()
        expense_schema = ExpenseSchema(many=True)
        expense_json = expense_schema.dump(expenses)
        return expense_json
    except IntegrityError as error:
        logging.error(error.args)
        raise ValueError("Erro ao listar todas despesas")


def total_expenses():
    try:
        total = Expense.get_total()
        return {"total": total}
    except IntegrityError as error:
        logging.error(error.args)
        raise ValueError("Erro ao calcular total de despesas")


def update_expense(id: int, body: UpdateExpenseBodySchema):
    try:
        Expense.update(id=id, value=body.value, description=body.description)
    except IntegrityError as error:
        logging.error(error.args)
        raise ValueError("Erro ao atualizar despesa")


def delete_expense(id: int):
    try:
        Expense.delete(id=id)
    except IntegrityError as error:
        logging.error(error.args)
        raise ValueError("Erro ao deletar despesa")
