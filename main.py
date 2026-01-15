import customtkinter

customtkinter.set_appearance_mode("dark")

maxchiffre = 9
pile_ecran = []
nombre_courant = False
ope_courante = False


def touche_appuyee(touche):
    if touche in ["0","1","2","3","4","5","6","7","8","9","."]:
        traite_touche_chiffre(touche)
    elif touche in ["Plus","Moins","Fois","Diviser","Egal"]:
        traite_touche_operation(touche)
    elif touche == "Reset":
        pile_ecran.clear()
        update_screen()


def _get_nombre_as_text_from_pile():
    text = ''
    for num in pile_ecran:
        text += str(num)
    return text

def _get_nombre_from_pile():
    text = _get_nombre_as_text_from_pile()
    if "." in pile_ecran:
        return float(text)
    else:
        return int(text)

def update_screen(value=False):
    if value:
        screen.configure(text=value[0:9])
    else:
        screen.configure(text="0")

def traite_touche_chiffre(num):
    if len(pile_ecran) < maxchiffre:
        if num == "." and "."  in pile_ecran:
            return
        pile_ecran.append(num)
        update_screen(_get_nombre_as_text_from_pile())

def traite_touche_operation(operation):
    global nombre_courant,ope_courante
    if nombre_courant and ope_courante:
        if ope_courante == "Egal":
            resultat = nombre_courant
        else:
            try:
                execute_operation(ope_courante)
            except ValueError:
                resultat = nombre_courant
    if not nombre_courant:
        nombre_courant = _get_nombre_from_pile()
    ope_courante = operation
    pile_ecran.clear()

def execute_operation(operation):
    global nombre_courant
    if operation:
        nombre2 = _get_nombre_from_pile()
        resultat = 0
        if operation == "Plus":
            resultat = nombre_courant + nombre2
        elif operation == "Moins":
            resultat = nombre_courant - nombre2
        elif operation == "Fois":
            resultat = nombre_courant * nombre2
        elif operation == "Diviser":
            resultat = nombre_courant / nombre2
        nombre_courant = resultat
        pile_ecran.clear()
        update_screen(str(resultat))







app = customtkinter.CTk()
app.title('Caclulatrice 1.0')
app.geometry("380x600")

screen_font = ("Courrier",55,'bold')
screen = customtkinter.CTkLabel(app,text="0",font=screen_font)
screen.grid(row=0,column=0,sticky="E",padx=(10,10),pady=(20,30),columnspan=4)


font_bouton = ("Arial",30,"bold")

btn_0 = customtkinter.CTkButton(app,text="0",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("0"))
btn_1 = customtkinter.CTkButton(app,text="1",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("1"))
btn_2 = customtkinter.CTkButton(app,text="2",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("2"))
btn_3 = customtkinter.CTkButton(app,text="3",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("3"))
btn_4 = customtkinter.CTkButton(app,text="4",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("4"))
btn_5 = customtkinter.CTkButton(app,text="5",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("5"))
btn_6 = customtkinter.CTkButton(app,text="6",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("6"))
btn_7 = customtkinter.CTkButton(app,text="7",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("7"))
btn_8 = customtkinter.CTkButton(app,text="8",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("8"))
btn_9 = customtkinter.CTkButton(app,text="9",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("9"))
btn_plus = customtkinter.CTkButton(app,text="+",width=75, height=180, font=font_bouton, command=lambda : touche_appuyee("Plus"))
btn_moins = customtkinter.CTkButton(app,text="-",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("Moins"))
btn_fois = customtkinter.CTkButton(app,text="x",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("Fois"))
btn_diviser = customtkinter.CTkButton(app,text="/",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("Diviser"))
btn_point = customtkinter.CTkButton(app,text=".",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("."))
btn_egal = customtkinter.CTkButton(app,text="=",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("Egal"))
btn_reset = customtkinter.CTkButton(app,text="Reset",width=75, height=75, font=font_bouton, command=lambda : touche_appuyee("Reset"))

btn_0.grid(row=5,column=0,padx=(10,10),pady=(10,10))
btn_1.grid(row=4,column=0,padx=(10,10),pady=(10,10))
btn_2.grid(row=4,column=1,padx=(10,10),pady=(10,10))
btn_3.grid(row=4,column=2,padx=(10,10),pady=(10,10))
btn_4.grid(row=3,column=0,padx=(10,10),pady=(10,10))
btn_5.grid(row=3,column=1,padx=(10,10),pady=(10,10))
btn_6.grid(row=3,column=2,padx=(10,10),pady=(10,10))
btn_7.grid(row=2,column=0,padx=(10,10),pady=(10,10))
btn_8.grid(row=2,column=1,padx=(10,10),pady=(10,10))
btn_9.grid(row=2,column=2,padx=(10,10),pady=(10,10))
btn_plus.grid(row=4,column=3,padx=(10,10),pady=(10,10),rowspan=2)
btn_moins.grid(row=3,column=3,padx=(10,10),pady=(10,10))
btn_fois.grid(row=2,column=3,padx=(10,10),pady=(10,10))
btn_diviser.grid(row=1,column=3,padx=(10,10),pady=(10,10))
btn_point.grid(row=5,column=1,padx=(10,10),pady=(10,10))
btn_egal.grid(row=5,column=2,padx=(10,10),pady=(10,10))
btn_reset.grid(row=1,column=0,padx=(10,10),pady=(10,10))


app.mainloop()