import logging
from flask import request, jsonify
from flask_openapi3 import APIBlueprint, Tag
from schemas.expense_schema import *
from marshmallow.exceptions import ValidationError
from services.expense_service import create_expense, list_expenses, total_expenses


tag = Tag(name="Expense", description="Routes do expenses control")
expense_bp = APIBlueprint(
    "expense",
    __name__,
    url_prefix="/expense",
    abp_tags=[tag],
    doc_ui=True,
    abp_responses={422: None},
)


@expense_bp.post(
    "/",
    summary="Creates a new expense",
    responses={
        201: CreateNewExpenseResponse,
        400: CreateNewExpenseValidationResponse,
        500: CreateNewExpenseErrorResponse,
    },
)
def create_new_expense(form: ExpensesBase):
    try:
        schema = ExpenseSchema()
        expense = schema.load(request.form)
        create_expense(expense)
        return dict(CreateNewExpenseResponse()), 201
    except ValidationError as error:
        return jsonify({"error": error.messages}), 400
    except Exception:
        return {"error": "Erro ao cadastrar nova despesa"}, 500


@expense_bp.get(
    "/",
    summary="List all expenses by desc date",
    responses={200: ListAllExpensesResponse},
)
def list_all_expenses():
    try:
        expenses = list_expenses()
        expense_schema = ExpenseSchema(many=True)
        expense_json = expense_schema.dump(expenses)
        return jsonify(data=expense_json), 200
    except Exception as error:
        logging.error(error)
        return dict(ListAllExpensesErrorResponse()), 500


@expense_bp.get(
    "/total",
    summary="Sum all expenses and return total",
    responses={
        200: CalculateTotalResponse,
        200: CalculateTotalErrorResponse,
    },
)
def calculate_total_expenses():
    try:
        response = total_expenses()
        return jsonify(response), 200
    except Exception as error:
        logging.error(error)
        return dict(CalculateTotalErrorResponse()), 500


# @despesa_bp.route('/atualizar_despesa/<int:id>', methods=['PUT'])
# def atualizar_despesa_endpoint(id):
#     data = request.json
#     response = atualizar_despesa(id, data)
#     return jsonify(response)

# @despesa_bp.route('/deletar_despesa/<int:id>', methods=['DELETE'])
# def deletar_despesa_endpoint(id):
#     response = deletar_despesa(id)
#     return jsonify(response)
