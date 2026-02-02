from flask import Blueprint, jsonify, request
from models.order import get_all_orders, update_order_status

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/orders", methods=["GET"])
def all_orders():
    orders = get_all_orders()
    return jsonify(orders)

@admin_bp.route("/admin/order/<int:order_id>/status", methods=["PUT"])
def update_status(order_id):
    status = request.json["status"]
    update_order_status(order_id, status)
    return jsonify({"message": "Status updated"})
