import os
from tkinter import * 
from tkinter import messagebox

os.system("cls")

def mensaje():
    messagebox.showinfo("Su Factura se ha creado exitosamente")

def crearFactura():
    ventanacf = Toplevel()
    ventanacf.geometry("450x400+100+100")
    ventanacf.title("Crear Factura")
    #ventanacf.configure(bg="#cdcdcb")

    global factura 
    global codigo 
    global detalle
    global precio
    global cantidad
    global listaP

    lblNumFac = Label(ventanacf,text="Indique el número de factura:",   font=("Agency FB", 10)).place(x=10,y=10)
    txtNumFac = Entry(ventanacf,textvariable=factura,width=20).place(x=10,y=30)

    lblCantidad = Label(ventanacf,text="Indique la cantidad del producto:", font=("Agency FB", 10)).place(x=200,y=10)
    txtCantidad = Entry(ventanacf,textvariable=cantidad,width=19).place(x=200,y=30)
    btnCFactura = Button(ventanacf,text="Salir",command=ventanacf.destroy, font=("Agency FB",16), width=12).place(x=180,y=280)
    listaP=Listbox(ventanacf, width= 20, height=5)
    listaP.pack(pady=60)
    for i in listaProductos:
        listaP.insert(0,i)

    Button(ventanacf,text='Crear Factura', command=CFactura).pack()
    show = Label(ventanacf)
    show.pack()


def CFactura():
    global listaP
    global facturas
    global factura 
    global codigo   
    global detalle
    global precio
    global cantidad
    global facturasl

    i = listaP.get(ANCHOR)
    codigo=listaProductos[i][0]  
    detalle= i 
    precio = listaProductos[i][1]
    facturasl = {codigo:[detalle,precio,cantidad.get()]}
    facturas[factura.get()] = facturasl
    print(facturas)
    return facturas

def agregarFactura():

    ventanaAf = Toplevel()
    ventanaAf.geometry("450x400+100+100")
    ventanaAf.title("Agregar Producto a la Factura")

    global facturas
    global factura 
    global codigo 
    global detalle
    global precio
    global cantidad
    global listaP

    lblNumFac = Label(ventanaAf,text="Indique el número de factura:", font=("Agency FB", 10)).place(x=10,y=10)
    txtNumFac = Entry(ventanaAf,textvariable=factura,width=20).place(x=10,y=30)

    lblCantidad = Label(ventanaAf,text="Indique la cantidad del producto:", font=("Agency FB", 10)).place(x=200,y=10)
    txtCantidad = Entry(ventanaAf,textvariable=cantidad,width=19).place(x=200,y=30)

    listaP=Listbox(ventanaAf, width= 20, height=5)
    listaP.pack(pady=60)
    for i in listaProductos:
        listaP.insert(0,i)

        
    btnCFactura = Button(ventanaAf,text="Agregar Producto",command=agProducto, font=("Agency FB",16), width=20).place(x=20,y=280)
    btnCFactura = Button(ventanaAf,text="Salir",command=ventanaAf.destroy, font=("Agency FB",16), width=12).place(x=180,y=280)

def agProducto():
    global facturas
    global factura 
    global codigo 
    global detalle
    global precio
    global cantidad
    global facturasl
    global listaP

    i = listaP.get(ANCHOR)
    codigo=listaProductos[i][0]  
    detalle= i 
    precio = listaProductos[i][1]
    facturasl = {codigo:[detalle,precio,cantidad.get()]}
    facturas[factura.get()].update(facturasl)
    print(facturas)       
    return facturas


def calcularTotalVentas():
    global facturas

    suma = 0
    for precio in facturas:
        for total in facturas[precio]:
            valor = facturas[precio][total][1]
            cantidad = facturas[precio][total][2]
            suma += (valor * cantidad )
    mensaje = "El total de la factura es: ", suma
    messagebox.showinfo(message= mensaje , title="Total")
    print()

def buscarFactura ():
    ventanaBf = Toplevel()
    ventanaBf.geometry("450x400+100+100")
    ventanaBf.title("Buscar Factura")
    global factura
    lblNumFac = Label(ventanaBf,text="Indique el número de factura:", font=("Agency FB", 14)).place(x=10,y=10)
    txtNumFac = Entry(ventanaBf,textvariable=factura,width=30).place(x=10,y=50)
    btnCFactura = Button(ventanaBf,text="Buscar Factura",command=mensajeFac, font=("Agency FB",14), width=12).place(x=20,y=280)
    

def mensajeFac ():
    global factura
    global facturas
    try:
        factural = facturas[factura.get()]
        productos=0
        sumatoria=0
        for total in factural:
            valor = factural[total][1]
            cantidad = factural[total][2]
            sumatoria += (valor*cantidad)
            productos+=cantidad
        mensaje = "el total de la factura es de",sumatoria,"y el total de productos es de",productos
        messagebox.showinfo(message= mensaje , title="Total")
    except:
        mensaje = "La factura no existe"
        messagebox.showinfo(message= mensaje , title="Total")  

ventana = Tk()
ventana.geometry("450x300+100+100")
ventana.title("Sistema de Factutación")

menuP= Menu(ventana)
ventana.config(menu=menuP)
archivo = Menu(ventana)
menuP.add_cascade(label="Archivo",menu=archivo)
archivo.add_command(label="Crear Farctura",command=crearFactura)
archivo.add_command(label="Buscar Facturas",command=buscarFactura)
archivo.add_command(label="Cierre Total",command=calcularTotalVentas)
archivo.add_command(label="Salir",command=ventana.destroy)

editar = Menu(ventana)
menuP.add_cascade(label="Editar",menu=editar)
editar.add_command(label="Agregar Productos",command=agregarFactura)

"""img = PhotoImage(file="imagen.gif")
label = Label(ventana,image=img)
label.place(x=0, y=0)"""


facturas = {}
listaProductos = {"Arroz":[10,1200],"Frijoles":[15,1000],"Papas tostadas":[30,100],"Fideos":[45, 800],"tortillas":[300,750],"Carton de Huevos":[201,1500],"Imperial":[102,850],"Leche":[603,900],"Pan":[507,500],"Queso":[356,1000],"Atun":[709,1100],"Aceite":[908,950],"Galletas":[167,500]}
factura = IntVar()  
codigo = IntVar()
detalle= StringVar()
precio = IntVar()
cantidad= IntVar()
listaP = Listbox

ventana.mainloop()



#{10:["Arroz",1200],15:["Frijoles",1000],30:["Papas tostadas",100],45:["Fideos", 800],300:["tortillas",750],201:["Carton de Huevos",1500],102:["Imperial",850],603:["Leche",900],507:["Pan",500],356:["Queso",1000],709:["Atun",1100],908:["Aceite",950],167:["Galletas",500]}