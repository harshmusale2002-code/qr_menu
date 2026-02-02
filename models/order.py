import mysql.connector
from config import db_config

def update_order_status(order_id, status):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "UPDATE orders SET status = %s WHERE id = %s"
    cursor.execute(query, (status, order_id))

    conn.commit()
    cursor.close()
    conn.close()
