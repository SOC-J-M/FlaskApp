from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

db_config = {
    'host': '106.0.63.154',
    'user': 'pdc1647_Test1101',
    'password': 'jmpTest1101',
    'database': 'pdc1647_Test1101'
}

# establish connection to mysql server
# connection = pymysql.connect(**db_config)


@app.route('/data', methods=['POST'])
def post_data():
    data = request.json

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    sql = "SELECT MAX(`key`) AS last_key FROM record"
    cursor.execute(sql)
        
    # Fetch the result
    result = cursor.fetchone()
    
    if result:
        last_key = result[0]

    time_stamp = data['time_stamp']
    reporting_node = data['reporting_node']
    department = data['department']
    work_center = data['work_center']
    employee_id = data['employee_id']
    part_number = data['part_number']
    quantity = data['quantity']
    work_order = data['work_order']
    start_time = data['start_time']
    end_time = data['end_time']
    sequence_num = data['sequence_num']
    progress = data['progress']
    setup_time = data['setup_time']
    die_set = data['die_set']
    material_lot = data['material_lot']
    status_code = data['status_code']
    comments = data['comments']

    print(time_stamp, reporting_node, department)

    sql = "INSERT into record (`key`, time_stamp, reporting_node, department, work_center, employee_id, part_number, quantity, work_order, start_time, end_time, sequence_num, progress, setup_time, die_set, material_lot, status_code, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    cursor.execute(sql, (last_key+1, time_stamp, reporting_node, department, work_center, employee_id, part_number, quantity, work_order, start_time, end_time, sequence_num, progress, setup_time, die_set, material_lot, status_code, comments))

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Data inserted successfully"}), 201



@app.route('/values', methods=['GET'])
def get_data():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    sql = "SELECT * FROM record LIMIT 10"
    cursor.execute(sql)

    results = cursor.fetchall()

    for result in results:
        print(result)
    
    cursor.close()
    connection.close()

    if results:
        return 'Success'
    else:
        return 'Failed'
    
if __name__ == "__main__":
    app.run(debug=True)
