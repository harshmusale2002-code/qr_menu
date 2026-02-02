from flask import Flask, jsonify
from flask_cors import CORS
from routes.admin_routes import admin_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(admin_bp)

# Import blueprints
from routes.auth_routes import auth_bp
from routes.menu_routes import menu_bp
from routes.order_routes import order_bp
from routes.payment_routes import payment_bp

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(order_bp)
app.register_blueprint(payment_bp)

@app.route("/menu", methods=["GET"])
def get_menu():
    menu = [
        {"id": 1, "name": "Pizza", "price": 250},
        {"id": 2, "name": "Burger", "price": 120},
        {"id": 3, "name": "Cold Drink", "price": 60}
    ]
    return jsonify(menu)

if __name__ == "__main__":
    app.run(debug=True)
