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
        while True:
            try:
                serialnumber = str(input('Ingrese el Número de serie: '))
                break
            except:
                print('Valor incorrecto!! intentalo nuevamente')
        while True:
            try:
                panelnumber = str(input('Ingrese el número de panel: '))
                break
            except:
                print('Valor incorrecto!! intentalo nuevamente')
        while True:
            try:
                jobnumber = str(input('Ingrese el número de trabajo: '))
                break
            except:
                print('Valor incorrecto!! intentalo nuevamente')
        while True:
            try:
                jobname = str(input('Ingrese el nombre de trabajo: '))
                break
            except:
                print('Valor incorrecto!! intentalo nuevamente')
        while True:
            try:
                seal_ = str(input('Sello: '))
                break
            except:
                print('Valor incorrecto!! intentalo nuevamente')
        while True:
            try:
                type_ = str(input('Ingrese el tipo: '))
                break
            except:
                print('Valor incorrecto!! intentalo nuevamente')
        while True:
            try:
                modbusid = int(input('Ingrese el ID de Modbus: '))
                break
            except:
                print('Debes excribir un numero')
        sent = "INSERT INTO job_travel (serial_number,panel_number,job_number,job_name,seal,type,modbus_id) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(serialnumber,panelnumber,jobnumber,jobname,seal_,type_,modbusid)
        cursor.execute(sent)
        connection.commit()
        print("Registro insertado exitosamente.")
except Exception as ex:
    print(ex)
finally:
    if connection.is_connected():
        connection.close()
        print("Conexión finalizada.")
