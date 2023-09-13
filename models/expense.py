from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc, func

from exceptions import NotFoundException

db = SQLAlchemy()


class Expense(db.Model):
    __tablename__ = "expense"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, description, value, date_time):
        self.description = description
        self.value = value
        self.date_time = date_time

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update(cls, id: int, value: float, description: str):
        updated_rows = (
            db.session.query(cls)
            .filter_by(id=id)
            .update({"value": value, "description": description})
        )

        if updated_rows == 0:
            raise NotFoundException(f"Despesa {id} não encontrada!")

        db.session.commit()

    @classmethod
    def delete(cls, id: int):
        deleted_rows = db.session.query(cls).filter_by(id=id).delete()

        if deleted_rows == 0:
            raise NotFoundException(f"Despesa {id} não encontrada!")

        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.order_by(desc(cls.date_time)).all()

    @classmethod
    def get_total(cls):
        query_sum = func.round(func.sum(cls.value), 2)
        return db.session.query(query_sum).scalar()
