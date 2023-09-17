from datetime import datetime
from models.expense import Expense, db


expenses_seed = [
    Expense(
        description="Gasolina para o carro",
        value=80.25,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Almoço em restaurante",
        value=35.90,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Manutenção do veículo",
        value=200.00,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Roupas e acessórios",
        value=75.50,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Assinatura de streaming",
        value=12.99,
        date_time=datetime.utcnow(),
    ),
    Expense(description="Farmácia", value=45.30, date_time=datetime.utcnow()),
    Expense(
        description="Café da manhã no café local",
        value=7.25,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Presente de aniversário",
        value=50.00,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Jantar em família",
        value=90.00,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Taxa de estacionamento",
        value=10.75,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Assinatura de academia",
        value=50.00,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Internet e TV a cabo",
        value=85.99,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Material de escritório",
        value=25.50,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Cinema com amigos",
        value=15.75,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Café e lanche no trabalho",
        value=20.00,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Taxa de estacionamento do shopping",
        value=7.50,
        date_time=datetime.utcnow(),
    ),
    Expense(
        description="Taxa de entrega de comida",
        value=8.25,
        date_time=datetime.utcnow(),
    ),
]


def seed_expense_table():
    if db.session.query(Expense).count() == 0:
        db.session.bulk_save_objects(expenses_seed)
        db.session.commit()
