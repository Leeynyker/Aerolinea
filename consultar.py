# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:08:08 2020

@author: leeyn
"""


from tkinter import *
from tkinter import messagebox
import tkinter.font
import tkinter as tk
#from PIL import Image, ImageDraw
from PIL import Image, ImageDraw, ImageFont
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


class origen(object):
    
    def __int__(self):
        self.pcod= ""
        self.self.pcode= ""
        
    def mostra(self,datos):
        
        tbl1=tk.Tk()
        tbl1.geometry("1000x170")
        tbl1.title("Agregar vuelo")
        tbl1.configure(background = "#ABCDEF")
                      
        Tagr = Label(tbl1, text="vuelo "+str(datos[0]))
        Tagr.pack(anchor=CENTER)
        Tagr.config(background="#ABCDEF", font=("Verdena",15))
                    
        r = Text(tbl1,width=120,height=4)
        r.insert(INSERT,"id_Vuelo\t\tNombre Aerolinea\t\tPais de Origen\t\tPais de Destino\t\tHora del Vuelo\t\tFecha del Vuelo\t\tCosto del Vuelo")
        r.insert(INSERT,"\n_______________________________________________________________________________________________________________________\n\n")
        r.insert(INSERT,str(datos[0])+"\t\t"+datos[1]+"\t\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        print(str(datos[0])+"\t\t"+datos[1]+"\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        r.config(state=DISABLED)
        r.pack()
        r.place(x=30,y=40)
        
        btnSa = Button(tbl1, text = "Salir", command = tbl1.destroy)
        btnSa.pack()
        btnSa.place(x = 700, y = 130)
        
        
    def consul(self):
        
        based = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Andres601",
        database="agencia")

        micursor = based.cursor()
        
        try:
            #Selecciona el registro cuyo codigo sea el ingresado
            sql_select1 = "select * from vuelo where pais_o = %s"
            
            codb = self.pcod.get()
                
            print(sql_select1)
            
            # tupla con 1 elemento
            micursor.execute(sql_select1,(codb,))
            fila = micursor.fetchone()
            print(micursor.rowcount)
            if micursor.rowcount <= 0:
                messagebox.showinfo('Base de datos', 'No existe vuelo con origen '+str(codb))
            else:
                self.mostra(fila)
#                print("hptaaaaaaaaa")
#                print("---------------------------------------------")
#                print("Codigo = ", fila[0])
#                print("Nombre = ", fila[1])
#                print("Primer nota = ", fila[2])
#                print("Segunda nota = ", fila[3])
#                print("Nota final = ", fila[4])
#                print("Promedio = ", fila[5])
#                print("---------------------------------------------")
            self.pcode.destroy()
            micursor.close()
            based.close()

        except Error as e :
            print ("Error en conexion ", e)
#            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        
    def pcod(self):
        self.pcode=tk.Tk()
        self.pcode.geometry("210x100")
        self.pcode.title("Buscar vuelo")
        self.pcode.configure(background = "#ABCDEF")
                      
        Tpcode = Label(self.pcode, text="Digite el origen del vuelo")
        Tpcode.pack(anchor=CENTER)
        Tpcode.config(background="#ABCDEF", font=("Verdena",11))
            
        #Entrada de datos
        
        self.pcod = tk.Entry(self.pcode, width = 21)
        self.pcod.pack(anchor=CENTER)
        self.pcod.place(x = 45, y = 30)
        
        btnbus = Button(self.pcode, text = "Buscar", command = self.consul)
        btnbus.pack()
        btnbus.place(x = 45, y = 70)
        
        btnbusS = Button(self.pcode, text = "Cancelar", command = self.pcode.destroy)
        btnbusS.pack()
        btnbusS.place(x = 120, y = 70)
        
        
class destino(object):
    
    def __int__(self):
        self.pcod= ""
        self.self.pcode= ""
        
    def mostra(self,datos):
        
        tbl1=tk.Tk()
        tbl1.geometry("1000x170")
        tbl1.title("Agregar vuelo")
        tbl1.configure(background = "#ABCDEF")
                      
        Tagr = Label(tbl1, text="vuelo "+str(datos[0]))
        Tagr.pack(anchor=CENTER)
        Tagr.config(background="#ABCDEF", font=("Verdena",15))
                    
        r = Text(tbl1,width=120,height=4)
        r.insert(INSERT,"id_Vuelo\t\tNombre Aerolinea\t\tPais de Origen\t\tPais de Destino\t\tHora del Vuelo\t\tFecha del Vuelo\t\tCosto del Vuelo")
        r.insert(INSERT,"\n_______________________________________________________________________________________________________________________\n\n")
        r.insert(INSERT,str(datos[0])+"\t\t"+datos[1]+"\t\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        print(str(datos[0])+"\t\t"+datos[1]+"\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        r.config(state=DISABLED)
        r.pack()
        r.place(x=30,y=40)
        
        btnSa = Button(tbl1, text = "Salir", command = tbl1.destroy)
        btnSa.pack()
        btnSa.place(x = 700, y = 130)
        
        
    def consul(self):
        
        based = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Andres601",
        database="agencia")

        micursor = based.cursor()
        
        try:
            #Selecciona el registro cuyo codigo sea el ingresado
            sql_select1 = "select * from vuelo where pais_d = %s"
            
            codb = self.pcod.get()
                
            print(sql_select1)
            
            # tupla con 1 elemento
            micursor.execute(sql_select1,(codb,))
            fila = micursor.fetchone()
            print(micursor.rowcount)
            if micursor.rowcount <= 0:
                messagebox.showinfo('Base de datos', 'No existe vuelo con destino '+str(codb))
            else:
                self.mostra(fila)
#                print("hptaaaaaaaaa")
#                print("---------------------------------------------")
#                print("Codigo = ", fila[0])
#                print("Nombre = ", fila[1])
#                print("Primer nota = ", fila[2])
#                print("Segunda nota = ", fila[3])
#                print("Nota final = ", fila[4])
#                print("Promedio = ", fila[5])
#                print("---------------------------------------------")
            self.pcode.destroy()
            micursor.close()
            based.close()

        except Error as e :
            print ("Error en conexion ", e)
#            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        
    def pcod(self):
        self.pcode=tk.Tk()
        self.pcode.geometry("210x100")
        self.pcode.title("Buscar vuelo")
        self.pcode.configure(background = "#ABCDEF")
                      
        Tpcode = Label(self.pcode, text="Digite el destino del vuelo")
        Tpcode.pack(anchor=CENTER)
        Tpcode.config(background="#ABCDEF", font=("Verdena",11))
            
        #Entrada de datos
        
        self.pcod = tk.Entry(self.pcode, width = 21)
        self.pcod.pack(anchor=CENTER)
        self.pcod.place(x = 45, y = 30)
        
        btnbus = Button(self.pcode, text = "Buscar", command = self.consul)
        btnbus.pack()
        btnbus.place(x = 45, y = 70)
        
        btnbusS = Button(self.pcode, text = "Cancelar", command = self.pcode.destroy)
        btnbusS.pack()
        btnbusS.place(x = 120, y = 70)

class aerolinea(object):
    
    def __int__(self):
        self.pcod= ""
        self.self.pcode= ""
        
    def mostra(self,datos):
        
        tbl1=tk.Tk()
        tbl1.geometry("1000x170")
        tbl1.title("Agregar vuelo")
        tbl1.configure(background = "#ABCDEF")
                      
        Tagr = Label(tbl1, text="vuelo "+str(datos[0]))
        Tagr.pack(anchor=CENTER)
        Tagr.config(background="#ABCDEF", font=("Verdena",15))
                    
        r = Text(tbl1,width=120,height=4)
        r.insert(INSERT,"id_Vuelo\t\tNombre Aerolinea\t\tPais de Origen\t\tPais de Destino\t\tHora del Vuelo\t\tFecha del Vuelo\t\tCosto del Vuelo")
        r.insert(INSERT,"\n_______________________________________________________________________________________________________________________\n\n")
        r.insert(INSERT,str(datos[0])+"\t\t"+datos[1]+"\t\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        print(str(datos[0])+"\t\t"+datos[1]+"\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        r.config(state=DISABLED)
        r.pack()
        r.place(x=30,y=40)
        
        btnSa = Button(tbl1, text = "Salir", command = tbl1.destroy)
        btnSa.pack()
        btnSa.place(x = 700, y = 130)
        
        
    def consul(self):
        
        based = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Andres601",
        database="agencia")

        micursor = based.cursor()
        
        try:
            #Selecciona el registro cuyo codigo sea el ingresado
            sql_select1 = "select * from vuelo where nombre_Aerolinea = %s"
            
            codb = self.pcod.get()
                
            print(sql_select1)
            
            # tupla con 1 elemento
            micursor.execute(sql_select1,(codb,))
            fila = micursor.fetchone()
            print(micursor.rowcount)
            if micursor.rowcount <= 0:
                messagebox.showinfo('Base de datos', 'No existe vuelo con aerolinea '+str(codb))
            else:
                self.mostra(fila)
#                print("hptaaaaaaaaa")
#                print("---------------------------------------------")
#                print("Codigo = ", fila[0])
#                print("Nombre = ", fila[1])
#                print("Primer nota = ", fila[2])
#                print("Segunda nota = ", fila[3])
#                print("Nota final = ", fila[4])
#                print("Promedio = ", fila[5])
#                print("---------------------------------------------")
            self.pcode.destroy()
            micursor.close()
            based.close()

        except Error as e :
            print ("Error en conexion ", e)
#            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        
    def pcod(self):
        self.pcode=tk.Tk()
        self.pcode.geometry("210x100")
        self.pcode.title("Buscar vuelo")
        self.pcode.configure(background = "#ABCDEF")
                      
        Tpcode = Label(self.pcode, text="Digite el aerolinea del vuelo")
        Tpcode.pack(anchor=CENTER)
        Tpcode.config(background="#ABCDEF", font=("Verdena",11))
            
        #Entrada de datos
        
        self.pcod = tk.Entry(self.pcode, width = 21)
        self.pcod.pack(anchor=CENTER)
        self.pcod.place(x = 45, y = 30)
        
        btnbus = Button(self.pcode, text = "Buscar", command = self.consul)
        btnbus.pack()
        btnbus.place(x = 45, y = 70)
        
        btnbusS = Button(self.pcode, text = "Cancelar", command = self.pcode.destroy)
        btnbusS.pack()
        btnbusS.place(x = 120, y = 70)
        
        
class fecha(object):
    
    def __int__(self):
        self.pcod= ""
        self.self.pcode= ""
        
    def mostra(self,datos):
        
        tbl1=tk.Tk()
        tbl1.geometry("1000x170")
        tbl1.title("Agregar vuelo")
        tbl1.configure(background = "#ABCDEF")
                      
        Tagr = Label(tbl1, text="vuelo "+str(datos[0]))
        Tagr.pack(anchor=CENTER)
        Tagr.config(background="#ABCDEF", font=("Verdena",15))
                    
        r = Text(tbl1,width=120,height=4)
        r.insert(INSERT,"id_Vuelo\t\tNombre Aerolinea\t\tPais de Origen\t\tPais de Destino\t\tHora del Vuelo\t\tFecha del Vuelo\t\tCosto del Vuelo")
        r.insert(INSERT,"\n_______________________________________________________________________________________________________________________\n\n")
        r.insert(INSERT,str(datos[0])+"\t\t"+datos[1]+"\t\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        print(str(datos[0])+"\t\t"+datos[1]+"\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        r.config(state=DISABLED)
        r.pack()
        r.place(x=30,y=40)
        
        btnSa = Button(tbl1, text = "Salir", command = tbl1.destroy)
        btnSa.pack()
        btnSa.place(x = 700, y = 130)
        
        
    def consul(self):
        
        based = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Andres601",
        database="agencia")

        micursor = based.cursor()
        
        try:
            #Selecciona el registro cuyo codigo sea el ingresado
            sql_select1 = "select * from vuelo where fecha_v = %s"
            
            codb = self.pcod.get()
                
            print(sql_select1)
            
            # tupla con 1 elemento
            micursor.execute(sql_select1,(codb,))
            fila = micursor.fetchone()
            print(micursor.rowcount)
            if micursor.rowcount <= 0:
                messagebox.showinfo('Base de datos', 'No existe vuelo con fecha '+str(codb))
            else:
                self.mostra(fila)
#                print("hptaaaaaaaaa")
#                print("---------------------------------------------")
#                print("Codigo = ", fila[0])
#                print("Nombre = ", fila[1])
#                print("Primer nota = ", fila[2])
#                print("Segunda nota = ", fila[3])
#                print("Nota final = ", fila[4])
#                print("Promedio = ", fila[5])
#                print("---------------------------------------------")
            self.pcode.destroy()
            micursor.close()
            based.close()

        except Error as e :
            print ("Error en conexion ", e)
#            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        
    def pcod(self):
        self.pcode=tk.Tk()
        self.pcode.geometry("210x100")
        self.pcode.title("Buscar vuelo")
        self.pcode.configure(background = "#ABCDEF")
                      
        Tpcode = Label(self.pcode, text="Digite el fecha del vuelo")
        Tpcode.pack(anchor=CENTER)
        Tpcode.config(background="#ABCDEF", font=("Verdena",11))
            
        #Entrada de datos
        
        self.pcod = tk.Entry(self.pcode, width = 21)
        self.pcod.pack(anchor=CENTER)
        self.pcod.place(x = 45, y = 30)
        
        btnbus = Button(self.pcode, text = "Buscar", command = self.consul)
        btnbus.pack()
        btnbus.place(x = 45, y = 70)
        
        btnbusS = Button(self.pcode, text = "Cancelar", command = self.pcode.destroy)
        btnbusS.pack()
        btnbusS.place(x = 120, y = 70)

class Listard(object):
    
    def __init__(self):
        self.k = ""
    
    def listado(self):
        
        lis=tk.Tk()
        lis.geometry("1000x500")
        lis.title("Agregar vuelo")
        lis.configure(background = "#ABCDEF")
                      
        Llis = Label(lis, text="vuelos ")
        Llis.pack(anchor=CENTER)
        Llis.config(background="#ABCDEF", font=("Verdena",20))
                    
        based = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Andres601",
        database="agencia")
        
        #Selecciona toda la tabla vuelos
        sql_select1 = "select * from vuelo"
        micursor = based.cursor()
        
        micursor.execute(sql_select1)
        records = micursor.fetchall()
        
        r = Text(lis,width=120)
        r.insert(INSERT,"id_Vuelo\t\tNombre Aerolinea\t\tPais de Origen\t\tPais de Destino\t\tHora del Vuelo\t\tFecha del Vuelo\t\tCosto del Vuelo")
        r.insert(INSERT,"\n_______________________________________________________________________________________________________________________\n\n")
        for datos in records:
            r.insert(INSERT,str(datos[0])+"\t\t"+datos[1]+"\t\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
            r.insert(INSERT,"\n_______________________________________________________________________________________________________________________\n\n")
        print(str(datos[0])+"\t\t"+datos[1]+"\t\t"+str(datos[2])+"\t\t"+str(datos[3])+"\t\t"+str(datos[4])+"\t\t"+str(datos[5])+"\t\t"+str(datos[6]))
        
        r.config(state=DISABLED)
        r.pack()
        r.place(x=30,y=40)
        
        btnSa = Button(lis, text = "Salir", command = lis.destroy)
        btnSa.pack()
        btnSa.place(x = 800, y = 420)


based = mysql.connector.connect( 
        host="localhost",
        user="root",
        passwd="Andres601")

#Crear el marco principal
marco = tk.Tk()
marco.title("Vuelos")
marco.geometry("400x200")
marco.configure(background = "#ABCDEF")

                #Label para el titulo
Title = Label(marco, text="Aeropuerto")
Title.pack(anchor=CENTER)
Title.config(background="#ABCDEF",
        font=("Verdena",24))
            
obagr=Listard()
obbus=origen()
oblis=destino()
obelim=aerolinea()
obmod=fecha()
    #botones 
btnAgregar = Button(marco, text = "Origen", command = obbus.pcod)
btnAgregar.pack()
btnAgregar.place(x = 70, y = 100)

btnCon = Button(marco, text = "Destino", command = oblis.pcod)
btnCon.pack()
btnCon.place(x = 210, y = 100)

btnLis = Button(marco, text = "Aerolinea", command = obelim.pcod)
btnLis.pack()
btnLis.place(x = 290, y = 100)

btnbor = Button(marco, text = "Fecha", command = obmod.pcod)
btnbor.pack()
btnbor.place(x = 150, y = 100)

btnbol = Button(marco, text = "Vuelos", command = obagr.listado )
btnbol.pack()
btnbol.place(x = 180, y = 150)

#count = 0
micursor = based.cursor()
#micursor.execute("SHOW DATABASES")
#for nom in micursor:
#    dbExis = nom
#    print("",dbExis)
#    if nom == "('sistema',)":
#        count = count+1
#    else:
#        print("",nom)
#                
#if count>0:
#    messagebox.showinfo('Base de datos', 'La base de datos ya existe')
#else:
try:
   micursor.execute("CREATE DATABASE sistema")
   messagebox.showinfo('Base de datos', 'Base de datos creada')
   
   
   
except Error:
    print("Funciannaaaaaaaaaaaa")
    messagebox.showinfo('Base de datos', 'LA BASE DE DATOS YA EXISTE')
    

    
    
micursor.close()
based.close()

mainloop()