import socket
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

HOST = 'localhost'
PORT = 50007

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((HOST, PORT))

client_socket.listen(1)

conn, addr = client_socket.accept()

cadena = list(range(10))
i = 0
k = 0

if(k == 0):
    based = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Andres601")
        
    micursor = based.cursor()
    micursor.execute("CREATE DATABASE IF NOT EXISTS Agencia")
    print("Base de datos creada")
    micursor.close()
    based.close()
    k = k+1
    
if(k == 1):
    based = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Andres601",
            database="Agencia")

    micursor = based.cursor()
    
    micursor.execute("CREATE TABLE IF NOT EXISTS cliente(cedula INT NOT NULL\
        PRIMARY KEY,nombre VARCHAR(255) NOT NULL);")

    micursor.execute("CREATE TABLE IF NOT EXISTS vuelo(id_Vuelo INT NOT NULL\
        PRIMARY KEY,nombre_Aerolinea VARCHAR(255) NOT NULL, pais_o VARCHAR(255) NOT NULL, pais_d VARCHAR(255) NOT NULL,\
        hora_v VARCHAR(5) NOT NULL, fecha_v VARCHAR(10) NOT NULL, costo_v FLOAT NOT NULL);")

    micursor.execute("CREATE TABLE IF NOT EXISTS cliente_vuelo(cedula_r INT NOT NULL, id_rVuelo INT NOT NULL,\
        FOREIGN KEY (cedula_r) REFERENCES cliente(cedula), FOREIGN KEY (id_rVuelo) REFERENCES vuelo(id_Vuelo));")

    print("Tablas creadas")
    micursor.close()
    based.close()

print(conn, ' conectado por ', addr)


def guardar_datos(cadena):
    based = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Andres601",
                database="Agencia")
    
    sql_select1 = "select * from cliente\
                where cedula=%s"
    
    micursor = based.cursor()
    micursor.execute(sql_select1,(int(cadena[0]),))
    micursor.fetchone()
    
    if micursor.rowcount > 0:
        print("Ya existe el cliente")
    else:
        if cadena[0] != '0':
            sqlIn = "insert into cliente(\
                        cedula, nombre)\
                        values(%s,%s)"
            
            micursor.execute(sqlIn, (int(cadena[0]), cadena[1]))
            based.commit()
            
        sql_select1 = "select * from vuelo\
                    where id_Vuelo=%s"
    
        
        micursor.execute(sql_select1,(int(cadena[2]),))
        micursor.fetchone()
            
        if micursor.rowcount > 0:
            print("Ya existe el vuelo")
                
        else:
            if cadena[2] != '0':
                sqlIn = "insert into vuelo(\
                                id_Vuelo, nombre_Aerolinea, pais_o,\
                                pais_d, hora_v, fecha_v, costo_v)\
                                values(%s,%s,%s,%s,%s,%s,%s)"
    
                micursor.execute(sqlIn, (int(cadena[2]), cadena[3], cadena[4], cadena[5], cadena[6], cadena[7], float(cadena[8])))
    
                #sqlIn = "insert into cliente_vuelo(\
                #                    cedula_r, id_rVuelo) \
                #                    values(%s,%s)"  
                #micursor.execute(sqlIn, (int(cadena[0]), int(cadena[2])))
                                
                based.commit()
                micursor.close()
                based.close()
    
    for j in range(8):
        print(cadena[j])
        
    

while 1:
    data = conn.recv(1024)
    print(type(data))
    cadena[i] = data.decode("utf-8")
    
    #print("El servidor recibio " + cadena)
    i = i+1
    if not data:
        guardar_datos(cadena)

    #conn.sendall(data)


