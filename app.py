from flask import Flask
from config import Config
from models import db
from routes import app

app.config.from_object(Config)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
