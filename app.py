import os
from flask_openapi3 import Info, OpenAPI
from flask_cors import CORS
from models.expense import db
from controllers.expense_controller import expense_bp
from seed import seed_expense_table

info = Info(title="Expenses management", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

with app.app_context():
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir, "database.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + database

    db.init_app(app)
    db.create_all()

    seed_expense_table()
    db.session.close()

app.register_api(expense_bp)


if __name__ == "__main__":
    app.run(debug=True)
