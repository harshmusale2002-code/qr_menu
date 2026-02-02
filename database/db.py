import mysql.connector


conn = mysql.connector.connect(
host="localhost",
user="root",
password="your_password",
database="qr_menu"
)


cursor = conn.cursor(dictionary=True)