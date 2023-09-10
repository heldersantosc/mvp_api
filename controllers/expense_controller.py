from flask import Blueprint, request, jsonify
from schemas.expense_schema import ExpenseSchema
from services.expense_service import create_expense, list_expenses, total_expenses

expense_bp = Blueprint("expense", __name__)


@expense_bp.post("/")
def criar_despesa():
    data = request.json
    response = create_expense(data)
    return jsonify(response)


@expense_bp.get("/")
def listar_todas_despesas():
    despesas = list_expenses()
    despesa_schema = ExpenseSchema(many=True)
    despesas_json = despesa_schema.dump(despesas)
    return jsonify(despesas_json)


@expense_bp.get("/total")
def calcular_total_despesas():
    response = total_expenses()
    return jsonify(response)


# @despesa_bp.route('/atualizar_despesa/<int:id>', methods=['PUT'])
# def atualizar_despesa_endpoint(id):
#     data = request.json
#     response = atualizar_despesa(id, data)
#     return jsonify(response)

# @despesa_bp.route('/deletar_despesa/<int:id>', methods=['DELETE'])
# def deletar_despesa_endpoint(id):
#     response = deletar_despesa(id)
#     return jsonify(response)
