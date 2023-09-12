from pydantic import BaseModel, Field
from marshmallow import Schema, fields, validates, ValidationError
from datetime import datetime
from typing import List


class ExpenseSchema(Schema):
    id = fields.Integer()
    description = fields.String(required=True)
    value = fields.Float(required=True)
    date_time = fields.DateTime(required=True)

    @validates("value")
    def validate_value(self, value):
        message = "O Valor não pode ser menor ou igual a zero."
        if value <= 0:
            raise ValidationError(message)


class ExpensesBase(BaseModel):
    description: str = Field(
        example="Ração para cachorro",
        description="expense description",
    )
    value: float = Field(
        example=189.99,
        description="expense value in R$",
    )
    date_time: datetime = Field(
        example=datetime.now().utcnow(),
        description="expense date and time",
    )


class ListAllExpenses(ExpensesBase):
    id: int = Field(
        example=3,
        description="Expense unique id",
    )


class ListAllExpensesResponse(BaseModel):
    data: List[ListAllExpenses]


class ListAllExpensesErrorResponse(BaseModel):
    error = "Erro ao listar despesas"


class CreateNewExpenseResponse(BaseModel):
    message: str = "Despesa adicionada com sucesso!"


class CreateNewExpenseValidationResponse(BaseModel):
    error = {"value": ["O Valor não pode ser menor ou igual a zero."]}


class CreateNewExpenseErrorResponse(BaseModel):
    error = "Erro ao cadastrar nova despesa"


class CalculateTotalResponse(BaseModel):
    total: float = 989.95


class CalculateTotalErrorResponse(BaseModel):
    error = "Erro ao calcular total de despesas"
