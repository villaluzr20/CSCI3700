from flask import Flask, jsonify
import psycopg2
from psycopg2 import Error

app = Flask(__name)

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'database': 'uniquefruits',
    'user': 'ryanv0630',
    'password': 'test',
}

# Function to execute SQL query
def execute_query(query, fetch=False):
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        if fetch:
            result = cursor.fetchall()
            return True, result
        return True, "Success!"
    except Error as e:
        return False, str(e)
    finally:
        if connection:
            cursor.close()
            connection.close()

# Route to insert a new row into basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    query = "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');"
    success, message = execute_query(query)
    if success:
        return "Success!"
    else:
        return message

# Route to show unique fruits in basket_a and basket_b in JSON format
@app.route('/api/unique')
def show_unique_fruits():
    query_a = "SELECT DISTINCT fruit_a FROM basket_a;"
    query_b = "SELECT DISTINCT fruit_b FROM basket_b;"
    
    success_a, result_a = execute_query(query_a, fetch=True)
    success_b, result_b = execute_query(query_b, fetch=True)
    
    if success_a and success_b:
        unique_fruits_a = [row[0] for row in result_a]
        unique_fruits_b = [row[0] for row in result_b]
        
        response_data = {
            "unique_fruits_a": unique_fruits_a,
            "unique_fruits_b": unique_fruits_b
        }
        return jsonify(response_data)
    else:
        return jsonify({"error": "Error occurred while fetching data"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5342)
