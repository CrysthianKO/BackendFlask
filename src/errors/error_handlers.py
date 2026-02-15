from flask import app, jsonify
from pydantic import ValidationError
from .exception import UserAlreadyExistsError


def register_error_handlers(app):

    @app.errorhandler(UserAlreadyExistsError)
    def handle_user_exists(e):
        return jsonify({"error": "Conflict", "message": str(e)}), 409

    @app.errorhandler(ValidationError)
    def handle_invalid_data(e):
        return jsonify({"error": "invalid data", "message": str(e)}), 422
