from tkinter import *

ventana = Tk()
ventana.title("Interes simple")
ventana.geometry("1000x600")
interes=0
capital=0
periodos=0

def int_simple():
	Co=float(capital_ent.get())
	i =  float(interes_ent.get())
	n = float(periodos_ent.get())
	interes_compuesto = Co*(1+(i*n/100))
	interes_compuesto = round(interes_compuesto,2)
	lb_resultado.insert(0,interes_compuesto)






#entry_datos

#entry_interes
interes_ent = Entry(ventana,bg = "LightSeaGreen",font=("Arial",23))
interes_ent.place(x=220,y=60,width=170,height=50)

#entry_capital_inicial
capital_ent = Entry(ventana,bg="Aquamarine",font=("Arial",23))
capital_ent.place(x=220,y=250,width=170,height=50)

#entry_periodos
periodos_ent = Entry(ventana,bg="DarkSeaGreen",font=("Arial",23))
periodos_ent.place(x=220,y=450,width=170,height=50)

#botones

#boton_calcular
btn_calcular = Button(ventana,text= "calcular",font=("Arial",20),command=int_simple)
btn_calcular.place(x=500,y=250,width=200,height=70)

#Labels

#Label_interes

lb_interes = Label(ventana,text="interes:", font =("Arial",20) )
lb_interes.place(x=20,y=50,width=200,height=70) 

#label_capital_inicial

lb_cap_in = Label(ventana, text="Capital inicial:",font=("Arial",20))
lb_cap_in.place(x=20,y=250,width=200,height=70)

#label_periodos
lb_periodos= Label(ventana,text="Periodos:",font=("Arial",20))
lb_periodos.place(x=20,y=450,width=200,height=70)

lb_resultado = Entry(ventana,font=("Arial",20))
lb_resultado.place(x=700,y=250,width=200,height=70)

lb_ramirez = Label(ventana,text="Calculadora Interes Simple By Juandivox",font=("Arial",20))
lb_ramirez.place(x=400,y=100,width=600,height=70)







ventana.mainloop() 


