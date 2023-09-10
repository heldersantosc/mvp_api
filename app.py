import os
from flask import Flask
from models.expense import db
from controllers.expense_controller import expense_bp

basedir = os.path.abspath(os.path.dirname(__file__))
database = os.path.join(basedir, "database.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + database

db.init_app(app)


with app.app_context():
    db.create_all()
    db.session.close()


app.register_blueprint(expense_bp, url_prefix="/expense")

if __name__ == "__main__":
    app.run(debug=True)
