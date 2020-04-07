import socket
import select
import errno
import sys

HOST = 'localhost'
PORT = 50007

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.setblocking (False)

cedula_u = int(input(f"Digite la cedula del cliente: "))
client_socket.send(str(cedula_u).encode())

nombre_u = input("Digite el nombre del cliente: ")
client_socket.sendall(nombre_u.encode())

id_v = input("Digite el id del vuelo: ")
client_socket.sendall(id_v.encode())

nombre_a = input("Digite el nombre de la aerolinea: ")
client_socket.send(nombre_a.encode())

pais_o = input("Digite el pais de origen del vuelo: ")
client_socket.send(pais_o.encode())

pais_d = input("Digite el pais de destino del vuelo: ")
client_socket.send(pais_d.encode())

hora_v = input("Digite la hora del vuelo: ")
client_socket.send(hora_v.encode())

fecha_v = input("Digite la fecha del vuelo: ")
client_socket.send(fecha_v.encode())

costo_v = float(input("Digite el costo del vuelo: "))
client_socket.send(str(costo_v).encode())

client_socket.close()

