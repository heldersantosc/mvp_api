from pydantic import BaseModel, Field, validator
from marshmallow import Schema, fields
from datetime import datetime
from typing import List


class ExpenseSchema(Schema):
    """
    Schema para listar os produtos e usar o many=true
    """

    id = fields.Integer()
    description = fields.String()
    value = fields.Float()
    date_time = fields.DateTime()


class ExpensesBase(BaseModel):
    """
    Schema para validar o form da rota post
    """

    description: str = Field(
        example="Ração para cachorro",
        description="expense description",
    )
    value: float = Field(
        example=189.99,
        description="expense value in R$",
    )
    date_time: datetime = Field(
        example=datetime.now().isoformat(),
        description="expense date and time in iso format",
    )

    @validator("value")
    def validate_value(cls, value):
        if value <= 0:
            raise ValueError("O valor não pode ser menor ou igual a zero")
        return value

    @validator("description")
    def validate_description_length(cls, description):
        if len(description) < 3:
            raise ValueError("A descrição deve ter pelo menos 3 caracteres")
        return description


class ListAllExpenses(ExpensesBase):
    """
    Schema que herda de ExpensesBase para listar as despesas com o atributo id
    """

    id: int = Field(
        example=3,
        description="Expense unique id",
    )


class PathIdSchema(BaseModel):
    """
    Parâmetro id para as rotas
    """

    id: int = Field(..., description="id from unique expense")


class ListAllExpensesResponse(BaseModel):
    """
    Schema para retornar uma lista de Despesas
    """

    data: List[ListAllExpenses]


class ListAllExpensesErrorResponse(BaseModel):
    error = "Erro ao listar despesas"


class CreateNewExpenseResponse(BaseModel):
    message = "Despesa adicionada com sucesso!"


class CreateNewExpenseValidationResponse(BaseModel):
    error = "O Valor não pode ser menor ou igual a zero."


class CreateNewExpenseErrorResponse(BaseModel):
    error = "Erro ao cadastrar nova despesa"


class CalculateTotalResponse(BaseModel):
    total: float = 989.95


class CalculateTotalErrorResponse(BaseModel):
    error = "Erro ao calcular total de despesas"


class UpdateExpenseBodySchema(BaseModel):
    value: float = Field(
        gt=0,
        example=32.4,
        error_msg="O valor da despesa dever ser maior que 0",
        description="price that will be updated",
    )
    description: str = Field(
        example="Pão de forma",
        description="new description for expense",
    )


class UpdateExpenseResponse(BaseModel):
    message = "Despesa atualizada com sucesso"


class UpdateExpenseNotFoundResponse(BaseModel):
    error = "Despesa informada não encontrada"


class UpdateExpenseErrorResponse(BaseModel):
    error = "Erro ao atualizar despesa"


class DeleteExpenseResponse(BaseModel):
    message = "Despesa deletada com sucesso"


class DeleteExpenseNotFoundResponse(BaseModel):
    error = "Despesa informada não encontrada"


class DeleteExpenseErrorResponse(BaseModel):
    error = "Erro ao deletar despesa"
