# app.py

from flask import Flask, jsonify
from routes import main

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(main)

    # Error handling
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal Server Error"}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

