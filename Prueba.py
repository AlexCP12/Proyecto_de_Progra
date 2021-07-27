import os
from tkinter import * 
from tkinter import messagebox
os.system("cls")



def crearFactura():
    ventanacf = Toplevel()
    ventanacf.geometry("450x400+100+100")
    ventanacf.title("Crear Factura")

    global factura 
    global codigo 
    global detalle
    global precio
    global cantidad

    lblNumFac = Label(ventanacf,text="Indique el número de factura:", font=("Agency FB", 14)).place(x=10,y=10)
    txtNumFac = Entry(ventanacf,textvariable=factura,width=30).place(x=10,y=50)
 
    lblCodPro = Label(ventanacf,text="Indique el código del producto:", font=("Agency FB", 14)).place(x=10,y=70)
    txtCodPro = Entry(ventanacf,textvariable=codigo,width=30).place(x=10,y=100)

    lblDetalle = Label(ventanacf,text="Indique el detalle del producto: ", font=("Agency FB", 14)).place(x=10,y=120)
    txtDetalle = Entry(ventanacf,textvariable=detalle,width=30).place(x=10,y=150)

    lblPrecio = Label(ventanacf,text="Indique el precio unitario: ", font=("Agency FB", 14)).place(x=10,y=170)
    txtPrecio = Entry(ventanacf,textvariable=precio,width=30).place(x=10,y=200)

    lblCantidad = Label(ventanacf,text="Indique la cantidad de productos:", font=("Agency FB", 14)).place(x=10,y=220)
    txtCantidad = Entry(ventanacf,textvariable=cantidad,width=30).place(x=10,y=250)
    
    
    btnCFactura = Button(ventanacf,text="Crear Factura",command=CFactura, font=("Agency FB",14), width=12).place(x=20,y=280)

def CFactura():
    global facturas
    global factura 
    global codigo 
    global detalle
    global precio
    global cantidad
    global facturasl
    facturasl = {codigo.get():[detalle.get(),precio.get(),cantidad.get()]}
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

    lblNumFac = Label(ventanaAf,text="Indique el número de factura:", font=("Agency FB", 14)).place(x=10,y=10)
    txtNumFac = Entry(ventanaAf,textvariable=factura,width=30).place(x=10,y=50)

    lblCodPro = Label(ventanaAf,text="Indique el código del producto:", font=("Agency FB", 14)).place(x=10,y=70)
    txtCodPro = Entry(ventanaAf,textvariable=codigo,width=30).place(x=10,y=100)

    lblDetalle = Label(ventanaAf,text="Indique el detalle del producto: ", font=("Agency FB", 14)).place(x=10,y=120)
    txtDetalle = Entry(ventanaAf,textvariable=detalle,width=30).place(x=10,y=150)

    lblPrecio = Label(ventanaAf,text="Indique el precio unitario: ", font=("Agency FB", 14)).place(x=10,y=170)
    txtPrecio = Entry(ventanaAf,textvariable=precio,width=30).place(x=10,y=200)

    lblCantidad = Label(ventanaAf,text="Indique la cantidad de productos:", font=("Agency FB", 14)).place(x=10,y=220)
    txtCantidad = Entry(ventanaAf,textvariable=cantidad,width=30).place(x=10,y=250)
        
    btnCFactura = Button(ventanaAf,text="Agregar Producto",command=agProducto, font=("Agency FB",14), width=12).place(x=20,y=280)
    
def agProducto():
    global facturas
    global factura 
    global codigo 
    global detalle
    global precio
    global cantidad
    global facturasl
    facturasl = {codigo.get():[detalle.get(),precio.get(),cantidad.get()]}
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
facturas = {}
factura = IntVar()
codigo = IntVar()
detalle= StringVar()
precio = IntVar()
cantidad= IntVar()
btnCrearFactura = Button(ventana,text="Crear Factura",command=crearFactura, font=("Agency FB",14), width=12).place(x=200,y=20)
btnAgregar = Button(ventana,text="Agregar Factura", command=agregarFactura, font=("Agency FB",14), width=12).place(x=200,y=70)
btnCalcular = Button(ventana,text="Calcular",command=calcularTotalVentas, font=("Agency FB",14), width=12).place(x=200,y=120)
btnBuscar = Button(ventana,text="Buscar",command=buscarFactura, font=("Agency FB",14), width=12).place(x=200,y=170)
ventana.mainloop()