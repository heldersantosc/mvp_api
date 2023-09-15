import logging
from flask import request, jsonify
from flask_openapi3 import APIBlueprint, Tag
from marshmallow.exceptions import ValidationError
from exceptions import NotFoundException
from schemas.expense_schema import *
from services.expense_service import *


tag = Tag(name="Expense", description="Routes to expenses control")
expense_bp = APIBlueprint(
    "expense",
    __name__,
    url_prefix="/api",
    abp_tags=[tag],
    doc_ui=True,
    abp_responses={422: None},
)


@expense_bp.post(
    "/expense",
    summary="Creates a new expense",
    responses={
        201: CreateNewExpenseResponse,
        400: CreateNewExpenseValidationResponse,
        500: CreateNewExpenseErrorResponse,
    },
)
def create_expense_endpoint(form: ExpensesBase):
    try:
        schema = ExpenseSchema()
        expense = schema.load(request.form)
        create_expense(expense)
        return dict(CreateNewExpenseResponse()), 201
    except ValidationError as error:
        return jsonify({"error": error.messages}), 400
    except Exception:
        return dict(CreateNewExpenseErrorResponse()), 500


@expense_bp.get(
    "/expense",
    summary="List all expenses by desc date",
    responses={
        200: ListAllExpensesResponse,
        500: ListAllExpensesErrorResponse,
    },
)
def list_expenses_endpoint():
    try:
        expenses = list_expenses()
        expense_schema = ExpenseSchema(many=True)
        expense_json = expense_schema.dump(expenses)
        # raise Exception
        return jsonify(data=expense_json), 200
    except Exception as error:
        logging.error(error)
        return dict(ListAllExpensesErrorResponse()), 500


@expense_bp.get(
    "/expense/total",
    summary="Sum all expenses values and return total",
    responses={
        200: CalculateTotalResponse,
        500: CalculateTotalErrorResponse,
    },
)
def total_expenses_endpoint():
    try:
        response = total_expenses()
        return jsonify(response), 200
    except Exception as error:
        logging.error(error)
        return dict(CalculateTotalErrorResponse()), 500


@expense_bp.put(
    "/expense/<int:id>",
    summary="Update an expense by id",
    responses={
        200: UpdateExpenseResponse,
        404: UpdateExpenseNotFoundResponse,
        500: UpdateExpenseErrorResponse,
    },
)
def update_expense_endpoint(path: PathIdSchema, body: UpdateExpenseBodySchema):
    try:
        update_expense(path.id, body)
        return dict(UpdateExpenseResponse()), 200
    except NotFoundException as error:
        logging.error(error)
        return dict(UpdateExpenseNotFoundResponse()), 404
    except Exception as error:
        logging.error(error)
        return dict(UpdateExpenseErrorResponse()), 500


@expense_bp.delete(
    "/expense/<int:id>",
    summary="Delete an expense by id",
    responses={
        200: DeleteExpenseResponse,
        404: DeleteExpenseNotFoundResponse,
        500: DeleteExpenseErrorResponse,
    },
)
def delete_expense_endpoint(path: PathIdSchema):
    try:
        delete_expense(path.id)
        return dict(DeleteExpenseResponse()), 200
    except NotFoundException as error:
        logging.error(error)
        return dict(DeleteExpenseNotFoundResponse()), 404
    except Exception as error:
        logging.error(error)
        return dict(DeleteExpenseErrorResponse()), 500
