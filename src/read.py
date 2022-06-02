import mysql.connector

try:
    connection = mysql.connector.connect(
        host='examtec.cqwj2g7rnvfr.us-east-1.rds.amazonaws.com',
        port='3306',
        user='admin',
        password='552883407a',
        db='examtec'
    )
    if connection.is_connected():
        print("Conexión exitosa.")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM job_travel")
        result = cursor.fetchall()
        for fila in result:
            print("Meter_no:",fila[0], "serial_number:",fila[1], "panel_number:",fila[2], "job_number:",fila[3], "job_name:",fila[4], "seal:",fila[5], "type:",fila[6], "modbus_id:",fila[7])
except Exception as ex:
    print(ex)
finally:
    if connection.is_connected():
        connection.close()
        print("Conexión finalizada.")
