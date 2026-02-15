from flask import Flask
from sqlmodel import SQLModel
from database import engine
from errors.error_handlers import register_error_handlers
from controllers import user_router
SQLModel.metadata.create_all(engine)

app = Flask(__name__)
register_error_handlers(app)
app.register_blueprint(user_router, url_prefix='/user')

if __name__ == "__main__":
    app.run()
