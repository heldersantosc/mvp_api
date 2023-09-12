import logging
from sqlite3 import IntegrityError
from flask import Blueprint, request, jsonify
from schemas.expense_schema import ExpenseSchema
from marshmallow.exceptions import ValidationError
from services.expense_service import create_expense, list_expenses, total_expenses
from sqlalchemy.exc import IntegrityError

expense_bp = Blueprint("expense", __name__)


@expense_bp.post("/")
def create_new_expense():
    try:
        schema = ExpenseSchema()
        expense = schema.load(request.form)
        response = create_expense(expense)
        return jsonify(response)
    except ValidationError as error:
        return jsonify({"error": error.messages}), 400
    except Exception:
        return {"error": "Erro ao cadastrar nova despesa"}, 500


@expense_bp.get("/")
def list_all_expenses():
    try:
        despesas = list_expenses()
        despesa_schema = ExpenseSchema(many=True)
        despesas_json = despesa_schema.dump(despesas)
        return jsonify(despesas_json)
    except Exception as error:
        logging.error(error)
        return {"error": "Erro ao listar despesas"}, 500


@expense_bp.get("/total")
def calculate_total_expenses():
    try:
        response = total_expenses()
        return jsonify(response)
    except Exception as error:
        logging.error(error)
        return {"error": "Erro ao calcular total de despesas"}, 500


# @despesa_bp.route('/atualizar_despesa/<int:id>', methods=['PUT'])
# def atualizar_despesa_endpoint(id):
#     data = request.json
#     response = atualizar_despesa(id, data)
#     return jsonify(response)

# @despesa_bp.route('/deletar_despesa/<int:id>', methods=['DELETE'])
# def deletar_despesa_endpoint(id):
#     response = deletar_despesa(id)
#     return jsonify(response)
